"""World builder and validator for Echoes of the Aethelgard Spire."""

from typing import Dict, List, Optional, Tuple
from engine.models import Coord3D, Item, LoreEntry, Recipe, Room, DIRECTION_DELTAS
from data.items_and_recipes import get_items, get_lore_entries, get_recipes
from data import (
    stratum_n3_abyss,
    stratum_n2_geothermal,
    stratum_n1_aqueducts,
    stratum_0_sanctum,
    stratum_p1_archives,
    stratum_p2_arboretum,
    stratum_p3_observatory,
)


class World:
    def __init__(self) -> None:
        self.items: Dict[str, Item] = get_items()
        self.recipes: List[Recipe] = get_recipes()
        self.lore: Dict[str, LoreEntry] = get_lore_entries()
        self.rooms: Dict[str, Room] = {}
        self.coord_to_room_id: Dict[Tuple[int, int, int], str] = {}
        self._load_all_strata()

    def _load_all_strata(self) -> None:
        modules = [
            stratum_n3_abyss,
            stratum_n2_geothermal,
            stratum_n1_aqueducts,
            stratum_0_sanctum,
            stratum_p1_archives,
            stratum_p2_arboretum,
            stratum_p3_observatory,
        ]
        for mod in modules:
            stratum_rooms = mod.get_rooms()
            for r_id, room in stratum_rooms.items():
                if r_id in self.rooms:
                    raise ValueError(f"Duplicate room ID: {r_id}")
                coord_tuple = room.coord.to_tuple()
                if coord_tuple in self.coord_to_room_id:
                    existing = self.coord_to_room_id[coord_tuple]
                    raise ValueError(f"Coordinate collision at {coord_tuple}: {r_id} vs {existing}")
                self.rooms[r_id] = room
                self.coord_to_room_id[coord_tuple] = r_id

    def validate_graph(self) -> List[str]:
        """Validate room exits, coordinate steps, and item references."""
        errors: List[str] = []
        for r_id, room in self.rooms.items():
            for item_id in room.items:
                if item_id not in self.items:
                    errors.append(f"Room {r_id} references unknown item {item_id}")
            for direction, ex in room.exits.items():
                if direction not in DIRECTION_DELTAS:
                    errors.append(f"Room {r_id} has invalid direction {direction}")
                if ex.target_room_id not in self.rooms:
                    errors.append(f"Room {r_id} exit {direction} points to missing room {ex.target_room_id}")
                else:
                    target = self.rooms[ex.target_room_id]
                    dx, dy, dz = DIRECTION_DELTAS[direction]
                    expected = (room.coord.x + dx, room.coord.y + dy, room.coord.z + dz)
                    if target.coord.to_tuple() != expected:
                        errors.append(
                            f"Coord mismatch: {r_id} {room.coord.to_tuple()} --{direction}--> "
                            f"{target.id} {target.coord.to_tuple()} (expected {expected})"
                        )
        return errors

    def match_item_in_list(self, query: str, item_ids: List[str]) -> Optional[str]:
        q = query.strip().lower()
        if not q:
            return None
        # Exact ID or name or alias match first
        for item_id in item_ids:
            item = self.items[item_id]
            if q == item.id.lower() or q == item.name.lower() or q in [a.lower() for a in item.aliases]:
                return item_id
        # Substring match second
        for item_id in item_ids:
            item = self.items[item_id]
            if q in item.name.lower() or any(q in a.lower() for a in item.aliases) or q in item.id.lower():
                return item_id
        return None
