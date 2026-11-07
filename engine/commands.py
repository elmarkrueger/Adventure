"""Command parser and execution engine for Echoes of the Aethelgard Spire."""

from __future__ import annotations
from typing import Optional, Tuple
from engine.models import GameState, Note, STRATUM_NAMES
from engine.world_builder import World
from engine.ui import (
    compute_inventory_slots_used,
    is_room_lit,
    render_full_map_modal,
)
from engine.puzzles import (
    get_contextual_hint,
    handle_activate_core,
    handle_play_or_strike,
    handle_set_or_dial,
    handle_turn_or_pull,
    handle_use_item,
)
from engine.save_system import list_saves, load_game, save_game


DIRECTION_ALIASES = {
    "n": "north",
    "north": "north",
    "s": "south",
    "south": "south",
    "e": "east",
    "east": "east",
    "w": "west",
    "west": "west",
    "u": "up",
    "up": "up",
    "ascend": "up",
    "climb": "up",
    "d": "down",
    "down": "down",
    "descend": "down",
}


class CommandResult:
    def __init__(
        self,
        message: str,
        should_quit: bool = False,
        new_world: Optional[World] = None,
        new_state: Optional[GameState] = None,
    ) -> None:
        self.message = message
        self.should_quit = should_quit
        self.new_world = new_world
        self.new_state = new_state


def process_command(world: World, state: GameState, raw_input: str) -> CommandResult:
    cleaned = raw_input.strip()
    if not cleaned:
        return CommandResult("Enter a command (or type `help` for a list of commands).")

    parts = cleaned.split(maxsplit=1)
    verb = parts[0].lower()
    arg = parts[1].strip() if len(parts) > 1 else ""

    # 1. Direct Direction Shorthand
    if verb in DIRECTION_ALIASES and not arg:
        return _handle_move(world, state, DIRECTION_ALIASES[verb])

    if verb in ("go", "move", "walk", "travel", "head", "enter", "climb", "ascend", "descend"):
        target_dir = DIRECTION_ALIASES.get(arg.lower()) or DIRECTION_ALIASES.get(verb)
        if target_dir:
            return _handle_move(world, state, target_dir)
        return CommandResult(f"Specify a valid direction (`north`, `south`, `east`, `west`, `up`, `down`).")

    # 2. Look / Examine / Read
    if verb in ("l", "look") and not arg:
        return CommandResult("You survey your surroundings carefully.")
    if verb in ("l", "look") and arg.lower().startswith("at "):
        return _handle_examine(world, state, arg[3:].strip())
    if verb in ("x", "examine", "inspect", "search", "check", "look"):
        return _handle_examine(world, state, arg)
    if verb in ("read", "study", "decipher"):
        return _handle_read(world, state, arg)

    # 3. Inventory: Take, Drop, Combine, Stash, Retrieve
    if verb in ("i", "inv", "inventory"):
        return _handle_inventory(world, state)
    if verb == "pick" and arg.lower().startswith("up "):
        return _handle_take(world, state, arg[3:].strip())
    if verb in ("take", "get", "grab", "collect", "acquire"):
        return _handle_take(world, state, arg)
    if verb in ("drop", "discard", "leave"):
        return _handle_drop(world, state, arg)
    if verb in ("combine", "craft", "mix", "merge", "attach", "join", "blend"):
        return _handle_combine(world, state, arg)
    if verb in ("stash", "deposit", "store"):
        return _handle_stash(world, state, arg)
    if verb in ("retrieve", "withdraw", "fetch"):
        return _handle_retrieve(world, state, arg)
    if verb == "locker":
        return _handle_locker_view(world, state)

    # 4. Puzzle & Fixture Interactions
    if verb in ("use", "apply", "insert", "place", "install", "equip", "wear", "pour"):
        if verb == "insert" and "cylinder" in arg.lower():
            return _handle_insert_cylinders(world, state, arg)
        return _handle_use(world, state, arg)
    if verb in ("unlock", "open", "unseal", "breach"):
        return _handle_unlock_or_open(world, state, arg)
    if verb in ("turn", "rotate", "spin", "pull", "push", "flip", "crank", "release", "haul"):
        return CommandResult(handle_turn_or_pull(world, state, arg or verb))
    if verb in ("set", "dial", "tune", "input", "align", "adjust"):
        return CommandResult(handle_set_or_dial(world, state, arg))
    if verb in ("play", "strike", "ring", "sound"):
        return CommandResult(handle_play_or_strike(world, state, arg))
    if verb == "activate" and ("core" in arg.lower() or "chorister" in arg.lower() or not arg):
        return CommandResult(handle_activate_core(world, state))

    # 5. Map, Notebook & Lore Journal
    if verb in ("m", "map", "minimap"):
        return CommandResult(render_full_map_modal(world, state, arg))
    if verb in ("note", "notes", "notebook"):
        return _handle_notes(world, state, verb, arg)
    if verb in ("journal", "lore", "memories", "cylinders"):
        return _handle_journal(world, state)

    # 6. Hints, Status, Save, Load, Help, Quit
    if verb in ("hint", "hints", "clue"):
        return CommandResult(get_contextual_hint(world, state))
    if verb in ("status", "score", "progress"):
        return _handle_status(world, state)
    if verb == "save":
        slot = arg if arg else "quicksave"
        _, msg, _ = save_game(world, state, slot)
        return CommandResult(f"[bold bright_green]💾 {msg}[/bold bright_green]")
    if verb == "load":
        slot = arg if arg else "quicksave"
        new_w, new_s, msg = load_game(slot)
        if new_w and new_s:
            return CommandResult(f"[bold bright_green]📂 {msg}[/bold bright_green]", new_world=new_w, new_state=new_s)
        return CommandResult(f"[bold red]{msg}[/bold red]")
    if verb == "saves":
        return _handle_list_saves()
    if verb in ("h", "help", "?"):
        return _handle_help(arg)
    if verb in ("q", "quit", "exit"):
        return CommandResult("Farewell, Architect Vaelen Korr.", should_quit=True)

    return CommandResult(
        f"Unrecognized command `{cleaned}`. Type `help` for available commands or `hint` for a contextual nudge."
    )


