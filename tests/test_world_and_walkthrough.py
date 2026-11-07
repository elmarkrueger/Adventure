"""Automated test suite and full golden-path walkthrough verification."""

from pathlib import Path
import tempfile
import unittest

from engine.models import GameState
from engine.world_builder import World
from engine.commands import process_command
from engine.ui import render_minimap_text
from engine.save_system import load_game, save_game


class TestAethelgardSpire(unittest.TestCase):
    def setUp(self) -> None:
        self.world = World()
        self.state = GameState()

    def test_01_world_graph_and_coordinates(self) -> None:
        """Verify 88 rooms across 7 strata, 92 items, 26 recipes, and 0 coordinate errors."""
        self.assertEqual(len(self.world.rooms), 88)
        self.assertEqual(len(self.world.items), 92)
        self.assertEqual(len(self.world.recipes), 26)

        strata_seen = {r.stratum for r in self.world.rooms.values()}
        self.assertEqual(strata_seen, {-3, -2, -1, 0, 1, 2, 3})

        errors = self.world.validate_graph()
        self.assertEqual(errors, [], f"World graph validation errors: {errors}")

    def test_02_inventory_limit_drop_and_satchel_upgrade(self) -> None:
        """Verify 8-slot inventory cap, drop persistence, and 10-slot satchel upgrade."""
        # Fill 8 slots
        self.state.inventory = [
            "fractured_vial",
            "unlit_lantern",
            "glow_moss",
            "rusted_grapnel",
            "brine_solvent",
            "mycelial_cord",
            "copper_wire_spool",
            "emery_cloth",
        ]
        # Place another item in current room and try to take it (should fail at 8/8)
        room = self.world.rooms[self.state.current_room_id]
        room.items.append("raw_quartz_crystal")
        res = process_command(self.world, self.state, "take raw_quartz_crystal")
        self.assertIn("Inventory Full", res.message)
        self.assertNotIn("raw_quartz_crystal", self.state.inventory)

        # Drop an item to free 1 slot
        res_drop = process_command(self.world, self.state, "drop fractured_vial")
        self.assertIn("fractured_vial", room.items)
        self.assertNotIn("fractured_vial", self.state.inventory)

        # Now taking raw_quartz_crystal succeeds
        res_take = process_command(self.world, self.state, "take raw_quartz_crystal")
        self.assertIn("raw_quartz_crystal", self.state.inventory)

        # Craft and equip Archivist's Satchel to expand to 10 slots
        self.state.inventory.remove("raw_quartz_crystal")
        self.state.inventory.remove("emery_cloth")
        self.state.inventory.extend(["torn_satchel", "cured_leather"])
        res_craft = process_command(self.world, self.state, "combine torn_satchel with cured_leather")
        self.assertIn("archivist_satchel", self.state.inventory)
        res_use = process_command(self.world, self.state, "use archivist_satchel")
        self.assertEqual(self.state.max_inventory_slots, 10)
        self.assertIn("10 slots", res_use.message)

    def test_03_fog_of_war_minimap_and_notebook(self) -> None:
        """Verify fog-of-war hides unvisited rooms and notebook tracks coordinates."""
        # At start, only n3_awakening_slab is visited
        map_str = render_minimap_text(self.world, self.state, -3)
        self.assertIn("[★]", map_str)
        self.assertIn("[?]", map_str)
        # Unexplored Stratum +3 should indicate no areas explored yet
        map_p3 = render_minimap_text(self.world, self.state, 3)
        self.assertIn("No areas explored", map_p3)

        # Add a tagged note and a general note
        process_command(self.world, self.state, "note tag sluice Open A and C, keep B closed")
        process_command(self.world, self.state, "note add Check Phosphor Cavern east")
        self.assertEqual(len(self.state.notes), 2)
        self.assertEqual(self.state.notes[0].coord, (0, 0, -3))

        notes_res = process_command(self.world, self.state, "notes sluice")
        self.assertIn("Open A and C", notes_res.message)

        process_command(self.world, self.state, "note del 1")
        self.assertEqual(len(self.state.notes), 1)

    def test_04_save_and_load_roundtrip(self) -> None:
        """Verify saving and loading preserves exact world and player state."""
        process_command(self.world, self.state, "take unlit_lantern")
        process_command(self.world, self.state, "e")
        process_command(self.world, self.state, "take glow_moss")
        process_command(self.world, self.state, "combine lantern with moss")
        process_command(self.world, self.state, "note add Crafted phosphor lantern")

        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            ok, _, _ = save_game(self.world, self.state, "test_slot", save_dir=tmp_path)
            self.assertTrue(ok)

            loaded_w, loaded_s, msg = load_game("test_slot", save_dir=tmp_path)
            self.assertIsNotNone(loaded_w)
            self.assertIsNotNone(loaded_s)
            self.assertEqual(loaded_s.current_room_id, "n3_phosphor_cavern")
            self.assertIn("phosphor_lantern", loaded_s.inventory)
            self.assertEqual(len(loaded_s.notes), 1)
            self.assertEqual(loaded_s.notes[0].text, "Crafted phosphor lantern")

    def test_05_full_golden_path_walkthrough_all_7_strata(self) -> None:
        """Execute a complete playthrough from Stratum -3 to Stratum +3 True Ending."""
        cmds = [
            # --- STRATUM -3: THE BIOLUMINESCENT ABYSS ---
            "take unlit_lantern",
            "e",  # Phosphor Cavern (1, 0, -3)
            "take glow_moss",
            "combine unlit_lantern with glow_moss",
            "s",  # Survivor's Alcove (1, -1, -3)
            "take brine_solvent",
            "read abyssal_tablet",
            "n",
            "w",  # Awakening Slab (0, 0, -3)
            "w",  # Sluice Control (-1, 0, -3)
            "s",  # Brine Filtration Pool (-1, -1, -3)
            "take rusted_grapnel",
            "combine rusted_grapnel with brine_solvent",
            "w",  # Calcified Cistern (-2, -1, -3)
            "take copper_wire_spool",
            "take cured_leather",
            "e",
            "n",  # Sluice Control (-1, 0, -3)
            "e",  # Awakening Slab (0, 0, -3)
            "n",  # Echoing Sump (0, 1, -3)
            "e",  # Mycelial Bridge (1, 1, -3)
            "take mycelial_cord",
            "combine mycelial_cord with copper_wire_spool",
            "combine clean_grapnel with braided_rope",
            "e",  # Submerged Bell-Dock (2, 1, -3)
            "take valve_wheel",
            "w",
            "w",  # Echoing Sump (0, 1, -3)
            "s",  # Awakening Slab
            "w",  # Sluice Control (-1, 0, -3)
            "turn valve_a",
            "use valve_wheel on spindle_c",
            "n",  # Drowned Ossuary (-1, 1, -3) — now drained!
            "take cylinder_1",
            "play cylinder_1",
            "take torn_satchel",
            "combine torn_satchel with cured_leather",
            "use archivist_satchel",  # Inventory upgraded to 10 slots!
            "e",  # Echoing Sump (0, 1, -3)
            "e",  # Mycelial Bridge (1, 1, -3)
            "n",  # Whispering Fissure (1, 2, -3)
            "use grappling_hook on shaft",
            "u",  # Ascend to Stratum -2: Venting Chimney Base (1, 2, -2)

            # --- STRATUM -2: THE GEOTHERMAL FOUNDRY ---
            "w",  # Abyssal Lift Landing (0, 2, -2)
            "w",  # Counterweight Winch Room (-1, 2, -2)
            "pull winch",  # Unlocks elevator shortcut to Stratum -3
            "take insulated_gauntlets",
            "s",  # Steam Turbine Gallery (-1, 1, -2)
            "take forge_hammer",
            "w",  # Forge-Master's Office (-2, 1, -2)
            "take broken_sanctum_key",
            "e",
            "e",  # Boiler Manifold Hall (0, 1, -2)
            "turn valve_alpha",
            "turn valve_beta",
            "turn valve_gamma",  # Manifold at 120 PSI!
            "s",  # Magma Siphon Bridge (0, 0, -2)
            "take empty_crucible",
            "w",  # Pneumatic Dispatch Hub (-1, 0, -2)
            "take brass_ingot",
            "take broken_coupler",
            "combine empty_crucible with brass_ingot",
            "s",  # Foundry Tram Dock (-1, -1, -2)
            "take sluice_crank",
            "n",
            "e",  # Magma Siphon Bridge (0, 0, -2)
            "use unheated_brass_crucible on furnace",
            "e",  # Obsidian Cooling Vats (1, 0, -2)
            "take clay_blank",
            "combine clay_blank with broken_sanctum_key",
            "combine molten_brass_crucible with key_mold",
            "drop broken_sanctum_key",
            "drop empty_crucible",
            "take cryo_canister",
            "use cryo_canister on slag",
            "s",  # Slag Crucible Chamber (1, -1, -2)
            "take cylinder_2",
            "play cylinder_2",
            "take slag_nodule",
            "combine slag_nodule with forge_hammer",
            "combine broken_coupler with meteoric_pin",
            "drop forge_hammer",
            "w",  # Pressure Regulation Vault (0, -1, -2)
            "use sanctum_key on up",
            "drop sanctum_key",
            "u",  # Ascend to Stratum -1: Steam Lift Vestibule (0, -1, -1)

            # --- STRATUM -1: THE SUNKEN AQUEDUCTS & LABS ---
            "e",  # Sluice Gate Overlook (1, -1, -1)
            "take muriatic_acid_vial",
            "n",  # Alchemical Distillery (1, 0, -1)
            "e",  # Vitriol Storage Vault (2, 0, -1)
            "take nitric_acid_vial",
            "take optical_resin",
            "w",  # Alchemical Distillery (1, 0, -1)
            "combine nitric_acid_vial with muriatic_acid_vial",
            "set burner medium",
            "use unrefined_regia on alembic",
            "w",  # Grand Aqueduct South (0, 0, -1)
            "w",  # Waterwheel Dynamo Hall (-1, 0, -1)
            "n",  # Canal Lock Control (-1, 1, -1)
            "use sluice_crank on lock_winch",
            "drop sluice_crank",
            "n",  # Whispering Acoustic Dome (-1, 2, -1)
            "set dish focus",
            "take beveled_gear",
            "e",  # Aqueduct Spiral Stair (0, 2, -1)
            "s",  # Grand Aqueduct North (0, 1, -1)
            "e",  # Glassblower's Annex (1, 1, -1)
            "take cracked_lens",
            "combine cracked_lens with optical_resin",
            "use aqua_regia on north",
            "n",  # Sunken Crypt of the Founders (1, 2, -1)
            "take cylinder_3",
            "play cylinder_3",
            "w",  # Aqueduct Spiral Stair (0, 2, -1)
            "u",  # Ascend to Stratum 0: Great Spiral Stairwell (0, 2, 0)

            # --- STRATUM 0: THE GRAND CLOCKWORK ATRIUM ---
            "e",  # Maintainer's Barracks (1, 2, 0)
            "take chime_mallet",
            "w",
            "w",  # Acoustic Chime Balcony (-1, 2, 0)
            "play sol mi do la",
            "drop chime_mallet",
            "s",  # Pneumatic Locker Room (-1, 1, 0)
            "take brass_gimbal",
            "combine mended_lens with brass_gimbal",
            "stash cylinder_1",
            "stash cylinder_2",
            "stash cylinder_3",
            "e",  # North Gear-Train Gallery (0, 1, 0)
            "use beveled_gear on spindle",
            "e",  # Chronometer Control Booth (1, 1, 0)
            "dial 4719",
            "s",  # East Cartographer's Wing (1, 0, 0)
            "e",  # Sun-Shaft Balcony (2, 0, 0)
            "pull shutter",
            "w",
            "s",  # Hall of the Seven Anchors (1, -1, 0)
            "take cylinder_4",
            "play cylinder_4",
            "w",  # South Escapement Hall (0, -1, 0)
            "n",  # Central Pendulum Rotunda (0, 0, 0)
            "w",  # West Tramway Concourse (-1, 0, 0)
            "use repaired_coupler on west",
            "w",  # Western Cantilever Span (-2, 0, 0)
            "take lead_counterweight",
            "take copper_fuse",
            "e",
            "s",  # Vault of Weights (-1, -1, 0)
            "use lead_counterweight on cradle",
            "e",  # South Escapement Hall (0, -1, 0)
            "pull brake",
            "n",  # Central Pendulum Rotunda (0, 0, 0)
            "u",  # Ascend to Stratum +1: Archive Rotunda (0, 0, 1)

            # --- STRATUM +1: THE MNEMONIC ARCHIVES ---
            "s",  # South Stacks (0, -1, 1)
            "take dried_dream_leaf",
            "w",  # Phonograph Listening Booths (-1, -1, 1)
            "take uv_bulb",
            "n",  # West Stacks (-1, 0, 1)
            "pull treatise",
            "w",  # Secret Vault (-2, 0, 1)
            "take cylinder_5",
            "play cylinder_5",
            "take tuning_fork_432",
            "e",
            "n",  # Curator's Private Study (-1, 1, 1)
            "take blank_blueprint",
            "stash cylinder_4",
            "stash cylinder_5",
            "s",
            "s",
            "e",
            "e",  # Parchment Restoration Lab (1, -1, 1)
            "combine blank_blueprint with uv_bulb",
            "drop uv_bulb",
            "drop revealed_blueprint",
            "n",  # East Stacks (1, 0, 1)
            "n",  # Acoustic Loom Chamber (1, 1, 1)
            "use tuning_fork_432 on loom",
            "n",  # Upper Gallery Overlook (1, 2, 1)
            "take empty_smoker",
            "combine empty_smoker with dried_dream_leaf",
            "w",  # Cipher Rotunda (0, 2, 1)
            "dial MNEMOS",
            "w",  # Paternoster Lift Landing (-1, 2, 1)
            "use copper_fuse on fusebox",
            "u",  # Ascend to Stratum +2: Conservatory Central Dome (-1, 2, 2)

            # --- STRATUM +2: THE AETHERIAL BOTANICAL DOMES ---
            "e",  # Heliostat Mirror Ring North (0, 2, 2)
            "set mirror_north center",
            "e",  # Spore Condenser Lab (1, 2, 2)
            "take starlight_pollen",
            "s",  # Starlight Orchid Grove (1, 1, 2)
            "use starlight_pollen on orchid",
            "take tuning_fork_528",
            "w",  # Prism Refraction Tower (0, 1, 2)
            "use focusing_optic on cradle",
            "s",  # Heliostat Mirror Ring South (0, 0, 2)
            "set mirror_south center",  # Awakens Abyssal Solar Core on Stratum -3!
            "w",  # Apiary of Brass Bees (-1, 0, 2)
            "use lit_smoker on hive",
            "drop lit_smoker",
            "take conducting_wax",
            "e",
            "e",  # Wind-Organ Loft (1, 0, 2)
            "take cylinder_6",
            "play cylinder_6",
            "play CEGB",
            "s",  # Cloud-Pier Lookout (1, -1, 2)
            "take aether_capacitor",
            "combine aether_capacitor with conducting_wax",
            "w",  # Celestial Elevator Lobby (0, -1, 2)
            "u",  # Ascend to Stratum +3: Observatory Arrival Platform (0, -1, 3)

            # --- STRATUM +3: THE CELESTIAL OBSERVATORY & CROWN ---
            "e",  # Architect's Living Quarters (1, -1, 3)
            "take architect_signet",
            "take cylinder_7",
            "play cylinder_7",
            "n",  # Equatorial Telescope Dome (1, 0, 3)
            "e",  # Lightning Rod Spire (2, 0, 3)
            "use waxed_capacitor on rod",
            "w",
            "n",  # East Harmonic Pylon (1, 1, 3)
            "use tuning_fork_528 on pylon",
            "s",
            "w",  # Zenith Glass Bridge (0, 0, 3)
            "use architect_signet on north",
            "w",  # Astrolabe Calibration Deck (-1, 0, 3)
            "set astrolabe 240 65",
            "n",  # West Harmonic Pylon (-1, 1, 3)
            "use tuning_fork_432 on pylon",
            "e",  # Memory Core Antechamber (0, 1, 3)
            "use charged_capacitor on receptacle",
            "n",  # The Resonance Crown (Apex) (0, 2, 3)
            "activate core",
        ]

        for step_idx, cmd in enumerate(cmds, 1):
            res = process_command(self.world, self.state, cmd)
            self.assertIsNotNone(res.message, f"Step {step_idx} ({cmd}) returned None")

        self.assertTrue(self.state.flags.get("n3_solar_core_awakened"), "Abyssal Solar Core should be awakened")
        self.assertEqual(len(self.state.memories_restored), 7, "All 7 Mnemonic Cylinders should be restored")
        self.assertTrue(self.state.game_won, "Game should be won after activating core")
        self.assertEqual(self.state.ending_type, "TRUE_HARMONIC_SYNTHESIS")


if __name__ == "__main__":
    unittest.main()
