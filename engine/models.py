"""Core data models and serializable state for Echoes of the Aethelgard Spire."""

from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional, Set, Tuple


DIRECTION_DELTAS: Dict[str, Tuple[int, int, int]] = {
    "north": (0, 1, 0),
    "south": (0, -1, 0),
    "east": (1, 0, 0),
    "west": (-1, 0, 0),
    "up": (0, 0, 1),
    "down": (0, 0, -1),
}

OPPOSITE_DIRECTIONS: Dict[str, str] = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
    "up": "down",
    "down": "up",
}

STRATUM_NAMES: Dict[int, str] = {
    -3: "Stratum -3: The Bioluminescent Abyss",
    -2: "Stratum -2: The Geothermal Foundry",
    -1: "Stratum -1: The Sunken Aqueducts & Labs",
    0: "Stratum  0: The Grand Clockwork Atrium",
    1: "Stratum +1: The Mnemonic Archives",
    2: "Stratum +2: The Aetherial Botanical Domes",
    3: "Stratum +3: The Celestial Observatory & Crown",
}

STRATUM_ELEVATIONS: Dict[int, str] = {
    -3: "-420m (Sub-Basal Chasm)",
    -2: "-280m (Magma Vent Line)",
    -1: "-130m (Subterranean Reservoir)",
    0: "   0m (Datum Horizon)",
    1: "+140m (Lower Spire Cloudline)",
    2: "+310m (Sunlit Canopy)",
    3: "+500m (Zenith Apex)",
}

STRATUM_THEMES: Dict[int, Dict[str, str]] = {
    -3: {"border": "bright_cyan", "title": "bold cyan", "accent": "turquoise2", "dim": "teal"},
    -2: {"border": "dark_orange", "title": "bold orange1", "accent": "gold1", "dim": "indian_red"},
    -1: {"border": "deep_sky_blue1", "title": "bold dodger_blue1", "accent": "aquamarine1", "dim": "steel_blue"},
    0: {"border": "gold3", "title": "bold yellow", "accent": "wheat1", "dim": "dark_goldenrod"},
    1: {"border": "medium_purple1", "title": "bold orchid1", "accent": "plum1", "dim": "medium_purple3"},
    2: {"border": "spring_green2", "title": "bold bright_green", "accent": "khaki1", "dim": "sea_green3"},
    3: {"border": "royal_blue1", "title": "bold bright_white", "accent": "sky_blue1", "dim": "slate_blue1"},
}


@dataclass(frozen=True)
class Coord3D:
    x: int
    y: int
    z: int

    def to_tuple(self) -> Tuple[int, int, int]:
        return (self.x, self.y, self.z)

    def __str__(self) -> str:
        z_str = f"+{self.z}" if self.z > 0 else str(self.z)
        return f"({self.x}, {self.y}, {z_str})"


@dataclass
class Exit:
    direction: str
    target_room_id: str
    description: str = ""
    locked: bool = False
    lock_id: Optional[str] = None
    unlock_item_id: Optional[str] = None
    lock_message: str = "The way is securely locked."
    unlock_message: str = "With a heavy metallic click, the lock disengages."
    hidden: bool = False
    consume_key: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Exit":
        return cls(**data)


@dataclass
class Item:
    id: str
    name: str
    aliases: List[str]
    short_desc: str
    examine_text: str
    slot_size: int = 1
    portable: bool = True
    category: str = "tool"  # tool, component, key, lore, memory, upgrade
    read_text: Optional[str] = None
    lore_id: Optional[str] = None
    memory_id: Optional[str] = None
    usable_targets: List[str] = field(default_factory=list)
    use_hint: Optional[str] = None


@dataclass
class Recipe:
    id: str
    ingredient_a: str
    ingredient_b: str
    result_item_id: str
    success_message: str
    station_feature: Optional[str] = None  # If set, must be in a room with this feature
    consume_a: bool = True
    consume_b: bool = True
    bonus_item_id: Optional[str] = None


@dataclass
class LoreEntry:
    id: str
    title: str
    stratum: int
    author: str
    text: str
    is_memory_cylinder: bool = False
    cylinder_number: Optional[int] = None


@dataclass
class Note:
    id: int
    text: str
    tag: str
    room_id: str
    room_name: str
    coord: Tuple[int, int, int]
    created_turn: int

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "text": self.text,
            "tag": self.tag,
            "room_id": self.room_id,
            "room_name": self.room_name,
            "coord": list(self.coord),
            "created_turn": self.created_turn,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Note":
        return cls(
            id=data["id"],
            text=data["text"],
            tag=data.get("tag", "general"),
            room_id=data["room_id"],
            room_name=data["room_name"],
            coord=tuple(data["coord"]),
            created_turn=data["created_turn"],
        )


@dataclass
class Room:
    id: str
    name: str
    coord: Coord3D
    stratum: int
    subtitle: str
    description: str
    exits: Dict[str, Exit] = field(default_factory=dict)
    items: List[str] = field(default_factory=list)
    features: Dict[str, str] = field(default_factory=dict)
    dark: bool = False
    dark_description: str = (
        "Pitch-black darkness swallows this chamber. You can hear distant drips and "
        "mechanical echoes, but without a steady light source it is too dangerous to "
        "search or navigate deeper."
    )
    ambient_hint: str = ""
    dynamic_flag_descriptions: Dict[str, str] = field(default_factory=dict)