def _handle_move(world: World, state: GameState, direction: str) -> CommandResult:
    room = world.rooms[state.current_room_id]
    if direction not in room.exits or room.exits[direction].hidden:
        return CommandResult(f"You cannot go **{direction}** from here.")

    ex = room.exits[direction]
    if ex.locked:
        # Check if player can auto-unlock or if diving helmet lets them into Ossuary
        if ex.lock_id == "ossuary_flood_lock" and "diving_helmet" in state.inventory:
            ex.locked = False
        else:
            return CommandResult(f"[bold red]🔒 Locked ({direction.upper()}):[/bold red] {ex.lock_message}")

    old_stratum = room.stratum
    target_room = world.rooms[ex.target_room_id]
    state.current_room_id = target_room.id
    state.visited_rooms.add(target_room.id)
    state.turn_count += 1

    msg = f"You move **{direction}** to **{target_room.name}**."
    if target_room.stratum != old_stratum:
        save_game(world, state, "autosave")
        stratum_title = STRATUM_NAMES.get(target_room.stratum, f"Stratum {target_room.stratum}")
        msg += f"\n[bold bright_cyan]✦ Entered {stratum_title} — Progress automatically saved to 'autosave'.[/bold bright_cyan]"

    return CommandResult(msg)


def _handle_examine(world: World, state: GameState, query: str) -> CommandResult:
    room = world.rooms[state.current_room_id]
    if not query or query.lower() in ("room", "around", "chamber", "here"):
        return CommandResult("You take a closer look around the chamber.")

    if not is_room_lit(world, state, room):
        # Allow examining inventory items even in the dark
        inv_match = world.match_item_in_list(query, state.inventory)
        if inv_match:
            return _examine_item_obj(world, state, inv_match)
        return CommandResult("It is too dark to examine anything in the room! Light your Phosphor Lantern first.")

    # 1. Check inventory or room items
    item_id = world.match_item_in_list(query, state.inventory + room.items)
    if item_id:
        return _examine_item_obj(world, state, item_id)

    # 2. Check room features
    q_low = query.lower()
    for feat_key, feat_desc in room.features.items():
        if q_low in feat_key.lower() or feat_key.lower() in q_low:
            return CommandResult(f"[bold cyan]✦ \\[{feat_key}]:[/bold cyan] {feat_desc}")

    # 3. Check exits
    if q_low in DIRECTION_ALIASES:
        d = DIRECTION_ALIASES[q_low]
        if d in room.exits and not room.exits[d].hidden:
            ex = room.exits[d]
            status = " (Locked)" if ex.locked else ""
            return CommandResult(f"[bold]Exit {d.upper()}{status}:[/bold] {ex.description}")

    return CommandResult(f"You don't see '{query}' here to examine.")


