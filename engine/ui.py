"""Rich-powered Terminal UI and Fog-of-War 3D Mini-Map for Echoes of the Aethelgard Spire."""

from __future__ import annotations
import os
import sys
from typing import Dict, List, Optional, Set, Tuple
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.columns import Columns
from rich.align import Align
from rich import box

from engine.models import (
    GameState,
    Room,
    STRATUM_ELEVATIONS,
    STRATUM_NAMES,
    STRATUM_THEMES,
)
from engine.world_builder import World


# Ensure UTF-8 output on Windows consoles so Unicode map & box symbols render cleanly
if sys.platform == "win32":
    try:
        os.system("chcp 65001 > nul 2>&1")
    except Exception:
        pass
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass

console = Console(force_terminal=True, legacy_windows=False)


def compute_inventory_slots_used(world: World, state: GameState) -> int:
    return sum(world.items[i].slot_size for i in state.inventory if i in world.items)


def is_room_lit(world: World, state: GameState, room: Room) -> bool:
    if not room.dark:
        return True
    if "phosphor_lantern" in state.inventory or "phosphor_lantern" in room.items:
        return True
    return False


def render_minimap_text(
    world: World,
    state: GameState,
    target_z: Optional[int] = None,
    include_legend: bool = True,
) -> str:
    """
    Build a Fog-of-War 2D ASCII/Unicode grid for stratum `target_z`.
    Strictly displays ONLY rooms in `state.visited_rooms` (plus `[?]` for directly
    adjacent unvisited rooms reachable via visible exits from visited rooms).
    """
    current_room = world.rooms[state.current_room_id]
    z = current_room.stratum if target_z is None else target_z

    # Collect visited rooms on level z
    visited_on_z: Dict[Tuple[int, int], Room] = {}
    adjacent_unknown: Set[Tuple[int, int]] = set()
    edges_h: Dict[Tuple[int, int], str] = {}  # (min_x, y) -> "open" | "locked"
    edges_v: Dict[Tuple[int, int], str] = {}  # (x, min_y) -> "open" | "locked"

    for r_id in state.visited_rooms:
        room = world.rooms.get(r_id)
        if not room or room.stratum != z:
            continue
        rx, ry = room.coord.x, room.coord.y
        visited_on_z[(rx, ry)] = room

        # Check N/S/E/W exits from this visited room
        for d, ex in room.exits.items():
            if ex.hidden or d in ("up", "down"):
                continue
            target = world.rooms.get(ex.target_room_id)
            if not target or target.stratum != z:
                continue
            tx, ty = target.coord.x, target.coord.y
            if target.id not in state.visited_rooms:
                adjacent_unknown.add((tx, ty))
            edge_state = "locked" if ex.locked else "open"
            if d in ("east", "west"):
                key = (min(rx, tx), ry)
                if edges_h.get(key) != "open":
                    edges_h[key] = edge_state
            elif d in ("north", "south"):
                key = (rx, min(ry, ty))
                if edges_v.get(key) != "open":
                    edges_v[key] = edge_state

    if not visited_on_z:
        return f"[dim]No areas explored on Stratum {z:+d} yet.[/dim]"

    all_coords = set(visited_on_z.keys()) | adjacent_unknown
    min_x = min(x for x, _ in all_coords)
    max_x = max(x for x, _ in all_coords)
    min_y = min(y for _, y in all_coords)
    max_y = max(y for _, y in all_coords)

    note_rooms = {n.room_id for n in state.notes}

    lines: List[str] = []
    # Render top-to-bottom (max_y down to min_y)
    for y in range(max_y, min_y - 1, -1):
        row_cells: List[str] = []
        for x in range(min_x, max_x + 1):
            if (x, y) in visited_on_z:
                rm = visited_on_z[(x, y)]
                has_up = "up" in rm.exits and not rm.exits["up"].hidden
                has_down = "down" in rm.exits and not rm.exits["down"].hidden
                if rm.id == state.current_room_id and z == current_room.stratum:
                    node = "[bold bright_yellow]\\[★][/]"
                elif has_up and has_down:
                    node = "[bold cyan]\\[↕][/]"
                elif has_up:
                    node = "[bold green]\\[▲][/]"
                elif has_down:
                    node = "[bold magenta]\\[▼][/]"
                elif rm.id in note_rooms:
                    node = "[bold bright_white]\\[✎][/]"
                elif rm.items and is_room_lit(world, state, rm):
                    node = "[bold gold1]\\[♦][/]"
                else:
                    node = "[bold bright_cyan]\\[●][/]"
            elif (x, y) in adjacent_unknown:
                node = "[dim]\\[?][/]"
            else:
                node = "   "
            row_cells.append(node)

            # Horizontal connector to (x + 1, y)
            if x < max_x:
                h_state = edges_h.get((x, y))
                if h_state == "open":
                    row_cells.append("───")
                elif h_state == "locked":
                    row_cells.append("[bold red]─╫─[/bold red]")
                else:
                    row_cells.append("   ")
        lines.append(" " + "".join(row_cells))

        # Vertical connector row to (x, y - 1)
        if y > min_y:
            v_cells: List[str] = []
            for x in range(min_x, max_x + 1):
                v_state = edges_v.get((x, y - 1))
                if v_state == "open":
                    v_cells.append(" │ ")
                elif v_state == "locked":
                    v_cells.append("[bold red] ╫ [/bold red]")
                else:
                    v_cells.append("   ")
                if x < max_x:
                    v_cells.append("   ")
            lines.append(" " + "".join(v_cells))

    if include_legend:
        # Build compact elevation bar
        elev_pills = []
        for sz in range(3, -4, -1):
            explored_on_sz = any(world.rooms[r].stratum == sz for r in state.visited_rooms)
            lbl = f"+{sz}" if sz > 0 else str(sz)
            if sz == current_room.stratum:
                elev_pills.append(f"[bold reverse yellow] {lbl}★ [/bold reverse yellow]")
            elif explored_on_sz:
                elev_pills.append(f"[cyan]{lbl}●[/cyan]")
            else:
                elev_pills.append(f"[dim]{lbl}·[/dim]")

        lines.append("")
        lines.append("[dim]──────────────────────────────[/dim]")
        lines.append("Elev: " + " ".join(elev_pills))
        lines.append(
            "[bold bright_yellow]★[/bold bright_yellow] You  "
            "[bold bright_cyan]●[/bold bright_cyan] Visited  "
            "[bold gold1]♦[/bold gold1] Item  "
            "[dim]?[/dim] Unknown"
        )
        lines.append(
            "[bold green]▲[/bold green] Up   "
            "[bold magenta]▼[/bold magenta] Down     "
            "[bold red]╫[/bold red] Locked "
            "[bold bright_white]✎[/bold bright_white] Note"
        )

    return "\n".join(lines)