@dataclass
class GameState:
    current_room_id: str = "n3_awakening_slab"
    inventory: List[str] = field(default_factory=list)
    max_inventory_slots: int = 8
    visited_rooms: Set[str] = field(default_factory=lambda: {"n3_awakening_slab"})
    pneumatic_locker: List[str] = field(default_factory=list)
    notes: List[Note] = field(default_factory=list)
    next_note_id: int = 1
    unlocked_lore: List[str] = field(default_factory=list)
    memories_restored: List[int] = field(default_factory=list)
    turn_count: int = 0
    puzzle_Solved_count: int = 0
    game_won: bool = False
    ending_type: Optional[str] = None
    last_message: str = ""
    flags: Dict[str, Any] = field(default_factory=lambda: {
        # Stratum -3 flags
        "n3_ossuary_drained": False,
        "n3_sluice_valve_a": False,
        "n3_sluice_valve_b": False,
        "n3_sluice_valve_c": False,
        "n3_grapnel_hooked": False,
        "n3_counterweight_dropped": False,
        "n3_solar_core_awakened": False,
        "n3_bell_pressurized": False,
        # Stratum -2 flags
        "n2_valve_alpha": 0,      # target: 40
        "n2_valve_beta": 0,       # target: 35 -> sum 75 for press, +45 gamma = 120 for lift
        "n2_valve_gamma": 0,
        "n2_steam_press_online": False,
        "n2_atrium_lift_powered": False,
        "n2_crucible_heated": False,
        "n2_counterweight_released": False,
        "n2_slag_bridge_cooled": False,
        "n2_tram_repaired": False,
        # Stratum -1 flags
        "n1_canal_water_level": "low",  # low, mid, high
        "n1_waterwheel_engaged": False,
        "n1_alembic_temp": "off",       # off, low, medium, high
        "n1_gold_seal_dissolved": False,
        "n1_whisper_angle": "north",    # north, east, west, focus
        "n1_crypt_gate_open": False,
        "n1_filtration_purged": False,
        # Stratum 0 flags
        "z0_pendulum_running": False,
        "z0_gear_installed": False,
        "z0_brake_released": False,
        "z0_chrono_dial": "0000",       # target: "4719"
        "z0_pneumatic_online": False,
        "z0_chime_sequence": [],        # target: ["sol", "mi", "do", "la"]
        "z0_weights_balanced": False,
        "z0_shutter_open": False,
        "z0_west_bridge_extended": False,
        # Stratum +1 flags
        "p1_cipher_wheel": "AAAA",      # target: "MNEMOS"
        "p1_uv_lamp_powered": False,
        "p1_blueprint_revealed": False,
        "p1_loom_tuned": False,
        "p1_secret_index_open": False,
        "p1_paternoster_fused": False,
        # Stratum +2 flags
        "p2_mirror_north": "east",     # target: "center"
        "p2_mirror_south": "west",     # target: "center"
        "p2_prism_installed": False,
        "p2_solar_beam_active": False,
        "p2_wind_organ_chord": "",      # target: "CEGB"
        "p2_bees_calmed": False,
        "p2_elevator_powered": False,
        "p2_orchid_pollinated": False,
        # Stratum +3 flags
        "p3_astrolabe_azimuth": 0,      # target: 240
        "p3_astrolabe_altitude": 0,     # target: 65
        "p3_astrolabe_aligned": False,
        "p3_west_pylon_freq": 0,        # target: 432
        "p3_east_pylon_freq": 0,        # target: 528
        "p3_pylons_synced": False,
        "p3_lightning_captured": False,
        "p3_core_unlocked": False,
        "p3_cylinders_inserted": [],
    })

    def to_dict(self, rooms: Dict[str, Room]) -> Dict[str, Any]:
        room_states = {}
        for r_id, room in rooms.items():
            room_states[r_id] = {
                "items": list(room.items),
                "exits": {
                    d: {
                        "locked": ex.locked,
                        "hidden": ex.hidden,
                    }
                    for d, ex in room.exits.items()
                },
            }
        return {
            "current_room_id": self.current_room_id,
            "inventory": list(self.inventory),
            "max_inventory_slots": self.max_inventory_slots,
            "visited_rooms": sorted(list(self.visited_rooms)),
            "pneumatic_locker": list(self.pneumatic_locker),
            "notes": [n.to_dict() for n in self.notes],
            "next_note_id": self.next_note_id,
            "unlocked_lore": list(self.unlocked_lore),
            "memories_restored": list(self.memories_restored),
            "turn_count": self.turn_count,
            "puzzle_Solved_count": self.puzzle_Solved_count,
            "game_won": self.game_won,
            "ending_type": self.ending_type,
            "last_message": self.last_message,
            "flags": self.flags,
            "room_states": room_states,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any], rooms: Dict[str, Room]) -> "GameState":
        state = cls(
            current_room_id=data["current_room_id"],
            inventory=list(data.get("inventory", [])),
            max_inventory_slots=data.get("max_inventory_slots", 8),
            visited_rooms=set(data.get("visited_rooms", [])),
            pneumatic_locker=list(data.get("pneumatic_locker", [])),
            notes=[Note.from_dict(n) for n in data.get("notes", [])],
            next_note_id=data.get("next_note_id", 1),
            unlocked_lore=list(data.get("unlocked_lore", [])),
            memories_restored=list(data.get("memories_restored", [])),
            turn_count=data.get("turn_count", 0),
            puzzle_Solved_count=data.get("puzzle_Solved_count", 0),
            game_won=data.get("game_won", False),
            ending_type=data.get("ending_type"),
            last_message=data.get("last_message", ""),
        )
        state.flags.update(data.get("flags", {}))

        room_states = data.get("room_states", {})
        for r_id, r_state in room_states.items():
            if r_id in rooms:
                rooms[r_id].items = list(r_state.get("items", []))
                for d, ex_state in r_state.get("exits", {}).items():
                    if d in rooms[r_id].exits:
                        rooms[r_id].exits[d].locked = ex_state.get("locked", False)
                        rooms[r_id].exits[d].hidden = ex_state.get("hidden", False)
        return state