def _examine_item_obj(world: World, state: GameState, item_id: str) -> CommandResult:
    item = world.items[item_id]
    if item.lore_id and item.lore_id not in state.unlocked_lore:
        state.unlocked_lore.append(item.lore_id)
    lines = [
        f"[bold gold1]❖ {item.name}[/bold gold1] [dim]({item.slot_size} slot{'s' if item.slot_size > 1 else ''}, {item.category})[/dim]",
        item.examine_text,
    ]
    if item.read_text:
        lines.append(f"\n[bold white]Inscribed Text:[/bold white]\n[italic]{item.read_text}[/italic]")
    if item_id == "wayfinder_compass":
        room = world.rooms[state.current_room_id]
        lines.append(f"\n[bold cyan]Wayfinder Reading:[/bold cyan] Current Stratum Z = {room.stratum:+d}, Coordinates {room.coord}.")
    return CommandResult("\n".join(lines))


def _handle_read(world: World, state: GameState, query: str) -> CommandResult:
    if not query:
        return CommandResult("Specify what you want to read (e.g., `read tablet`, `read ledger`, `read blueprint`).")
    room = world.rooms[state.current_room_id]
    item_id = world.match_item_in_list(query, state.inventory + (room.items if is_room_lit(world, state, room) else []))
    if item_id:
        item = world.items[item_id]
        if item.lore_id and item.lore_id not in state.unlocked_lore:
            state.unlocked_lore.append(item.lore_id)
        if item.read_text:
            return CommandResult(f"[bold gold1]📖 Reading {item.name}:[/bold gold1]\n{item.read_text}")
        return CommandResult(f"{item.name} has no text to read, though examining it reveals:\n{item.examine_text}")
    return _handle_examine(world, state, query)


def _handle_inventory(world: World, state: GameState) -> CommandResult:
    slots_used = compute_inventory_slots_used(world, state)
    lines = [
        f"[bold bright_white]═══ INVENTORY ({slots_used}/{state.max_inventory_slots} Slots Used) ═══[/bold bright_white]"
    ]
    if not state.inventory:
        lines.append("  [dim]Your pack is currently empty.[/dim]")
    else:
        for item_id in state.inventory:
            it = world.items[item_id]
            s_lbl = f"{it.slot_size} slot" if it.slot_size == 1 else f"{it.slot_size} slots"
            lines.append(f"  • [bold gold1]{it.name}[/bold gold1] (`{it.id}`) — [cyan]{s_lbl}[/cyan] — {it.short_desc}")
    if state.pneumatic_locker:
        locker_names = ", ".join(world.items[i].name for i in state.pneumatic_locker)
        lines.append(f"\n[bold cyan]Pneumatic Network Storage:[/bold cyan] {locker_names}")
    return CommandResult("\n".join(lines))


def _handle_take(world: World, state: GameState, query: str) -> CommandResult:
    room = world.rooms[state.current_room_id]
    if not is_room_lit(world, state, room):
        return CommandResult("It is pitch-dark! You cannot see anything to pick up without a light source.")
    if not query:
        return CommandResult("Specify what to take (e.g., `take lantern`, or `take all`).")

    if query.lower() == "all":
        if not room.items:
            return CommandResult("There are no portable items here to take.")
        taken_msgs = []
        for item_id in list(room.items):
            res = _take_single_item(world, state, room, item_id)
            taken_msgs.append(res)
        return CommandResult("\n".join(taken_msgs))

    item_id = world.match_item_in_list(query, room.items)
    if not item_id:
        if world.match_item_in_list(query, state.inventory):
            return CommandResult("You are already carrying that item.")
        return CommandResult(f"You don't see '{query}' here to take.")

    return CommandResult(_take_single_item(world, state, room, item_id))


