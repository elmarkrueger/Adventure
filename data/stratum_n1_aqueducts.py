"""Stratum -1: The Sunken Aqueducts & Alchemical Labs (13 Rooms, Z = -1)."""

from typing import Dict
from engine.models import Coord3D, Exit, Room


def get_rooms() -> Dict[str, Room]:
    rooms = [
        Room(
            id="n1_steam_vestibule",
            name="Steam Lift Vestibule",
            coord=Coord3D(0, -1, -1),
            stratum=-1,
            subtitle="Subterranean Reservoir Arrival",
            description=(
                "The hiss of geothermal steam gives way to the cool, reverberant rush of falling "
                "water. You stand inside a vaulted limestone colonnade above the Foundry lift shaft. "
                "Greenish-blue light reflects off subterranean canals to the north, while stone "
                "walkways branch east and west along the reservoir wall."
            ),
            exits={
                "down": Exit("down", "n2_pressure_vault", "Descend in the Steam Lift to Stratum -2."),
                "north": Exit("north", "n1_aqueduct_south", "North onto the Grand Aqueduct South pier."),
                "east": Exit("east", "n1_sluice_overlook", "East along the Sluice Gate Overlook."),
                "west": Exit("west", "n1_drainage_basin", "West toward the Botanical Drainage Basin."),
            },
            items=[],
            features={
                "colonnade": "Carved with bas-reliefs of alchemists pouring stars into underground rivers.",
                "resonator": "An aquamarine-inlaid Mnemonic Resonator stands in an alcove (`play <cylinder>`).",
            },
        ),
        Room(
            id="n1_drainage_basin",
            name="Botanical Drainage Basin",
            coord=Coord3D(-1, -1, -1),
            stratum=-1,
            subtitle="Root-Fed Cistern",
            description=(
                "Calcified roots from the Botanical Domes three strata above hang through ceiling "
                "grates, dripping mineral-rich dew into copper catch-basins. A condensation coil "
                "along the wall collects triple-distilled water."
            ),
            exits={
                "east": Exit("east", "n1_steam_vestibule", "East to the Steam Lift Vestibule."),
                "north": Exit("north", "n1_waterwheel_dynamo", "North to the Waterwheel Dynamo chamber."),
            },
            items=["distilled_water"],
            features={
                "coil": "A螺旋 copper condenser dripping ultra-pure water.",
                "roots": "Silver-barked aerial roots drinking from the mist.",
            },
        ),
        Room(
            id="n1_sluice_overlook",
            name="Sluice Gate Overlook",
            coord=Coord3D(1, -1, -1),
            stratum=-1,
            subtitle="Eastern Spillway",
            description=(
                "A cantilevered stone balcony overlooks a roaring spillway where reservoir water "
                "plunges toward the geothermal boilers below. To the north, the sharp, acrid tang "
                "of nitric spirits drifts from the Alchemical Distillery."
            ),
            exits={
                "west": Exit("west", "n1_steam_vestibule", "West to the Steam Lift Vestibule."),
                "north": Exit("north", "n1_alchemical_distillery", "North into the Alchemical Distillery."),
            },
            items=["muriatic_acid_vial"],
            features={
                "spillway": "White water churns through bronze trash-racks into the dark.",
            },
        ),
        Room(
            id="n1_waterwheel_dynamo",
            name="Waterwheel Dynamo Hall",
            coord=Coord3D(-1, 0, -1),
            stratum=-1,
            subtitle="Hydro-Electric Generator",
            description=(
                "A forty-foot undershot waterwheel of copper-sheathed oak straddles the western "
                "millrace. When the canal water level is raised, the wheel spins a massive "
                "gramme-ring dynamo that powers the Archive UV lamps and lifts above."
            ),
            exits={
                "south": Exit("south", "n1_drainage_basin", "South to the Botanical Drainage Basin."),
                "east": Exit("east", "n1_aqueduct_south", "East to the Grand Aqueduct South pier."),
                "north": Exit("north", "n1_canal_lock_control", "North up the millrace steps to Canal Lock Control."),
            },
            items=[],
            features={
                "waterwheel": "Requires the Canal Lock water level to be set to HIGH in the control room to the north.",
                "dynamo": "Heavy braided cables lead upward from its commutator brushes toward Strata 0 and +1.",
            },
            dynamic_flag_descriptions={
                "n1_waterwheel_engaged": (
                    "\n[bold dodger_blue1]✦ The raised canal water surges through the millrace! "
                    "The Waterwheel Dynamo spins briskly, sending hydro-electric current up the Spire![/bold dodger_blue1]"
                )
            },
        ),
        Room(
            id="n1_aqueduct_south",
            name="Grand Aqueduct South",
            coord=Coord3D(0, 0, -1),
            stratum=-1,
            subtitle="Central Canal Pier",
            description=(
                "You stand at the southern brink of the Grand Subterranean Canal. Across fifty feet "
                "of deep turquoise water lies the northern pier. Between the two piers rests a "
                "floating pontoon causeway—currently stranded twenty feet below pier level unless "
                "the canal lock is raised."
            ),
            exits={
                "south": Exit("south", "n1_steam_vestibule", "South to the Steam Lift Vestibule."),
                "west": Exit("west", "n1_waterwheel_dynamo", "West to the Waterwheel Dynamo Hall."),
                "east": Exit("east", "n1_alchemical_distillery", "East into the Alchemical Distillery."),
                "north": Exit(
                    "north",
                    "n1_aqueduct_north",
                    "Cross the floating pontoon bridge to Grand Aqueduct North.",
                    locked=True,
                    lock_id="pontoon_lock",
                    lock_message=(
                        "The pontoon bridge floats far below the pier edge! Raise the canal water "
                        "level to HIGH in the Canal Lock Control room (`west` then `north`)."
                    ),
                ),
            },
            items=[],
            features={
                "pontoon": "A copper-hulled floating bridge guided by vertical stone grooves.",
                "canal": "Crystal-clear subterranean water fed by deep mountain aquifers.",
            },
            dynamic_flag_descriptions={
                "n1_waterwheel_engaged": (
                    "\n[bold dodger_blue1]✦ With the canal at HIGH water, the pontoon causeway "
                    "floats flush with the stone piers, forming a bridge north![/bold dodger_blue1]"
                )
            },
        ),
        Room(
            id="n1_alchemical_distillery",
            name="Alchemical Distillery",
            coord=Coord3D(1, 0, -1),
            stratum=-1,
            subtitle="Hall of Alembics",
            description=(
                "Coiled glass retorts, serpentine condensers, and copper water-baths cover long "
                "slate worktables. At the center stands the Master Alembic Bench, fitted with a "
                "gas-spirit burner that can be adjusted to `off`, `low`, `medium`, or `high` heat. "
                "To the east is a reinforced acid storage vault; to the north, a glassblowing studio."
            ),
            exits={
                "south": Exit("south", "n1_sluice_overlook", "South to the Sluice Gate Overlook."),
                "west": Exit("west", "n1_aqueduct_south", "West to Grand Aqueduct South."),
                "east": Exit("east", "n1_vitriol_vault", "East into the Vitriol Storage Vault."),
                "north": Exit("north", "n1_glassblower_annex", "North into the Glassblower's Annex."),
            },
            items=["alchemist_notes"],
            features={
                "burner": (
                    "The Alembic Bench gas-spirit burner (`set burner low/medium/high`). "
                    "Currently set to variable heat."
                ),
                "alembic": (
                    "A platinum-lined distillation apparatus. Once the burner is set to `medium`, "
                    "use `unrefined_regia` on `alembic` (`use unrefined_regia on alembic`) to distill pure Aqua Regia."
                ),
            },
            ambient_hint="Read `alchemist_notes`, combine `nitric_acid_vial` + `muriatic_acid_vial`, set `burner` to `medium`, and `use unrefined_regia on alembic`.",
        ),
        Room(
            id="n1_vitriol_vault",
            name="Vitriol Storage Vault",
            coord=Coord3D(2, 0, -1),
            stratum=-1,
            subtitle="Corrosive Reagents Locker",
            description=(
                "Lead-lined shelves arranged inside a cool, pitch-dark rock chamber hold rows of "
                "wax-stoppered stoneware jugs and glass carboys."
            ),
            dark=True,
            exits={
                "west": Exit("west", "n1_alchemical_distillery", "West to the Alchemical Distillery."),
            },
            items=["nitric_acid_vial", "optical_resin"],
            features={
                "shelves": "Lead trays filled with white diatomaceous earth to absorb any acid spills.",
            },
        ),
        Room(
            id="n1_canal_lock_control",
            name="Canal Lock Control",
            coord=Coord3D(-1, 1, -1),
            stratum=-1,
            subtitle="Hydraulic Winch House",
            description=(
                "A stone turret overlooking the northern lock gates. A heavy ratcheted winch-post "
                "controls the miter gates that regulate water depth across the Grand Aqueduct and "
                "the Waterwheel millrace. The winch spindle requires a Heavy Iron Lock-Crank."
            ),
            exits={
                "south": Exit("south", "n1_waterwheel_dynamo", "South down to the Waterwheel Dynamo Hall."),
                "east": Exit("east", "n1_aqueduct_north", "East onto the Grand Aqueduct North pier."),
                "north": Exit("north", "n1_whispering_dome", "North into the Whispering Acoustic Dome."),
            },
            items=[],
            features={
                "lock_winch": (
                    "The miter-gate winch (`use sluice_crank on lock_winch` or `turn lock_winch`). "
                    "Raises the canal water level to HIGH, floating the pontoon bridge and spinning the Waterwheel Dynamo!"
                ),
                "depth_gauge": "Shows the current water depth in the main canal basin.",
            },
            ambient_hint="Use the `sluice_crank` (from the Foundry Tram Dock) on `lock_winch` to raise the canal water level.",
        ),
        Room(
            id="n1_aqueduct_north",
            name="Grand Aqueduct North",
            coord=Coord3D(0, 1, -1),
            stratum=-1,
            subtitle="Northern Canal Pier",
            description=(
                "Broad flagstone steps rise from the northern edge of the subterranean canal toward "
                "a grand archway. To the west stands the Canal Lock Control turret; to the east, "
                "the warm glow of annealing ovens in the Glassblower's Annex; to the north, the "
                "base of the Aqueduct Spiral Stair."
            ),
            exits={
                "south": Exit(
                    "south",
                    "n1_aqueduct_south",
                    "South across the floating pontoon bridge.",
                    locked=True,
                    lock_id="pontoon_lock",
                    lock_message="The pontoon bridge is too low to cross! Raise the water level in Canal Lock Control to the west.",
                ),
                "west": Exit("west", "n1_canal_lock_control", "West to Canal Lock Control."),
                "east": Exit("east", "n1_glassblower_annex", "East into the Glassblower's Annex."),
                "north": Exit("north", "n1_spiral_stair", "North to the Aqueduct Spiral Stair."),
            },
            items=["drained_compass"],
            features={
                "statue": "A weathered bronze statue of an hydrologist holding a plumb-line.",
            },
        ),
        Room(
            id="n1_glassblower_annex",
            name="Glassblower's Annex",
            coord=Coord3D(1, 1, -1),
            stratum=-1,
            subtitle="Optical Quartz Workshop",
            description=(
                "Iron blowpipes, marvering slabs, and lens-grinding laps clutter this workshop where "
                "the Spire's telescope and heliostat optics were ground. To the north stands the "
                "ornate bronze portal of the Sunken Crypt of the Founders, sealed shut with a "
                "massive plug of solid cast gold."
            ),
            exits={
                "south": Exit("south", "n1_alchemical_distillery", "South to the Alchemical Distillery."),
                "west": Exit("west", "n1_aqueduct_north", "West to Grand Aqueduct North."),
                "north": Exit(
                    "north",
                    "n1_founders_crypt",
                    "North into the Sunken Crypt of the Founders.",
                    locked=True,
                    lock_id="gold_crypt_seal",
                    unlock_item_id="aqua_regia",
                    consume_key=True,
                    lock_message=(
                        "The bronze doors are fused shut by a thick royal seal of solid gold! "
                        "No ordinary acid will touch gold—you need pure Aqua Regia (`use aqua_regia on north`)."
                    ),
                    unlock_message=(
                        "You pour the scarlet Aqua Regia over the solid gold seal! In a cloud of "
                        "auric-chloride vapor, the gold dissolves like sugar, and the crypt doors swing open!"
                    ),
                ),
            },
            items=["cracked_lens"],
            features={
                "gold_seal": "A heavy tamper-proof plug of 24-karat gold sealing the northern crypt door (`use aqua_regia on seal`).",
                "grinding_lap": "A cast-iron spindle used to grind concave quartz lenses.",
            },
            ambient_hint="Distill `aqua_regia` in the Alchemical Distillery to dissolve the gold seal on the north door.",
        ),
        Room(
            id="n1_whispering_dome",
            name="Whispering Acoustic Dome",
            coord=Coord3D(-1, 2, -1),
            stratum=-1,
            subtitle="Parabolic Sound Chamber",
            description=(
                "An elliptical dome of polished white marble engineered with uncanny acoustic "
                "precision. A rotatable bronze Parabolic Dish stands at the focal point, aimed "
                "upward toward an acoustic conduit leading to the Atrium Chime Balcony above."
            ),
            exits={
                "south": Exit("south", "n1_canal_lock_control", "South to Canal Lock Control."),
                "east": Exit("east", "n1_spiral_stair", "East to the Aqueduct Spiral Stair."),
            },
            items=["beveled_gear"],
            features={
                "dish": (
                    "A bronze parabolic sound mirror (`set dish focus`). When set to `focus`, "
                    "it amplifies the four-note chime sequence echoing down from Stratum 0: "
                    "'SOL — MI — DO — LA'."
                ),
                "dome": "Even the faintest whisper at one focal point rings crystal-clear at the other.",
            },
            ambient_hint="Take the `beveled_gear` and `set dish focus` to hear the secret four-note Atrium chime melody (`SOL - MI - DO - LA`).",
        ),
        Room(
            id="n1_spiral_stair",
            name="Aqueduct Spiral Stair",
            coord=Coord3D(0, 2, -1),
            stratum=-1,
            subtitle="Ascent to Datum Zero",
            description=(
                "A grand double-helix staircase of carved travertine coils upward through a vaulted "
                "rotunda, rising out of the damp subterranean strata toward the warm brass light "
                "of the Grand Clockwork Atrium (`Z = 0`)."
            ),
            exits={
                "south": Exit("south", "n1_aqueduct_north", "South to Grand Aqueduct North."),
                "west": Exit("west", "n1_whispering_dome", "West into the Whispering Acoustic Dome."),
                "east": Exit(
                    "east",
                    "n1_founders_crypt",
                    "East into the Sunken Crypt of the Founders.",
                    locked=True,
                    lock_id="gold_crypt_seal",
                    unlock_item_id="aqua_regia",
                    consume_key=True,
                    lock_message="The side grille to the Founders' Crypt is sealed by the same solid gold lock (`use aqua_regia`).",
                    unlock_message="The Aqua Regia dissolves the gold lock-bolt, opening the crypt grille!",
                ),
                "up": Exit("up", "z0_great_stairwell", "Ascend the double-helix stair to Stratum 0 (The Grand Clockwork Atrium)."),
            },
            items=[],
            features={
                "staircase": "Each stone riser is carved with elevation markers counting up toward 0m Datum.",
            },
        ),
        Room(
            id="n1_founders_crypt",
            name="Sunken Crypt of the Founders",
            coord=Coord3D(1, 2, -1),
            stratum=-1,
            subtitle="Reliquary of the First Horologists",
            description=(
                "Behind the dissolved gold seal lies a serene sepulcher lit by phosphorescent "
                "water-lamps. Alabaster sarcophagi surround an octagonal altar bearing an "
                "aquamarine Mnemonic Cylinder and a perforated brass dispatch card."
            ),
            exits={
                "south": Exit("south", "n1_glassblower_annex", "South to the Glassblower's Annex."),
                "west": Exit("west", "n1_spiral_stair", "West to the Aqueduct Spiral Stair."),
            },
            items=["cylinder_3", "pneumatic_passkey"],
            features={
                "altar": "Inscribed: 'MEMORY ANCHOR III — THE WHISPER IN THE RESERVOIR'.",
                "sarcophagi": "Tombs of the master hydrologists and glassmakers who built Stratum -1.",
            },
            ambient_hint="Take `cylinder_3` and `pneumatic_passkey`! Now ascend from the Spiral Stair (`up`) to Stratum 0.",
        ),
    ]
    return {r.id: r for r in rooms}