def render_dashboard(world: World, state: GameState, feedback_message: str = "") -> None:
    room = world.rooms[state.current_room_id]
    theme = STRATUM_THEMES.get(room.stratum, STRATUM_THEMES[0])
    lit = is_room_lit(world, state, room)

    slots_used = compute_inventory_slots_used(world, state)
    slots_bar = "█" * slots_used + "░" * max(0, state.max_inventory_slots - slots_used)
    mem_bar = "".join("◈" if i in state.memories_restored else "◇" for i in range(1, 8))

    # 1. Header Panel
    header_table = Table.grid(expand=True)
    header_table.add_column(justify="left", ratio=3)
    header_table.add_column(justify="right", ratio=2)

    stratum_title = STRATUM_NAMES.get(room.stratum, f"Stratum {room.stratum}")
    elev_str = STRATUM_ELEVATIONS.get(room.stratum, "0m")
    header_table.add_row(
        f"[{theme['title']}]❖ THE AETHELGARD SPIRE[/] │ [{theme['accent']}]{stratum_title}[/]",
        f"[bold white]Pos:[/] {room.coord} │ [bold white]Elev:[/] {elev_str}",
    )
    header_table.add_row(
        f"[bold white]Inventory:[/] [{theme['accent']}]\\[{slots_bar}][/] {slots_used}/{state.max_inventory_slots} Slots │ "
        f"[bold white]Memories:[/] [bright_cyan]{mem_bar}[/] ({len(state.memories_restored)}/7)",
        f"[bold white]Notes:[/] {len(state.notes)} │ [bold white]Explored:[/] {len(state.visited_rooms)}/{len(world.rooms)} │ [bold white]Turns:[/] {state.turn_count}",
    )
    header_panel = Panel(header_table, border_style=theme["border"], box=box.DOUBLE_EDGE, padding=(0, 1))

    # 2. Left Column: Room Narrative, Fixtures, Items, Exits, Action Feedback
    narrative_parts: List[str] = []
    narrative_parts.append(f"[{theme['title']}]{room.name.upper()}[/]  [dim italic]— {room.subtitle}[/]")
    narrative_parts.append(f"[{theme['dim']}]{'─' * 56}[/]")

    if not lit:
        narrative_parts.append(f"[bold red]{room.dark_description}[/]")
    else:
        desc = room.description
        for flag_name, extra_text in room.dynamic_flag_descriptions.items():
            if state.flags.get(flag_name):
                desc += extra_text
        narrative_parts.append(desc)

        # Interactive features
        if room.features:
            feat_tags = "  ".join(f"[bold {theme['accent']}]\\[{k}][/]" for k in room.features.keys())
            narrative_parts.append(f"\n[bold white]✦ Fixtures :[/] {feat_tags}")

        # Items in room
        if room.items:
            item_lines = []
            for item_id in room.items:
                it = world.items[item_id]
                slot_lbl = f"{it.slot_size} slot" if it.slot_size == 1 else f"{it.slot_size} slots"
                item_lines.append(f"  • [bold gold1]{it.name}[/] [dim]({slot_lbl}) — {it.short_desc}[/]")
            narrative_parts.append("[bold white]❖ Items Here:[/]\n" + "\n".join(item_lines))

    # Exits
    exit_badges = []
    for d, ex in room.exits.items():
        if ex.hidden:
            continue
        target_rm = world.rooms[ex.target_room_id]
        target_label = target_rm.name if target_rm.id in state.visited_rooms else "Unexplored"
        d_short = d.upper()
        if ex.locked:
            exit_badges.append(f"[bold red]\\[{d_short}: {target_label} (Locked)][/]")
        elif d in ("up", "down"):
            exit_badges.append(f"[bold bright_green]\\[{d_short} ↕ {target_label}][/]")
        else:
            exit_badges.append(f"[bold {theme['accent']}]\\[{d_short}][/] {target_label}")

    narrative_parts.append("\n[bold white]⇄ Exits     :[/] " + "   ".join(exit_badges))

    # Notes pinned in this room
    room_notes = [n for n in state.notes if n.room_id == room.id]
    if room_notes:
        narrative_parts.append(
            f"[bold bright_white]✎ Room Note :[/] [italic]\"{room_notes[-1].text}\"[/]"
        )

    if feedback_message:
        narrative_parts.append(f"\n[{theme['dim']}]{'═' * 56}[/]")
        narrative_parts.append(feedback_message)

    room_panel = Panel(
        "\n".join(narrative_parts),
        title=f"[{theme['title']}]Chamber View[/]",
        border_style=theme["border"],
        box=box.ROUNDED,
        padding=(0, 1),
    )

    # 3. Right Column: Fog-of-War Mini-Map + Quick Commands
    minimap_str = render_minimap_text(world, state, room.stratum, include_legend=True)
    map_panel = Panel(
        Align.center(minimap_str),
        title=f"[{theme['title']}]Fog-of-War Mini-Map (Z = {room.stratum:+d})[/]",
        subtitle="[dim]Type 'map' for full legend[/]",
        border_style=theme["border"],
        box=box.ROUNDED,
        padding=(0, 1),
    )

    # Combine side-by-side using a 2-column grid
    body_grid = Table.grid(expand=True)
    body_grid.add_column(ratio=7)
    body_grid.add_column(ratio=4)
    body_grid.add_row(room_panel, map_panel)

    footer_text = (
        "[dim]Commands:[/dim] [bold]n/s/e/w/u/d[/bold] Move │ [bold]x <obj>[/bold] Examine │ "
        "[bold]take/drop <item>[/bold] │ [bold]combine <a> with <b>[/bold] │ [bold]use <item> on <obj>[/bold] │ "
        "[bold]map \\[z][/bold] │ [bold]note add <txt>[/bold] │ [bold]inv[/bold] │ [bold]hint[/bold] │ [bold]save/load[/bold] │ [bold]help[/bold]"
    )
    footer_panel = Panel(footer_text, border_style="bright_black", box=box.ROUNDED, padding=(0, 1))

    console.print(header_panel)
    console.print(body_grid)
    console.print(footer_panel)