def _take_single_item(world: World, state: GameState, room: Room, item_id: str) -> str:
    item = world.items[item_id]
    if not item.portable:
        return f"The {item.name} is fixed in place and cannot be carried."

    slots_used = compute_inventory_slots_used(world, state)
    if slots_used + item.slot_size > state.max_inventory_slots:
        return (
            f"[bold red]⚠ Inventory Full ({slots_used}/{state.max_inventory_slots} slots)![/bold red] "
            f"**{item.name}** requires {item.slot_size} slot(s). Use `drop <item>` to leave something here, "
            "`combine` items, or `stash <item>` at a Pneumatic Locker."
        )

    room.items.remove(item_id)
    state.inventory.append(item_id)
    state.turn_count += 1
    if item.lore_id and item.lore_id not in state.unlocked_lore:
        state.unlocked_lore.append(item.lore_id)

    new_used = compute_inventory_slots_used(world, state)
    return f"Taken: **[bold gold1]{item.name}[/bold gold1]** ({new_used}/{state.max_inventory_slots} slots used)."


def _handle_drop(world: World, state: GameState, query: str) -> CommandResult:
    if not query:
        return CommandResult("Specify which item from your inventory to drop (`drop <item>`).")
    item_id = world.match_item_in_list(query, state.inventory)
    if not item_id:
        return CommandResult(f"You aren't carrying '{query}'.")

    room = world.rooms[state.current_room_id]
    state.inventory.remove(item_id)
    room.items.append(item_id)
    state.turn_count += 1
    item = world.items[item_id]
    new_used = compute_inventory_slots_used(world, state)
    return CommandResult(
        f"You set down **[bold gold1]{item.name}[/bold gold1]** in {room.name} "
        f"({new_used}/{state.max_inventory_slots} slots used)."
    )


def _handle_combine(world: World, state: GameState, arg: str) -> CommandResult:
    # Split on "with", "and", "+", ","
    lower = arg.lower()
    part_a, part_b = "", ""
    for sep in (" with ", " and ", " + ", " into ", " onto ", " to ", ","):
        if sep in lower:
            idx = lower.index(sep)
            part_a = arg[:idx].strip()
            part_b = arg[idx + len(sep) :].strip()
            break
    if not part_a or not part_b:
        tokens = arg.split()
        if len(tokens) == 2:
            part_a, part_b = tokens[0], tokens[1]
        else:
            return CommandResult("Use the syntax: `combine <item1> with <item2>`.")

    room = world.rooms[state.current_room_id]
    available = state.inventory + (room.items if is_room_lit(world, state, room) else [])
    id_a = world.match_item_in_list(part_a, available)
    id_b = world.match_item_in_list(part_b, available)

    if not id_a:
        return CommandResult(f"You don't have '{part_a}' to combine.")
    if not id_b:
        return CommandResult(f"You don't have '{part_b}' to combine.")
    if id_a == id_b:
        return CommandResult("You must combine two distinct items.")

    for recipe in world.recipes:
        pair_match = (recipe.ingredient_a == id_a and recipe.ingredient_b == id_b) or (
            recipe.ingredient_a == id_b and recipe.ingredient_b == id_a
        )
        if pair_match:
            if recipe.station_feature and recipe.station_feature not in room.features:
                return CommandResult(
                    f"Combining {world.items[id_a].name} and {world.items[id_b].name} requires "
                    f"being at a `{recipe.station_feature}`!"
                )
            # Remove consumed ingredients from inventory or room
            for ing_id, consume in ((recipe.ingredient_a, recipe.consume_a), (recipe.ingredient_b, recipe.consume_b)):
                if consume:
                    if ing_id in state.inventory:
                        state.inventory.remove(ing_id)
                    elif ing_id in room.items:
                        room.items.remove(ing_id)

            res_id = recipe.result_item_id
            if res_id not in state.inventory:
                state.inventory.append(res_id)
            if recipe.bonus_item_id and recipe.bonus_item_id not in state.inventory:
                state.inventory.append(recipe.bonus_item_id)

            res_item = world.items[res_id]
            if res_item.lore_id and res_item.lore_id not in state.unlocked_lore:
                state.unlocked_lore.append(res_item.lore_id)

            state.turn_count += 1
            return CommandResult(
                f"[bold bright_green]⚒ CRAFTED: {res_item.name}![/bold bright_green]\n{recipe.success_message}"
            )

    return CommandResult(
        f"Combining **{world.items[id_a].name}** with **{world.items[id_b].name}** doesn't produce anything useful."
    )


