"""Main entry point for Echoes of the Aethelgard Spire."""

from __future__ import annotations
import argparse
import sys
from rich.panel import Panel
from rich.align import Align
from rich import box

from engine.models import GameState
from engine.world_builder import World
from engine.ui import console, render_dashboard
from engine.commands import process_command
from engine.save_system import list_saves, load_game, save_game


TITLE_ART = r"""[bold bright_cyan]
                     ▲
                    ╱ ╲                   STRATUM +3 : Celestial Observatory & Crown
                   ╱ ◈ ╲
                  ╠═════╣                 STRATUM +2 : Aetherial Botanical Domes
                 ╱ ╲ ☼ ╱ ╲
                ╠═════════╣               STRATUM +1 : The Mnemonic Archives
               ╱   ║ │ ║   ╲
              ╠════╬═●═╬════╣             STRATUM  0 : Grand Clockwork Atrium (0m)
              ║    ║ │ ║    ║
              ╠════╩═══╩════╣             STRATUM -1 : Sunken Aqueducts & Labs
               ╲  ≈≈≈│≈≈≈  ╱
                ╠════╪════╣               STRATUM -2 : Geothermal Foundry
                 ╲ ♨ │ ♨ ╱
                  ╠══╪══╣                 STRATUM -3 : The Bioluminescent Abyss
                   ╲ ★ ╱
                    ╲▼╱[/bold bright_cyan]
[bold bright_white]         E C H O E S   O F   T H E   A E T H E L G A R D   S P I R E[/bold bright_white]
[dim italic]                A Seven-Stratum Mystery of Memory, Light, and Clockwork[/dim italic]
"""

PROLOGUE_TEXT = (
    "[italic]Cold brine laps against your fingers. You open your eyes to a cathedral of wet black "
    "basalt four hundred meters beneath the earth. Your head throbs with a hollow ache: you cannot "
    "remember your name, how you descended into this chasm, or why your hand clutches an empty quartz "
    "phial labeled 'OBLIVION DRAUGHT'.\n\n"
    "Above you rises the Aethelgard Spire—seven vertical levels of subterranean sluices, geothermal "
    "furnaces, alchemical aqueducts, giant clockwork pendulums, cryptographic libraries, sunlit "
    "botanical domes, and a starlit observatory crown. To uncover who you are and why your memories "
    "were sealed inside seven crystalline cylinders, you must craft tools, take careful field notes, "
    "chart the fog-shrouded strata, and ascend toward the light.[/italic]"
)


def show_title_screen() -> None:
    console.print(
        Panel(
            Align.center(TITLE_ART + "\n" + PROLOGUE_TEXT),
            border_style="bright_cyan",
            box=box.DOUBLE_EDGE,
            padding=(1, 3),
        )
    )


def interactive_startup_menu() -> tuple[World, GameState, str]:
    show_title_screen()
    saves = list_saves()
    if saves:
        console.print(
            f"[bold cyan]Found {len(saves)} saved expedition(s).[/bold cyan] "
            "Press [bold yellow]Enter[/bold yellow] for a New Game, type [bold green]continue[/bold green] "
            "to load your most recent save, or [bold green]load <slot>[/bold green]:"
        )
        try:
            choice = console.input("[bold bright_cyan]Start > [/bold bright_cyan]").strip()
        except (EOFError, KeyboardInterrupt):
            sys.exit(0)

        if choice.lower() in ("c", "continue", "resume"):
            latest_slot = saves[0]["slot"]
            w, s, msg = load_game(latest_slot)
            if w and s:
                return w, s, msg
        elif choice.lower().startswith("load"):
            parts = choice.split(maxsplit=1)
            slot = parts[1] if len(parts) > 1 else saves[0]["slot"]
            w, s, msg = load_game(slot)
            if w and s:
                return w, s, msg

    world = World()
    state = GameState()
    return (
        world,
        state,
        "[bold bright_cyan]✦ You awaken upon the Obsidian Slab at Stratum -3. Type `help` for commands or `hint` if you ever need guidance.[/bold bright_cyan]",
    )


def run_game_loop(world: World, state: GameState, initial_message: str, clear_screen: bool = False) -> None:
    feedback = initial_message
    while True:
        if clear_screen:
            console.clear()
        render_dashboard(world, state, feedback)

        if state.game_won:
            console.print(
                Panel(
                    "[bold bright_green]Congratulations on completing Echoes of the Aethelgard Spire![/bold bright_green]\n"
                    "You may continue exploring the Spire, `save` your completed file, or type `quit` to exit.",
                    border_style="bright_green",
                )
            )
            state.game_won = False  # Allow continued post-game exploration if desired

        try:
            room = world.rooms[state.current_room_id]
            prompt_str = f"\n[bold bright_cyan]\\[Z={room.stratum:+d} {room.coord}][/bold bright_cyan] [bold white]Command > [/bold white]"
            user_in = console.input(prompt_str)
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Saving progress to 'autosave' before exiting...[/dim]")
            save_game(world, state, "autosave")
            break

        res = process_command(world, state, user_in)
        if res.new_world is not None and res.new_state is not None:
            world = res.new_world
            state = res.new_state
        feedback = res.message
        if res.should_quit:
            console.print(f"\n[bold cyan]{feedback}[/bold cyan]")
            break


def main() -> None:
    parser = argparse.ArgumentParser(description="Echoes of the Aethelgard Spire — 3D Terminal Text Adventure")
    parser.add_argument("--new", action="store_true", help="Start a new game immediately")
    parser.add_argument("--load", type=str, metavar="SLOT", help="Load a specific save slot immediately")
    parser.add_argument("--clear", action="store_true", help="Clear terminal screen between turns")
    args = parser.parse_args()

    if args.load:
        w, s, msg = load_game(args.load)
        if not w or not s:
            console.print(f"[bold red]{msg}[/bold red]")
            sys.exit(1)
        run_game_loop(w, s, msg, clear_screen=args.clear)
    elif args.new:
        show_title_screen()
        w = World()
        s = GameState()
        run_game_loop(
            w,
            s,
            "[bold bright_cyan]✦ New expedition begun at Stratum -3 (The Bioluminescent Abyss).[/bold bright_cyan]",
            clear_screen=args.clear,
        )
    else:
        w, s, msg = interactive_startup_menu()
        run_game_loop(w, s, msg, clear_screen=args.clear)


if __name__ == "__main__":
    main()
