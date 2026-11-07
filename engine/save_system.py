"""Save and Load system for Echoes of the Aethelgard Spire."""

from __future__ import annotations
import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from engine.models import GameState, STRATUM_NAMES
from engine.world_builder import World


DEFAULT_SAVE_DIR = Path(__file__).resolve().parent.parent / "saves"


def sanitize_slot_name(slot: str) -> str:
    cleaned = "".join(c if (c.isalnum() or c in ("_", "-")) else "_" for c in slot.strip())
    return cleaned.lower() or "quicksave"


def save_game(
    world: World,
    state: GameState,
    slot_name: str = "quicksave",
    save_dir: Path = DEFAULT_SAVE_DIR,
) -> Tuple[bool, str, Path]:
    save_dir.mkdir(parents=True, exist_ok=True)
    slot = sanitize_slot_name(slot_name)
    file_path = save_dir / f"{slot}.json"

    room = world.rooms[state.current_room_id]
    state_dict = state.to_dict(world.rooms)
    payload_str = json.dumps(state_dict, sort_keys=True)
    checksum = hashlib.sha256(payload_str.encode("utf-8")).hexdigest()[:16]

    envelope = {
        "meta": {
            "slot": slot,
            "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "room_name": room.name,
            "stratum": room.stratum,
            "stratum_name": STRATUM_NAMES.get(room.stratum, f"Stratum {room.stratum}"),
            "turn_count": state.turn_count,
            "memories_restored": len(state.memories_restored),
            "visited_count": len(state.visited_rooms),
            "checksum": checksum,
        },
        "state": state_dict,
    }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(envelope, f, indent=2)

    return True, f"Progress saved to slot **'{slot}'** ({file_path.name}).", file_path


def load_game(
    slot_name: str = "quicksave",
    save_dir: Path = DEFAULT_SAVE_DIR,
) -> Tuple[Optional[World], Optional[GameState], str]:
    slot = sanitize_slot_name(slot_name)
    file_path = save_dir / f"{slot}.json"
    if not file_path.exists():
        return None, None, f"Save slot '{slot}' not found in {save_dir}."

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            envelope = json.load(f)
        state_data = envelope["state"]
        fresh_world = World()
        restored_state = GameState.from_dict(state_data, fresh_world.rooms)
        meta = envelope.get("meta", {})
        saved_at = meta.get("saved_at", "unknown time")
        return (
            fresh_world,
            restored_state,
            f"Loaded save slot **'{slot}'** (saved {saved_at} at {meta.get('room_name', 'Unknown')}).",
        )
    except Exception as exc:
        return None, None, f"Failed to load save slot '{slot}': {exc}"


def list_saves(save_dir: Path = DEFAULT_SAVE_DIR) -> List[Dict[str, Any]]:
    if not save_dir.exists():
        return []
    saves: List[Dict[str, Any]] = []
    for path in sorted(save_dir.glob("*.json"), key=os.path.getmtime, reverse=True):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            meta = data.get("meta", {})
            meta["slot"] = meta.get("slot", path.stem)
            saves.append(meta)
        except Exception:
            continue
    return saves