def _handle_stash(world: World, state: GameState, query: str) -> CommandResult:
    room = world.rooms[state.current_room_id]
    if "locker" not in room.features:
        return CommandResult("There is no Pneumatic Dispatch Locker in this chamber.")
    item_id = world.match_item_in_list(query, state.inventory)
    if not item_id:
        return CommandResult(f"You aren't carrying '{query}' to stash.")
    state.inventory.remove(item_id)
    state.pneumatic_locker.append(item_id)
    return CommandResult(
        f"You place **{world.items[item_id].name}** into the Pneumatic Carrier Tube. "
        "You can retrieve it at any Pneumatic Locker across the Spire (`retrieve <item>`)."
    )


def _handle_retrieve(world: World, state: GameState, query: str) -> CommandResult:
    room = world.rooms[state.current_room_id]
    if "locker" not in room.features:
        return CommandResult("There is no Pneumatic Dispatch Locker in this chamber.")
    if not state.pneumatic_locker:
        return CommandResult("The Pneumatic Locker network is currently empty.")
    item_id = world.match_item_in_list(query, state.pneumatic_locker)
    if not item_id:
        return CommandResult(f"'{query}' is not in the Pneumatic Locker.")
    item = world.items[item_id]
    slots_used = compute_inventory_slots_used(world, state)
    if slots_used + item.slot_size > state.max_inventory_slots:
        return CommandResult(
            f"[bold red]Inventory Full ({slots_used}/{state.max_inventory_slots} slots)![/bold red] "
            f"Drop or stash something before retrieving {item.name}."
        )
    state.pneumatic_locker.remove(item_id)
    state.inventory.append(item_id)
    return CommandResult(f"Retrieved **{item.name}** from the Pneumatic Locker.")


def _handle_locker_view(world: World, state: GameState) -> CommandResult:
    if not state.pneumatic_locker:
        return CommandResult("The Pneumatic Dispatch Locker is currently empty. Use `stash <item>` at any hub.")
    items_str = "\n".join(f"  • [bold gold1]{world.items[i].name}[/bold gold1]" for i in state.pneumatic_locker)
    return CommandResult(f"[bold cyan]═══ PNEUMATIC LOCKER CONTENTS ═══[/bold cyan]\n{items_str}")


def _handle_use(world: World, state: GameState, arg: str) -> CommandResult:
    if not arg:
        return CommandResult("Specify what to use (e.g., `use satchel`, `use grappling_hook on shaft`).")

    # Check if user wrote "use <item1> with <item2>" -> delegate to combine
    if " with " in arg.lower():
        return _handle_combine(world, state, arg)

    item_part = arg
    target_part = None
    for sep in (" on ", " in ", " into ", " at ", " against ", " to "):
        if sep in arg.lower():
            idx = arg.lower().index(sep)
            item_part = arg[:idx].strip()
            target_part = arg[idx + len(sep) :].strip()
            break

    room = world.rooms[state.current_room_id]
    item_id = world.match_item_in_list(item_part, state.inventory)
    if not item_id:
        # Check if user is trying to "use winch" or "use brake" directly on a room fixture
        for fk in room.features:
            if item_part.lower() in fk.lower() or fk.lower() in item_part.lower():
                return CommandResult(handle_turn_or_pull(world, state, item_part))
        return CommandResult(f"You aren't carrying '{item_part}'.")

    state.turn_count += 1
    return CommandResult(handle_use_item(world, state, item_id, target_part))


def _handle_insert_cylinders(world: World, state: GameState, arg: str) -> CommandResult:
    room = world.rooms[state.current_room_id]
    if room.id != "p3_resonance_crown":
        return CommandResult("You can only insert all Mnemonic Cylinders at The Resonance Crown (Apex) on Stratum +3.")
    inserted = state.flags.get("p3_cylinders_inserted", [])
    count = 0
    for item_id in list(state.inventory):
        if world.items[item_id].category == "memory":
            if item_id not in inserted:
                inserted.append(item_id)
                cyl_num = world.lore[world.items[item_id].memory_id].cylinder_number
                if cyl_num not in state.memories_restored:
                    state.memories_restored.append(cyl_num)
            state.inventory.remove(item_id)
            count += 1
    state.flags["p3_cylinders_inserted"] = inserted
    if count == 0 and not inserted:
        return CommandResult("You are not carrying any Mnemonic Cylinders in your inventory.")
    return CommandResult(
        f"[bold bright_white]✦ Seated {count} cylinder(s) into the Chorister's Core Drum "
        f"(Total loaded/restored: {len(set(inserted) | {f'cylinder_{m}' for m in state.memories_restored})}/7). "
        "Now type `activate core` to resolve the Spire's fate![/bold bright_white]"
    )


