"""Stratum +3: The Celestial Observatory & Resonance Crown (11 Rooms, Z = +3)."""

from typing import Dict
from engine.models import Coord3D, Exit, Room


def get_rooms() -> Dict[str, Room]:
    rooms = [
        Room(
            id="p3_arrival_platform",
            name="Observatory Arrival Platform",
            coord=Coord3D(0, -1, 3),
            stratum=3,
            subtitle="Five Hundred Meters Above Datum",
            description=(
                "The glass elevator opens onto a windswept rotunda of silvered steel and star-phire "
                "crystal, five hundred meters above the datum horizon and nearly a kilometer above "
                "the Awakening Slab where your journey began. Above you arches the open sky of "
                "twilight and aurora. Northward spans the Zenith Glass Bridge; west lies the "
                "Star-Charting Rotunda; east are your private Architect's Quarters."
            ),
            exits={
                "down": Exit("down", "p2_elevator_lobby", "Descend in the Celestial Glass Elevator to Stratum +2."),
                "north": Exit("north", "p3_zenith_bridge", "North onto the Zenith Glass Bridge."),
                "west": Exit("west", "p3_star_chart_rotunda", "West into the Star-Charting Rotunda."),
                "east": Exit("east", "p3_architect_quarters", "East into the Architect's Living Quarters."),
            },
            items=[],
            features={
                "resonator": "A platinum-and-diamond Mnemonic Resonator stands on an astral plinth (`play <cylinder>`).",
                "locker": "The Apex Pneumatic Dispatch Terminal (`stash <item>`, `retrieve <item>`, `locker`).",
            },
        ),
        Room(
            id="p3_star_chart_rotunda",
            name="Star-Charting Rotunda",
            coord=Coord3D(-1, -1, 3),
            stratum=3,
            subtitle="Celestial Cartography Hall",
            description=(
                "Armillary spheres and brass planispheres hang suspended from silk threads. "
                "On the central charting table rests a Perforated Brass Star-Chart Disc etched "
                "with the Zenith alignment coordinates."
            ),
            exits={
                "east": Exit("east", "p3_arrival_platform", "East to the Observatory Arrival Platform."),
                "north": Exit("north", "p3_astrolabe_deck", "North onto the Astrolabe Calibration Deck."),
            },
            items=["star_chart_overlay"],
            features={
                "planispheres": "Confirm that the Zenith Alignment is Azimuth 240, Altitude 65.",
            },
            ambient_hint="Read `star_chart_overlay` (`read star chart`) to confirm the Astrolabe settings: Azimuth 240, Altitude 65.",
        ),
        Room(
            id="p3_architect_quarters",
            name="Architect's Living Quarters",
            coord=Coord3D(1, -1, 3),
            stratum=3,
            subtitle="Sanctuary of Vaelen Korr",
            description=(
                "A quiet, book-lined study that feels piercingly familiar—because it was your home. "
                "A cold cup of tea still sits beside an open farewell letter on your writing desk, "
                "next to your platinum Sovereign Ring and the seventh, final Mnemonic Cylinder."
            ),
            exits={
                "west": Exit("west", "p3_arrival_platform", "West to the Observatory Arrival Platform."),
                "north": Exit("north", "p3_telescope_dome", "North into the Equatorial Telescope Dome."),
            },
            items=["architect_signet", "cylinder_7"],
            features={
                "desk": (
                    "Your handwritten farewell note reads: 'If you are standing here, my gambit "
                    "succeeded. Take your Sovereign Ring and Cylinder VII. Align the Astrolabe "
                    "(240 / 65), tune the West Pylon (432 Hz) and East Pylon (528 Hz), charge the "
                    "Leyden Capacitor at the Lightning Spire, and enter the Resonance Crown.'"
                ),
            },
            ambient_hint="Take `architect_signet` and `cylinder_7`, and play `cylinder_7` at a Resonator!",
        ),
        Room(
            id="p3_astrolabe_deck",
            name="Astrolabe Calibration Deck",
            coord=Coord3D(-1, 0, 3),
            stratum=3,
            subtitle="Great Armillary Ring",
            description=(
                "A twenty-foot bronze armillary astrolabe juts out over the western precipice. "
                "Two graduated vernier handwheels set its `azimuth` (0–360°) and `altitude` (0–90°)."
            ),
            exits={
                "south": Exit("south", "p3_star_chart_rotunda", "South to the Star-Charting Rotunda."),
                "east": Exit("east", "p3_zenith_bridge", "East onto the Zenith Glass Bridge."),
                "north": Exit("north", "p3_west_pylon", "North to the West Harmonic Pylon."),
            },
            items=[],
            features={
                "astrolabe": (
                    "The Great Celestial Astrolabe (`set azimuth 240` and `set altitude 65`, or "
                    "`set astrolabe 240 65`)."
                ),
            },
            dynamic_flag_descriptions={
                "p3_astrolabe_aligned": (
                    "\n[bold sky_blue1]✦ Locked at Azimuth 240°, Altitude 65°, the Great Astrolabe "
                    "projects a beam of starlight onto the Crown lock![/bold sky_blue1]"
                )
            },
            ambient_hint="Align the Astrolabe using `set azimuth 240` and `set altitude 65` (or `set astrolabe 240 65`).",
        ),
        Room(
            id="p3_zenith_bridge",
            name="Zenith Glass Bridge",
            coord=Coord3D(0, 0, 3),
            stratum=3,
            subtitle="Axis Mundi Span",
            description=(
                "A bridge of three-inch-thick transparent quartz spans the central core of the "
                "Spire. Looking straight down between your boots, you can see all the way through "
                "the Botanical Prism Tower and the Clockwork Pendulum Rotunda to the Abyssal Solar "
                "Core seven hundred meters below! Ahead to the north stands the sealed door of the "
                "Memory Core Antechamber."
            ),
            exits={
                "south": Exit("south", "p3_arrival_platform", "South to the Observatory Arrival Platform."),
                "west": Exit("west", "p3_astrolabe_deck", "West to the Astrolabe Calibration Deck."),
                "east": Exit("east", "p3_telescope_dome", "East into the Equatorial Telescope Dome."),
                "north": Exit(
                    "north",
                    "p3_core_antechamber",
                    "North into the Memory Core Antechamber.",
                    locked=True,
                    lock_id="architect_signet_lock",
                    unlock_item_id="architect_signet",
                    lock_message=(
                        "The Antechamber portal bears the depressed signet bezel of the Chief "
                        "Architect (`use architect_signet on north`)."
                    ),
                    unlock_message=(
                        "You press Vaelen Korr's Master Sovereign Ring into the bezel! Silver "
                        "filigree bolts retract, and the Antechamber doors part silently."
                    ),
                ),
            },
            items=[],
            features={
                "glass_floor": "Provides a breathtaking vertical view down the entire seven-stratum axis.",
            },
            ambient_hint="Unlock the northern door with `architect_signet` (`use architect_signet on north`).",
        ),
        Room(
            id="p3_telescope_dome",
            name="Equatorial Telescope Dome",
            coord=Coord3D(1, 0, 3),
            stratum=3,
            subtitle="Great Refractor Hall",
            description=(
                "A revolving copper dome houses a forty-foot brass refracting telescope aimed "
                "at the aurora-draped zenith. Catwalks lead north to the East Harmonic Pylon and "
                "east out onto the exposed Lightning Rod Spire."
            ),
            exits={
                "south": Exit("south", "p3_architect_quarters", "South to the Architect's Living Quarters."),
                "west": Exit("west", "p3_zenith_bridge", "West onto the Zenith Glass Bridge."),
                "north": Exit("north", "p3_east_pylon", "North to the East Harmonic Pylon."),
                "east": Exit("east", "p3_lightning_spire", "East out onto the Lightning Rod Spire."),
            },
            items=[],
            features={
                "telescope": "Through the eyepiece, you see temporal ripples shimmering in the upper atmosphere.",
            },
        ),
        Room(
            id="p3_lightning_spire",
            name="Lightning Rod Spire",
            coord=Coord3D(2, 0, 3),
            stratum=3,
            subtitle="Storm-Capture Outrigger",
            description=(
                "A narrow copper gangway juts out into the crackling storm-collar encircling the "
                "Spire's peak. St. Elmo's fire dances along a twenty-foot platinum lightning rod "
                "fitted with an accumulator cradle at its base."
            ),
            exits={
                "west": Exit("west", "p3_telescope_dome", "West back inside the Equatorial Telescope Dome."),
            },
            items=[],
            features={
                "rod": (
                    "The Platinum Lightning Rod (`use waxed_capacitor on rod`). Requires a "
                    "Conducting-Sealed Leyden Capacitor (`aether_capacitor` + `conducting_wax`)."
                ),
            },
            ambient_hint="Combine `aether_capacitor` + `conducting_wax`, then `use waxed_capacitor on rod` to capture a lightning bolt!",
        ),
        Room(
            id="p3_west_pylon",
            name="West Harmonic Pylon",
            coord=Coord3D(-1, 1, 3),
            stratum=3,
            subtitle="Veridian Resonance Tower",
            description=(
                "A thirty-foot tuning tower of veridian-patinated bronze hums against the wind. "
                "At its base is a frequency resonator slot stamped 'WEST PYLON — TARGET: 432 HZ'."
            ),
            exits={
                "south": Exit("south", "p3_astrolabe_deck", "South to the Astrolabe Calibration Deck."),
                "east": Exit("east", "p3_core_antechamber", "East into the Memory Core Antechamber."),
            },
            items=[],
            features={
                "pylon_west": (
                    "The West Harmonic Pylon (`use tuning_fork_432 on pylon` or `set west_pylon 432`)."
                ),
            },
            dynamic_flag_descriptions={
                "p3_west_pylon_tuned": (
                    "\n[bold sky_blue1]✦ The West Harmonic Pylon sings at a pure, unwavering 432 Hz![/bold sky_blue1]"
                )
            },
            ambient_hint="Use `tuning_fork_432` on the pylon (or `set west_pylon 432`).",
        ),
        Room(
            id="p3_core_antechamber",
            name="Memory Core Antechamber",
            coord=Coord3D(0, 1, 3),
            stratum=3,
            subtitle="Threshold of the Chorister",
            description=(
                "A solemn chamber of white alabaster and silver bus-bars. Flanking passages lead "
                "west and east to the twin Harmonic Pylons. Directly ahead to the north stands the "
                "triple-sealed blast portal of the Resonance Crown, beside a high-voltage Capacitor "
                "Receptacle."
            ),
            exits={
                "south": Exit("south", "p3_zenith_bridge", "South onto the Zenith Glass Bridge."),
                "west": Exit("west", "p3_west_pylon", "West to the West Harmonic Pylon."),
                "east": Exit("east", "p3_east_pylon", "East to the East Harmonic Pylon."),
                "north": Exit(
                    "north",
                    "p3_resonance_crown",
                    "North into the Resonance Crown (Apex).",
                    locked=True,
                    lock_id="crown_apex_lock",
                    lock_message=(
                        "The Resonance Crown portal requires three conditions: (1) Great Astrolabe "
                        "aligned to 240 / 65, (2) West Pylon tuned to 432 Hz & East Pylon tuned to "
                        "528 Hz, and (3) Storm-Charged Aether Capacitor inserted into the receptacle here "
                        "(`use charged_capacitor on receptacle`)."
                    ),
                ),
            },
            items=[],
            features={
                "receptacle": (
                    "High-Voltage Capacitor Receptacle (`use charged_capacitor on receptacle`)."
                ),
            },
            dynamic_flag_descriptions={
                "p3_core_unlocked": (
                    "\n[bold bright_white]✦ With the Astrolabe aligned, both Pylons synchronized, "
                    "and the Storm-Charged Capacitor discharging into the bus-bars, the northern "
                    "portal to the Resonance Crown stands wide open![/bold bright_white]"
                )
            },
            ambient_hint="Ensure the Astrolabe is at 240/65, both Pylons are tuned (432 Hz & 528 Hz), and `use charged_capacitor on receptacle`!",
        ),
        Room(
            id="p3_east_pylon",
            name="East Harmonic Pylon",
            coord=Coord3D(1, 1, 3),
            stratum=3,
            subtitle="Golden Resonance Tower",
            description=(
                "A thirty-foot tuning tower of gilded bell-metal stands opposite its western "
                "twin. Its acoustic cradle is stamped 'EAST PYLON — TARGET: 528 HZ'."
            ),
            exits={
                "south": Exit("south", "p3_telescope_dome", "South to the Equatorial Telescope Dome."),
                "west": Exit("west", "p3_core_antechamber", "West into the Memory Core Antechamber."),
            },
            items=[],
            features={
                "pylon_east": (
                    "The East Harmonic Pylon (`use tuning_fork_528 on pylon` or `set east_pylon 528`)."
                ),
            },
            dynamic_flag_descriptions={
                "p3_east_pylon_tuned": (
                    "\n[bold sky_blue1]✦ The East Harmonic Pylon resonates at a brilliant 528 Hz![/bold sky_blue1]"
                )
            },
            ambient_hint="Use `tuning_fork_528` (from the Starlight Orchid on Stratum +2) on the pylon (or `set east_pylon 528`).",
        ),
        Room(
            id="p3_resonance_crown",
            name="The Resonance Crown (Apex)",
            coord=Coord3D(0, 2, 3),
            stratum=3,
            subtitle="Heart of the Chorister",
            description=(
                "You stand at the highest pinnacle of the Aethelgard Spire beneath an open vault "
                "of stars. Rising before you is the Chorister—a breathtaking concentric sphere of "
                "spinning brass rings, crystal pipes, and silver harmonic strings. At its heart "
                "is the Seven-Slotted Mnemonic Core Drum, waiting to receive the Crystalline "
                "Memory Cylinders of Vaelen Korr."
            ),
            exits={
                "south": Exit("south", "p3_core_antechamber", "South to the Memory Core Antechamber."),
            },
            items=[],
            features={
                "core": (
                    "The Chorister's Mnemonic Core Drum. You can insert individual cylinders "
                    "(`use cylinder_1 on core`) or all carried cylinders at once (`insert cylinders`), "
                    "and then trigger the final resolution with `activate core`!"
                ),
                "chorister": (
                    "A polyphonic voice like a choir of glass bells whispers: 'ARCHITECT KORR. "
                    "INSERT YOUR MEMORIES AND CHOOSE OUR FATE (`activate core`).'"
                ),
            },
            ambient_hint="Use `insert cylinders` (or `use <cylinder> on core`) and then `activate core` to complete your journey!",
        ),
    ]
    return {r.id: r for r in rooms}
