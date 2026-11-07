"""Stratum -3: The Bioluminescent Abyss (12 Rooms, Z = -3)."""

from typing import Dict
from engine.models import Coord3D, Exit, Room


def get_rooms() -> Dict[str, Room]:
    rooms = [
        Room(
            id="n3_awakening_slab",
            name="Obsidian Awakening Slab",
            coord=Coord3D(0, 0, -3),
            stratum=-3,
            subtitle="The Sub-Basal Sanctuary",
            description=(
                "You stand beside a carved slab of wet black obsidian at the nadir of a colossal "
                "vertical chasm. Four hundred meters overhead, darkness swallows the shaft, broken "
                "only by a vertical collimating aperture waiting for light from above. Filigree "
                "channels in the stone floor drain trickles of silver-tinted alchemical brine. "
                "In the center of the chamber rests a dormant Solar Core crystal."
            ),
            exits={
                "north": Exit("north", "n3_echoing_sump", "A dripping archway leading toward the central sump."),
                "east": Exit("east", "n3_phosphor_cavern", "A fissure glowing with faint cyan fungal light."),
                "west": Exit("west", "n3_sluice_control", "A rusted iron gangway leading to a valve alcove."),
            },
            items=["fractured_vial", "unlit_lantern"],
            features={
                "slab": (
                    "The volcanic glass slab bears shallow depressions shaped for a human body. "
                    "Scratched into the stone by a trembling fingernail are the words: "
                    "'CRAFT LIGHT. ASCEND THE SEVEN STRATA. RECLAIM WHAT YOU CHOSE TO FORGET.'"
                ),
                "solar_core": (
                    "A massive multifaceted crystal anchor embedded in the floor directly beneath "
                    "the Spire's central vertical axis. It is currently cold and dark—awaiting a "
                    "concentrated beam of sunlight from the Botanical Domes far above."
                ),
                "resonator": (
                    "An acoustic brass horn and quartz phonograph mandrel bolted beside the slab. "
                    "You can play any Mnemonic Cylinder here (`play <cylinder>`)."
                ),
            },
            dynamic_flag_descriptions={
                "n3_solar_core_awakened": (
                    "\n[bold bright_yellow]✦ A blinding column of golden sunlight spears down from "
                    "Stratum +2, igniting the Abyssal Solar Core with a deep harmonic thrum![/bold bright_yellow]"
                )
            },
            ambient_hint="Combine the Unlit Brass Lantern with Luminous Mycelium from the east cavern to see in dark chambers.",
        ),
        Room(
            id="n3_phosphor_cavern",
            name="Phosphor Cavern",
            coord=Coord3D(1, 0, -3),
            stratum=-3,
            subtitle="Bioluminescent Grotto",
            description=(
                "Curtains of cyan and cerulean mycelium drape from the vaulted limestone ceiling, "
                "bathing the wet rock in an eerie, dreamlike twilight. Spores drift lazily on warm "
                "updrafts rising from deeper fissures. A narrow ledge winds north toward a fibrous "
                "bridge, while a dry cleft opens to the south."
            ),
            exits={
                "west": Exit("west", "n3_awakening_slab", "Back to the Obsidian Awakening Slab."),
                "north": Exit("north", "n3_mycelial_bridge", "A natural arch overgrown with thick fungal tendons."),
                "south": Exit("south", "n3_hermit_alcove", "A low stone crawlspace tucked behind hanging moss."),
            },
            items=["glow_moss", "raw_quartz_crystal"],
            features={
                "canopy": (
                    "Thousands of bioluminescent fruiting bodies pulse in slow, rhythmic waves, "
                    "as though synchronized to a distant pendulum."
                ),
                "fissures": "Warm vapor carrying a faint tang of sulfur rises from Stratum -2 above.",
            },
            ambient_hint="Take the Luminous Mycelium Clump and combine it with your Unlit Brass Lantern (`combine lantern with moss`).",
        ),
        Room(
            id="n3_hermit_alcove",
            name="Survivor's Alcove",
            coord=Coord3D(1, -1, -3),
            stratum=-3,
            subtitle="Forgotten Shelter",
            description=(
                "Tucked beneath an overhang of basalt is an improvised camp built long ago—in fact, "
                "judging by the handwriting on the wall, built by you before you drank the Oblivion "
                "Draught. A stone workbench holds survival supplies and a waterproof slate."
            ),
            exits={
                "north": Exit("north", "n3_phosphor_cavern", "Out to the Phosphor Cavern."),
            },
            items=["brine_solvent", "abyssal_tablet", "emery_cloth"],
            features={
                "workbench": (
                    "On the bench sits a chalk diagram showing three sluice valves: "
                    "'VALVE A: OPEN | VALVE B: CLOSED | VALVE C: ATTACH WHEEL & OPEN'."
                ),
                "wall": (
                    "Charcoal tally marks line the stone, beside a warning: "
                    "'Do not trust the Chorister's lullaby. Only the seven cylinders hold the truth.'"
                ),
            },
            ambient_hint="Read the Slate Tablet (`read tablet`) to learn how to drain the Drowned Ossuary.",
        ),
        Room(
            id="n3_sluice_control",
            name="Sluice Control Niche",
            coord=Coord3D(-1, 0, -3),
            stratum=-3,
            subtitle="Hydraulic Drainage Post",
            description=(
                "A riveted iron platform straddles a roaring subterranean culvert. Three heavy "
                "cast-iron sluice manifolds—marked A, B, and C—govern the water level of the "
                "Drowned Ossuary to the north. Valve A and Valve B have handwheels attached, "
                "but Spindle C is bare, its bronze wheel missing."
            ),
            exits={
                "east": Exit("east", "n3_awakening_slab", "Across the gangway to the Awakening Slab."),
                "north": Exit(
                    "north",
                    "n3_drowned_ossuary",
                    "A stone portal leading into the Ossuary.",
                    locked=True,
                    lock_id="ossuary_flood_lock",
                    lock_message=(
                        "Black brine fills the Ossuary to the ceiling! You must either drain it using "
                        "the three sluice valves here or carry the Pressurized Brass Diving Hood."
                    ),
                ),
                "south": Exit("south", "n3_brine_pool", "Down a slick stone ramp to the filtration pools."),
            },
            items=[],
            features={
                "valve_a": "Intake Bypass Valve A. Turn it with `turn valve_a`.",
                "valve_b": "Backflow Equalizer Valve B. Turn it with `turn valve_b`.",
                "spindle_c": "Sump Outflow Spindle C. Needs the Octagonal Bronze Valve Wheel (`use valve_wheel on spindle_c`).",
                "gauge": "A brass hydro-gauge measuring the water depth inside the northern Ossuary.",
            },
            dynamic_flag_descriptions={
                "n3_ossuary_drained": (
                    "\n[bold cyan]✦ With Valves A and C open and B closed, the culvert roars! "
                    "The floodwaters have drained from the Drowned Ossuary to the north.[/bold cyan]"
                )
            },
            ambient_hint="Find the Bronze Valve Wheel in the eastern dock, attach it to `spindle_c`, and set A=Open, B=Closed, C=Open.",
        ),
        Room(
            id="n3_brine_pool",
            name="Brine Filtration Pool",
            coord=Coord3D(-1, -1, -3),
            stratum=-3,
            subtitle="Mineral Settling Basin",
            description=(
                "Terraced basins of milky, mineral-saturated water step down into the gloom. "
                "Stalagmites of pure white salt crust the railings. A rusted tool rack hangs beside "
                "a partially submerged archway leading west."
            ),
            exits={
                "north": Exit("north", "n3_sluice_control", "Up the slick stone ramp to Sluice Control."),
                "west": Exit("west", "n3_calcified_cistern", "Through a salt-crusted archway."),
            },
            items=["rusted_grapnel", "calcified_barnacle"],
            features={
                "basins": "Thick salt crystals form geometric lattices across the water's surface.",
                "rack": "Most tools have rusted to dust, save for a heavily encrusted iron grapnel.",
            },
            ambient_hint="Combine the Encrusted Iron Grapnel with the Flask of Acidic Brine-Solvent to strip away the scale.",
        ),
        Room(
            id="n3_calcified_cistern",
            name="Calcified Cistern",
            coord=Coord3D(-2, -1, -3),
            stratum=-3,
            subtitle="Old Telemetry Conduit",
            description=(
                "This cylindrical stone tank once housed the Spire's deep-seismic sensors. "
                "Now, broken gutta-percha conduits hang from the ceiling like vines, exposing "
                "reels of braided copper wire. The chamber is pitch-dark without a light source."
            ),
            dark=True,
            exits={
                "east": Exit("east", "n3_brine_pool", "Back to the Brine Filtration Pool."),
            },
            items=["copper_wire_spool", "cured_leather"],
            features={
                "conduits": "Heavy telegraph cables that once carried seismic readings up to the Atrium.",
                "sensors": "Cracked glass seismographs frozen at the exact moment of the Resonance Collapse.",
            },
            ambient_hint="Take the Spool of Braided Copper Wire and Roll of Cured Basal-Hide.",
        ),
        Room(
            id="n3_echoing_sump",
            name="Echoing Sump",
            coord=Coord3D(0, 1, -3),
            stratum=-3,
            subtitle="Central Chasm Floor",
            description=(
                "A circular stone plaza bordered by massive buttresses that support the weight of "
                "six strata above. Every footstep rings out in a cascade of metallic echoes. "
                "To the north stands the bottom cage-dock of the Abyssal Counterweight Lift; "
                "to the west lies the Ossuary vault; to the east, a bridge of woven fungal roots."
            ),
            exits={
                "south": Exit("south", "n3_awakening_slab", "South to the Obsidian Awakening Slab."),
                "east": Exit("east", "n3_mycelial_bridge", "Onto the woven Mycelial Bridge."),
                "west": Exit(
                    "west",
                    "n3_drowned_ossuary",
                    "West into the Drowned Ossuary.",
                    locked=True,
                    lock_id="ossuary_flood_lock",
                    lock_message="The Ossuary is flooded to the arch crown! Drain it at Sluice Control first.",
                ),
                "north": Exit("north", "n3_lift_shaft_bottom", "North to the Abyssal Lift Shaft."),
            },
            items=[],
            features={
                "buttresses": "Cyclopean arches of basalt reinforced with riveted wrought-iron bands.",
                "plaza": "Carved into the center of the floor is the compass rose of Aethelgard.",
            },
        ),
        Room(
            id="n3_mycelial_bridge",
            name="Mycelial Suspension Bridge",
            coord=Coord3D(1, 1, -3),
            stratum=-3,
            subtitle="Living Span",
            description=(
                "A swaying bridge woven from petrified fungal cords spans a bottomless black crevasse. "
                "Bundles of dried mycelial fiber hang from the handrails. Eastward, the bridge "
                "terminates at a flooded diving-bell dock; northward, a rocky ledge climbs toward "
                "a narrow vertical chimney."
            ),
            exits={
                "south": Exit("south", "n3_phosphor_cavern", "South into the glowing Phosphor Cavern."),
                "west": Exit("west", "n3_echoing_sump", "West to the Echoing Sump plaza."),
                "east": Exit("east", "n3_submerged_bell_dock", "East to the Submerged Bell-Dock."),
                "north": Exit("north", "n3_whispering_fissure", "North toward the Whispering Fissure chimney."),
            },
            items=["mycelial_cord"],
            features={
                "crevasse": "Far below, the faint crimson glow of deep earth magma reflects off rising mist.",
                "handrails": "Woven from remarkably tough fungal sinew.",
            },
            ambient_hint="Combine Raw Mycelial Fiber Bundle with the Spool of Braided Copper Wire to craft a climbing rope.",
        ),
        Room(
            id="n3_submerged_bell_dock",
            name="Submerged Bell-Dock",
            coord=Coord3D(2, 1, -3),
            stratum=-3,
            subtitle="Abyssal Pier",
            description=(
                "An iron pier juts out over a subterranean lake as still as black glass. "
                "Suspended from an A-frame crane is an antique brass diving bell. Without a lantern, "
                "this cavern is shrouded in impenetrable darkness."
            ),
            dark=True,
            exits={
                "west": Exit("west", "n3_mycelial_bridge", "West across the Mycelial Bridge."),
            },
            items=["valve_wheel", "diving_helmet"],
            features={
                "diving_bell": (
                    "Inside the open hatch of the bell rests an Octagonal Bronze Valve Wheel and a "
                    "Pressurized Brass Diving Hood."
                ),
                "lake": "Blind white cave-amphipods dart beneath the surface whenever your light sweeps past.",
            },
            ambient_hint="Take the Octagonal Bronze Valve Wheel to repair Spindle C in the Sluice Control Niche.",
        ),
        Room(
            id="n3_drowned_ossuary",
            name="Drowned Ossuary",
            coord=Coord3D(-1, 1, -3),
            stratum=-3,
            subtitle="Vault of the First Excavators",
            description=(
                "Rows of arched stone niches line the dripping walls of this solemn vault. "
                "Now that the black brine has receded, the central reliquary pedestal stands "
                "exposed on the mosaic floor. A crystalline phonograph cylinder gleams inside "
                "an open bronze coffer."
            ),
            dark=True,
            exits={
                "east": Exit("east", "n3_echoing_sump", "East to the Echoing Sump."),
                "south": Exit("south", "n3_sluice_control", "South to the Sluice Control Niche."),
            },
            items=["cylinder_1", "torn_satchel"],
            features={
                "reliquary": (
                    "The bronze coffer bears your own seal: 'MEMORY ANCHOR I — DEPOSIT OF VAELEN KORR'."
                ),
                "niches": "Memorial plaques honor the miners and horologists who excavated the chasm.",
            },
            ambient_hint="Take Mnemonic Cylinder I and play it on any Resonator (`play cylinder 1`) to recover your first memory!",
        ),
        Room(
            id="n3_whispering_fissure",
            name="Whispering Fissure",
            coord=Coord3D(1, 2, -3),
            stratum=-3,
            subtitle="Emergency Ventilation Shaft",
            description=(
                "A narrow vertical chimney cut through solid basalt vents hot air from the "
                "Geothermal Foundry a hundred and forty meters above. The lower twenty feet of the "
                "iron rung ladder have sheared away, leaving an overhanging iron stanchion just "
                "within throwing range of a grappling hook."
            ),
            exits={
                "south": Exit("south", "n3_mycelial_bridge", "South to the Mycelial Suspension Bridge."),
                "up": Exit(
                    "up",
                    "n2_venting_chimney",
                    "Up the vertical ventilation shaft via your anchored grappling rope.",
                    locked=True,
                    lock_id="n3_fissure_climb",
                    unlock_item_id="grappling_hook",
                    lock_message=(
                        "The lower rungs are missing! You need an Abyssal Grappling Hook "
                        "(`use grappling_hook on shaft`) to reach the upper ladder."
                    ),
                    unlock_message=(
                        "You whirl the Abyssal Grappling Hook and hurl it upward! The steel prongs "
                        "bite solidly into the iron stanchion overhead, trailing the copper-core rope."
                    ),
                ),
            },
            items=[],
            features={
                "shaft": (
                    "An overhanging iron rung-stanchion juts out twenty-five feet up the chimney. "
                    "Use an Abyssal Grappling Hook (`use grappling_hook on shaft`) to rig a climbable line."
                ),
            },
            ambient_hint="Craft the Abyssal Grappling Hook (`clean_grapnel` + `braided_rope`) and `use grappling_hook on shaft` to ascend to Stratum -2!",
        ),
        Room(
            id="n3_lift_shaft_bottom",
            name="Abyssal Lift Shaft (Bottom)",
            coord=Coord3D(0, 2, -3),
            stratum=-3,
            subtitle="Counterweight Cage Dock",
            description=(
                "Twin vertical guide-rails rise into the gloom toward Stratum -2. A heavy wrought-iron "
                "elevator cage rests in the pit, but its haul-cable hangs slack—the counterweight "
                "in the Foundry Winch Room above has not yet been released."
            ),
            exits={
                "south": Exit("south", "n3_echoing_sump", "South to the Echoing Sump."),
                "up": Exit(
                    "up",
                    "n2_lift_landing",
                    "Ascend in the Counterweight Lift Cage to Stratum -2.",
                    locked=True,
                    lock_id="n3_counterweight_lock",
                    lock_message=(
                        "The lift cable is uncoupled! Release the counterweight in the Winch Room on "
                        "Stratum -2 (reachable first via the Whispering Fissure to the east)."
                    ),
                ),
            },
            items=[],
            features={
                "cage": "A heavy iron freight cage connecting Stratum -3 and Stratum -2.",
                "cable": "Three-inch braided steel cable running up to the Foundry Winch Room.",
            },
            dynamic_flag_descriptions={
                "n2_counterweight_released": (
                    "\n[bold cyan]✦ The heavy counterweight is engaged! The lift cage is now "
                    "operational between Stratum -3 and Stratum -2 (`up`).[/bold cyan]"
                )
            },
        ),
    ]
    return {r.id: r for r in rooms}