def _handle_unlock_or_open(world: World, state: GameState, arg: str) -> CommandResult:
    room = world.rooms[state.current_room_id]
    lower = arg.lower()
    if "shutter" in lower and room.id == "z0_sun_shaft_balcony":
        return CommandResult(handle_turn_or_pull(world, state, "shutter"))
    if "valve" in lower:
        return CommandResult(handle_turn_or_pull(world, state, lower))
    if " with " in lower:
        idx = lower.index(" with ")
        target_part = arg[:idx].strip()
        item_part = arg[idx + 6 :].strip()
        item_id = world.match_item_in_list(item_part, state.inventory)
        if not item_id:
            return CommandResult(f"You don't have '{item_part}' in your inventory.")
        return CommandResult(handle_use_item(world, state, item_id, target_part))

    # Otherwise try any key/tool in inventory that unlocks an exit in this room
    for d, ex in room.exits.items():
        if ex.locked and ex.unlock_item_id and ex.unlock_item_id in state.inventory:
            return CommandResult(handle_use_item(world, state, ex.unlock_item_id, d))

    return CommandResult(f"Specify what to unlock and with which tool (`use <item> on <direction/target>`).")


def _handle_notes(world: World, state: GameState, verb: str, arg: str) -> CommandResult:
    room = world.rooms[state.current_room_id]
    if verb in ("notes", "notebook"):
        return _list_notes(state, arg)
    if not arg or arg.lower() == "list":
        return _list_notes(state, "")

    parts = arg.split(maxsplit=1)
    sub = parts[0].lower()
    rest = parts[1].strip() if len(parts) > 1 else ""

    if sub in ("add", "new", "write"):
        if not rest:
            return CommandResult("Usage: `note add <your note text>`")
        return _add_note(state, room, "general", rest)

    if sub == "tag":
        tag_parts = rest.split(maxsplit=1)
        if len(tag_parts) < 2:
            return CommandResult("Usage: `note tag <tag_name> <your note text>`")
        return _add_note(state, room, tag_parts[0].lower(), tag_parts[1])

    if sub in ("del", "delete", "remove", "rm"):
        if not rest.isdigit():
            return CommandResult("Usage: `note del <note_id>` (e.g., `note del 1`).")
        target_id = int(rest)
        for n in state.notes:
            if n.id == target_id:
                state.notes.remove(n)
                return CommandResult(f"Deleted Note #{target_id}.")
        return CommandResult(f"No note found with ID #{target_id}.")

    if sub in ("list", "search", "find", "filter"):
        return _list_notes(state, rest)

    # Shorthand: `note <text>` adds a note directly!
    return _add_note(state, room, "general", arg)


def _add_note(state: GameState, room, tag: str, text: str) -> CommandResult:
    note = Note(
        id=state.next_note_id,
        text=text,
        tag=tag,
        room_id=room.id,
        room_name=room.name,
        coord=room.coord.to_tuple(),
        created_turn=state.turn_count,
    )
    state.notes.append(note)
    state.next_note_id += 1
    return CommandResult(
        f"[bold bright_white]✎ Note #{note.id} Recorded[/bold bright_white] at {room.name} {room.coord} "
        f"[cyan]\\[#{tag}][/cyan]: \"{text}\""
    )


def _list_notes(state: GameState, filter_q: str) -> CommandResult:
    if not state.notes:
        return CommandResult(
            "Your Field Notebook is empty. Add a note anytime with `note add <text>` or `note tag <tag> <text>`."
        )
    q = filter_q.strip().lower()
    filtered = [
        n
        for n in state.notes
        if not q
        or q in n.text.lower()
        or q in n.tag.lower()
        or q in n.room_name.lower()
    ]
    lines = ["[bold bright_white]═══ ARCHITECT'S FIELD NOTEBOOK ═══[/bold bright_white]"]
    if not filtered:
        lines.append(f"  [dim]No notes matching '{filter_q}'.[/dim]")
    else:
        for n in filtered:
            c_str = f"({n.coord[0]}, {n.coord[1]}, {n.coord[2]:+d})"
            lines.append(
                f"  [bold yellow]#{n.id}[/bold yellow] [cyan]\\[{n.tag}][/cyan] "
                f"[bold]{n.room_name}[/bold] {c_str} (Turn {n.created_turn}):\n"
                f"     \"{n.text}\""
            )
    return CommandResult("\n".join(lines))


