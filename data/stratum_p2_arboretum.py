"""Stratum +2: The Aetherial Botanical Domes & Prism Arrays (12 Rooms, Z = +2)."""

from typing import Dict
from engine.models import Coord3D, Exit, Room


def get_rooms() -> Dict[str, Room]:
    rooms = [
        Room(
            id="p2_conservatory_dome",
            name="Conservatory Central Dome",
            coord=Coord3D(-1, 2, 2),
            stratum=2,
            subtitle="Sunlit Glass Pavilion",
            description=(
                "Stepping out of the Paternoster lift, you are greeted by dazzling mountain sunlight "
                "streaming through a soaring geodesic dome of leaded crystal and wrought iron. "
                "Silver-barked cloud-trees and luminescent ferns perfume the warm air with ozone "
                "and jasmine. Catwalks lead east toward the northern heliostat array and south "
                "toward the hydroponic reservoirs."
            ),
            exits={
                "down": Exit("down", "p1_paternoster_landing", "Ride the Paternoster lift down to Stratum +1."),
                "east": Exit("east", "p2_mirror_north", "East to the Heliostat Mirror Ring North."),
                "south": Exit("south", "p2_hydroponic_reservoir", "South to the Hydroponic Reservoir."),
            },
            items=[],
            features={
                "dome": "Three hundred meters above the mountain cloudline, the sky is a deep cobalt blue.",
                "resonator": "A jade-inlaid Mnemonic Resonator stands among the ferns (`play <cylinder>`).",
            },
        ),
        Room(
            id="p2_mirror_north",
            name="Heliostat Mirror Ring (North)",
            coord=Coord3D(0, 2, 2),
            stratum=2,
            subtitle="Northern Solar Collector",
            description=(
                "A twelve-foot parabolic mirror of silvered speculum metal tracks the sun along "
                "a curved brass rail. Its hand-wheel allows it to aim its reflected beam `east`, "
                "`west`, or `center` (directly into the Prism Refraction Tower to the south)."
            ),
            exits={
                "west": Exit("west", "p2_conservatory_dome", "West to the Conservatory Central Dome."),
                "east": Exit("east", "p2_spore_condenser", "East into the Spore Condenser Lab."),
                "south": Exit("south", "p2_prism_tower", "South into the Prism Refraction Tower."),
            },
            items=[],
            features={
                "mirror_north": (
                    "The Northern Heliostat Mirror (`set mirror_north center` or `turn mirror_north`). "
                    "When aimed at `center`, it feeds concentrated sunlight into the Prism Tower."
                ),
            },
            dynamic_flag_descriptions={
                "p2_mirror_north_aligned": (
                    "\n[bold bright_green]✦ The Northern Heliostat Mirror is aimed directly at the central Prism Tower![/bold bright_green]"
                )
            },
            ambient_hint="Aim this mirror at the Prism Tower using `set mirror_north center` (or `turn mirror_north`).",
        ),
        Room(
            id="p2_spore_condenser",
            name="Spore Condenser Lab",
            coord=Coord3D(1, 2, 2),
            stratum=2,
            subtitle="Nocturne Bloom Greenhouse",
            description=(
                "Shaded by tinted cobalt glass, night-blooming Nocturne Lilies open their velvet "
                "petals around brass electrostatic pollen traps. A glittering phial of luminescent "
                "pollen rests on the harvesting tray."
            ),
            exits={
                "west": Exit("west", "p2_mirror_north", "West to the Heliostat Mirror Ring (North)."),
                "south": Exit("south", "p2_orchid_grove", "South into the Starlight Orchid Grove."),
            },
            items=["starlight_pollen"],
            features={
                "lilies": "Their anthers shimmer with silver-gold Starlight Pollen.",
            },
            ambient_hint="Take `starlight_pollen` and dust it on the giant Sun-Orchid in the grove to the south.",
        ),
        Room(
            id="p2_hydroponic_reservoir",
            name="Hydroponic Reservoir",
            coord=Coord3D(-1, 1, 2),
            stratum=2,
            subtitle="Nutrient Cascade",
            description=(
                "Glass aqueducts carry aerated mineral water through hanging gardens of silver moss. "
                "To the south, an warning sign before a hexagonal conservatory reads: 'CAUTION: "
                "CLOCKWORK APIARY — DO NOT ENTER WITHOUT SOMNUS-FERN SMOKER'."
            ),
            exits={
                "north": Exit("north", "p2_conservatory_dome", "North to the Conservatory Central Dome."),
                "east": Exit("east", "p2_prism_tower", "East into the Prism Refraction Tower."),
                "south": Exit("south", "p2_apiary", "South into the Apiary of Brass Bees."),
            },
            items=[],
            features={
                "cascade": "Feeds the roots that trail all the way down to Stratum -1.",
            },
        ),
        Room(
            id="p2_prism_tower",
            name="Prism Refraction Tower",
            coord=Coord3D(0, 1, 2),
            stratum=2,
            subtitle="Vertical Solar Collimator",
            description=(
                "At the geometric center of the Botanical Domes rises a latticework brass tower "
                "positioned directly over the Spire's vertical light-shaft. When the Gimbal-Mounted "
                "Focusing Optic is seated in the central cradle and both the North and South "
                "Heliostat Mirrors are aimed at `center`, a blazing lance of solar energy shoots "
                "down through the entire Spire!"
            ),
            exits={
                "north": Exit("north", "p2_mirror_north", "North to the Heliostat Mirror Ring (North)."),
                "west": Exit("west", "p2_hydroponic_reservoir", "West to the Hydroponic Reservoir."),
                "east": Exit("east", "p2_orchid_grove", "East to the Starlight Orchid Grove."),
                "south": Exit("south", "p2_mirror_south", "South to the Heliostat Mirror Ring (South)."),
            },
            items=[],
            features={
                "cradle": (
                    "The Collimator Optic Cradle (`use focusing_optic on cradle`). Requires the "
                    "Gimbal-Mounted Focusing Optic (`cracked_lens` + `optical_resin` + `brass_gimbal`)."
                ),
            },
            dynamic_flag_descriptions={
                "p2_solar_beam_active": (
                    "\n[bold bright_green]✦ Both Heliostats converge through the Focusing Optic! A "
                    "brilliant golden column of sunlight shoots straight down the central shaft![/bold bright_green]"
                )
            },
            ambient_hint="Install `focusing_optic` here and set both `mirror_north` and `mirror_south` to `center`.",
        ),
        Room(
            id="p2_orchid_grove",
            name="Starlight Orchid Grove",
            coord=Coord3D(1, 1, 2),
            stratum=2,
            subtitle="Crystalline Flora",
            description=(
                "In the center of a mossy rotunda grows the Sovereign Starlight Orchid—a colossal "
                "bio-alchemical flower whose translucent quartz petals are tightly closed around "
                "a gleaming golden object inside its calyx."
            ),
            exits={
                "north": Exit("north", "p2_spore_condenser", "North to the Spore Condenser Lab."),
                "west": Exit("west", "p2_prism_tower", "West to the Prism Refraction Tower."),
                "south": Exit("south", "p2_wind_organ_loft", "South into the Wind-Organ Loft."),
            },
            items=[],
            features={
                "orchid": (
                    "The Sovereign Starlight Orchid (`use starlight_pollen on orchid`). Dusting its "
                    "stigma with luminescent pollen will cause its crystalline petals to unfurl."
                ),
            },
            dynamic_flag_descriptions={
                "p2_orchid_pollinated": (
                    "\n[bold bright_green]✦ The Sovereign Starlight Orchid stands in full, radiant bloom![/bold bright_green]"
                )
            },
            ambient_hint="Use `starlight_pollen` on the `orchid` to bloom its petals and reveal the 528 Hz Tuning Fork!",
        ),
        Room(
            id="p2_apiary",
            name="Apiary of Brass Bees",
            coord=Coord3D(-1, 0, 2),
            stratum=2,
            subtitle="Clockwork Hives",
            description=(
                "Tiered hexagonal skeps of hammered copper hum with thousands of thumb-sized "
                "clockwork bees whose wings beat at ultrasonic speeds. Inside the central queen-skep "
                "glistens a comb of Gold-Spun Conducting Wax."
            ),
            exits={
                "north": Exit("north", "p2_hydroponic_reservoir", "North to the Hydroponic Reservoir."),
                "east": Exit("east", "p2_mirror_south", "East to the Heliostat Mirror Ring (South)."),
                "south": Exit("south", "p2_root_catwalk", "South onto the Hanging Root Catwalk."),
            },
            items=[],
            features={
                "hive": (
                    "The aggressive clockwork swarm guards the Gold-Spun Conducting Wax! Use the "
                    "Smoldering Somnus-Fern Smoker (`use lit_smoker on hive`) to put them into dormancy."
                ),
            },
            dynamic_flag_descriptions={
                "p2_bees_calmed": (
                    "\n[bold bright_green]✦ Lulled by the Somnus-Fern vapor, the clockwork bees "
                    "slumber peacefully in their copper combs.[/bold bright_green]"
                )
            },
            ambient_hint="Use `lit_smoker` (`empty_smoker` + `dried_dream_leaf`) on `hive` to harvest the `conducting_wax`.",
        ),
        Room(
            id="p2_mirror_south",
            name="Heliostat Mirror Ring (South)",
            coord=Coord3D(0, 0, 2),
            stratum=2,
            subtitle="Southern Solar Collector",
            description=(
                "The southern counterpart to the northern collector, this twelve-foot speculum "
                "mirror catches the high mountain sun and reflects it along a vernier arc. It can "
                "be aimed `east`, `west`, or `center` (into the Prism Tower to the north)."
            ),
            exits={
                "north": Exit("north", "p2_prism_tower", "North to the Prism Refraction Tower."),
                "west": Exit("west", "p2_apiary", "West to the Apiary of Brass Bees."),
                "east": Exit("east", "p2_wind_organ_loft", "East into the Wind-Organ Loft."),
                "south": Exit("south", "p2_elevator_lobby", "South to the Celestial Elevator Lobby."),
            },
            items=[],
            features={
                "mirror_south": (
                    "The Southern Heliostat Mirror (`set mirror_south center` or `turn mirror_south`). "
                    "Aim it at `center` to feed the Prism Refraction Tower."
                ),
            },
            dynamic_flag_descriptions={
                "p2_mirror_south_aligned": (
                    "\n[bold bright_green]✦ The Southern Heliostat Mirror is aimed directly at the central Prism Tower![/bold bright_green]"
                )
            },
            ambient_hint="Set this mirror to `center` (`set mirror_south center` or `turn mirror_south`).",
        ),
        Room(
            id="p2_wind_organ_loft",
            name="Wind-Organ Loft",
            coord=Coord3D(1, 0, 2),
            stratum=2,
            subtitle="Aeolian Pipe Gallery",
            description=(
                "Thirty-foot brass organ pipes jut through the dome roof to catch the high-altitude "
                "trade winds. An ivory keyboard console governs the Aeolian dynamo that powers the "
                "Celestial Elevator to Stratum +3. Resting in a niche beneath the pedal-board is "
                "an emerald jade Mnemonic Cylinder."
            ),
            exits={
                "north": Exit("north", "p2_orchid_grove", "North to the Starlight Orchid Grove."),
                "west": Exit("west", "p2_mirror_south", "West to the Heliostat Mirror Ring (South)."),
                "south": Exit("south", "p2_cloud_pier", "South out onto the Cloud-Pier Lookout."),
            },
            items=["cylinder_6"],
            features={
                "organ": (
                    "The Aeolian Wind-Organ console (`play CEGB` or `set organ CEGB`). According to "
                    "the Architect's Blueprint, playing the four-note major seventh chord `CEGB` "
                    "engages the Celestial Elevator dynamo."
                ),
            },
            dynamic_flag_descriptions={
                "p2_elevator_powered": (
                    "\n[bold bright_green]✦ The Wind-Organ sustains a majestic C-E-G-B chord, "
                    "energizing the Celestial Elevator to Stratum +3![/bold bright_green]"
                )
            },
            ambient_hint="Take `cylinder_6` and play the chord `play CEGB` on the Wind-Organ to power the elevator to the Observatory!",
        ),
        Room(
            id="p2_root_catwalk",
            name="Hanging Root Catwalk",
            coord=Coord3D(-1, -1, 2),
            stratum=2,
            subtitle="Under-Canopy Suspension Walk",
            description=(
                "A swaying catwalk slung beneath the glass floor of the conservatory, surrounded "
                "by mist-fed aerial roots and hanging brass planters."
            ),
            exits={
                "north": Exit("north", "p2_apiary", "North to the Apiary of Brass Bees."),
                "east": Exit("east", "p2_elevator_lobby", "East to the Celestial Elevator Lobby."),
            },
            items=[],
            features={
                "planters": "Contain rare high-altitude lichens that absorb static electricity from storm clouds.",
            },
        ),
        Room(
            id="p2_elevator_lobby",
            name="Celestial Elevator Lobby",
            coord=Coord3D(0, -1, 2),
            stratum=2,
            subtitle="Ascent to the Apex",
            description=(
                "A filigree brass-and-crystal elevator car waits inside a cylindrical glass tube "
                "that rises straight through the dome apex toward the Celestial Observatory & "
                "Resonance Crown (`Z = +3`)."
            ),
            exits={
                "north": Exit("north", "p2_mirror_south", "North to the Heliostat Mirror Ring (South)."),
                "west": Exit("west", "p2_root_catwalk", "West onto the Hanging Root Catwalk."),
                "east": Exit("east", "p2_cloud_pier", "East onto the Cloud-Pier Lookout."),
                "up": Exit(
                    "up",
                    "p3_arrival_platform",
                    "Ascend in the Celestial Glass Elevator to Stratum +3.",
                    locked=True,
                    lock_id="p2_elevator_lock",
                    lock_message=(
                        "The Celestial Elevator lacks acoustic-dynamo power! Play the chord `CEGB` "
                        "(`play CEGB`) on the Wind-Organ in the eastern loft."
                    ),
                ),
            },
            items=[],
            features={
                "elevator": "Powered by the Aeolian Wind-Organ in the eastern loft (`play CEGB`).",
                "locker": "A Pneumatic Dispatch Terminal (`stash <item>`, `retrieve <item>`, `locker`).",
            },
        ),
        Room(
            id="p2_cloud_pier",
            name="Cloud-Pier Lookout",
            coord=Coord3D(1, -1, 2),
            stratum=2,
            subtitle="Open-Air Sky Deck",
            description=(
                "An open promenade of white stone jutting out into a sea of billowing silver clouds. "
                "High above, lightning arcs silently between the twin harmonic pylons of the "
                "Observatory Crown."
            ),
            exits={
                "north": Exit("north", "p2_wind_organ_loft", "North into the Wind-Organ Loft."),
                "west": Exit("west", "p2_elevator_lobby", "West to the Celestial Elevator Lobby."),
            },
            items=["aether_capacitor"],
            features={
                "clouds": "An endless ocean of sunlit cumulus stretching to the horizon.",
            },
            ambient_hint="Take the `aether_capacitor` and combine it with `conducting_wax` from the Apiary!",
        ),
    ]
    return {r.id: r for r in rooms}