def render_full_map_modal(world: World, state: GameState, arg: str = "") -> str:
    """Return a rich detailed Fog-of-War map string for a stratum or vertical overview."""
    current_room = world.rooms[state.current_room_id]
    arg_clean = arg.strip().lower()

    if arg_clean in ("vertical", "all", "spire", "tower", "strata"):
        lines = ["[bold bright_white]═══ THE AETHELGARD SPIRE — VERTICAL CROSS-SECTION (FOG OF WAR) ═══[/bold bright_white]\n"]
        for z in range(3, -4, -1):
            total_z = sum(1 for r in world.rooms.values() if r.stratum == z)
            visited_z = [world.rooms[r_id] for r_id in state.visited_rooms if world.rooms[r_id].stratum == z]
            here = " [bold bright_yellow]◄ YOU ARE HERE[/bold bright_yellow]" if current_room.stratum == z else ""
            bar = "█" * len(visited_z) + "░" * (total_z - len(visited_z))
            if visited_z:
                s_name = STRATUM_NAMES[z]
                elev = STRATUM_ELEVATIONS[z]
                lines.append(f"[bold cyan]{s_name}[/bold cyan] ({elev}){here}")
                lines.append(f"  Explored: \\[{bar}] {len(visited_z)}/{total_z} chambers  |  Type `map {z}` to inspect grid")
            else:
                lines.append(f"[dim]Stratum {z:+d}: \\[░░░░░░░░░░░░] 0/{total_z} chambers (Unexplored)[/dim]")
            if z > -3:
                lines.append("        ║")
        return "\n".join(lines)

    target_z = current_room.stratum
    if arg_clean:
        try:
            parsed = int(arg_clean.replace("+", ""))
            if -3 <= parsed <= 3:
                target_z = parsed
            else:
                return "Specify a stratum between -3 and +3 (e.g., `map -3`, `map 0`, `map 2`, or `map vertical`)."
        except ValueError:
            return "Specify a stratum number between -3 and +3, or `map vertical`."

    grid = render_minimap_text(world, state, target_z, include_legend=True)
    visited_rooms_z = sorted(
        [world.rooms[r_id] for r_id in state.visited_rooms if world.rooms[r_id].stratum == target_z],
        key=lambda r: (-r.coord.y, r.coord.x),
    )

    lines = [
        f"[bold bright_white]═══ DETAILED FOG-OF-WAR MAP: {STRATUM_NAMES.get(target_z, f'Stratum {target_z}')} ═══[/bold bright_white]",
        grid,
        "\n[bold white]Explored Chambers on This Stratum:[/bold white]",
    ]
    if not visited_rooms_z:
        lines.append("  [dim]You have not yet discovered any chambers on this stratum.[/dim]")
    else:
        for rm in visited_rooms_z:
            marker = "★" if rm.id == state.current_room_id else "•"
            items_tag = ""
            if rm.items and is_room_lit(world, state, rm):
                item_names = ", ".join(world.items[i].name for i in rm.items)
                items_tag = f" [gold1]\\[Items: {item_names}][/gold1]"
            vert_tag = ""
            if "up" in rm.exits and not rm.exits["up"].hidden:
                vert_tag += " [green]\\[▲UP][/green]"
            if "down" in rm.exits and not rm.exits["down"].hidden:
                vert_tag += " [magenta]\\[▼DOWN][/magenta]"
            lines.append(f"  {marker} [bold]{rm.coord}[/bold] {rm.name}{vert_tag}{items_tag}")

    lines.append("\n[dim]Tip: Use `map <z>` (from -3 to +3) to inspect other strata, or `map vertical` for the Spire overview.[/dim]")
    return "\n".join(lines)