def _handle_journal(world: World, state: GameState) -> CommandResult:
    lines = [
        f"[bold bright_cyan]═══ RESTORED MEMORIES & LORE JOURNAL ({len(state.memories_restored)}/7 Cylinders) ═══[/bold bright_cyan]"
    ]
    if not state.unlocked_lore:
        lines.append(
            "  [dim]You have not yet read any lore tablets or played any Mnemonic Cylinders.[/dim]"
        )
    else:
        for lore_id in state.unlocked_lore:
            entry = world.lore.get(lore_id)
            if not entry:
                continue
            badge = "◈ MEMORY CYLINDER" if entry.is_memory_cylinder else "📜 LORE DOCUMENT"
            lines.append(f"\n[bold gold1]{badge}: {entry.title}[/bold gold1] [dim](Stratum {entry.stratum:+d})[/dim]")
            lines.append(entry.text)
    return CommandResult("\n".join(lines))


def _handle_status(world: World, state: GameState) -> CommandResult:
    slots_used = compute_inventory_slots_used(world, state)
    return CommandResult(
        "[bold bright_white]═══ EXPEDITION STATUS ═══[/bold bright_white]\n"
        f"  • Chambers Explored : {len(state.visited_rooms)} / {len(world.rooms)} across 7 Strata\n"
        f"  • Memories Restored : {len(state.memories_restored)} / 7 Cylinders\n"
        f"  • Puzzles Solved    : {state.puzzle_Solved_count}\n"
        f"  • Inventory Slots   : {slots_used} / {state.max_inventory_slots}\n"
        f"  • Field Notes Taken : {len(state.notes)}\n"
        f"  • Solar Core Status : {'AWAKENED' if state.flags.get('n3_solar_core_awakened') else 'DORMANT'}\n"
        f"  • Turns Elapsed     : {state.turn_count}"
    )


def _handle_list_saves() -> CommandResult:
    saves = list_saves()
    if not saves:
        return CommandResult("No save files found yet. Use `save <slot_name>` to save your game.")
    lines = ["[bold bright_white]═══ SAVED GAMES ═══[/bold bright_white]"]
    for s in saves:
        lines.append(
            f"  • [bold bright_green]{s.get('slot')}[/bold bright_green] — "
            f"{s.get('room_name')} ({s.get('stratum_name')}) | "
            f"Memories: {s.get('memories_restored', 0)}/7 | "
            f"Explored: {s.get('visited_count', 1)}/88 | "
            f"Saved: {s.get('saved_at')}"
        )
    lines.append("\n[dim]Type `load <slot>` to resume from any save.[/dim]")
    return CommandResult("\n".join(lines))


def _handle_help(topic: str = "") -> CommandResult:
    return CommandResult(
        "[bold bright_white]═══ COMMAND REFERENCE: ECHOES OF THE AETHELGARD SPIRE ═══[/bold bright_white]\n"
        "  [bold cyan]Navigation[/bold cyan]  : `n`, `s`, `e`, `w`, `u` (`up`), `d` (`down`)\n"
        "  [bold cyan]Exploration[/bold cyan] : `look` (`l`), `examine <target>` (`x`), `read <item>`\n"
        "  [bold cyan]Inventory[/bold cyan]   : `inventory` (`i`), `take <item>`, `drop <item>`, `stash <item>`, `retrieve <item>`\n"
        "  [bold cyan]Crafting[/bold cyan]    : `combine <item1> with <item2>` (or `craft <a > with <b>`)\n"
        "  [bold cyan]Puzzles[/bold cyan]     : `use <item> on <target>`, `turn <valve>`, `pull <lever>`,\n"
        "                `set <target> <value>`, `dial <code>`, `play <cylinder/notes>`\n"
        "  [bold cyan]Mini-Map[/bold cyan]    : `map` (current level), `map <z>` (-3 to +3), `map vertical`\n"
        "  [bold cyan]Notebook[/bold cyan]    : `note add <text>`, `note tag <tag> <text>`, `notes`, `note del <id>`\n"
        "  [bold cyan]Journal[/bold cyan]     : `journal` (view all restored Memory Cylinders & Lore)\n"
        "  [bold cyan]System[/bold cyan]      : `hint`, `status`, `save [slot]`, `load [slot]`, `saves`, `quit`"
    )
