"""Stratum 0: The Grand Clockwork Atrium & Hall of Anchors (14 Rooms, Z = 0)."""

from typing import Dict
from engine.models import Coord3D, Exit, Room


def get_rooms() -> Dict[str, Room]:
    rooms = [
        Room(
            id="z0_great_stairwell",
            name="Great Spiral Stairwell",
            coord=Coord3D(0, 2, 0),
            stratum=0,
            subtitle="Datum Horizon Landing",
            description=(
                "You emerge from the subterranean stairs into a breathtaking cathedral of polished "
                "brass, mahogany, and stained glass. A golden plaque inlaid in the marble floor "
                "reads: 'STRATUM 0 — DATUM HORIZON (0 METERS)'. To the south, giant clockwork "
                "gear-trains fill the central nave; to the west is an acoustic bell balcony; "
                "to the east, the horologists' quarters."
            ),
            exits={
                "down": Exit("down", "n1_spiral_stair", "Descend the travertine stairs to Stratum -1."),
                "south": Exit("south", "z0_north_gear_gallery", "South into the North Gear-Train Gallery."),
                "west": Exit("west", "z0_chime_balcony", "West onto the Acoustic Chime Balcony."),
                "east": Exit("east", "z0_maintainer_barracks", "East into the Maintainer's Barracks."),
            },
            items=[],
            features={
                "plaque": "Marks the exact sea-level datum dividing the subterranean foundation from the upper Spire.",
                "resonator": "An ornate gilded Mnemonic Resonator stands beside the balustrade (`play <cylinder>`).",
            },
        ),
        Room(
            id="z0_chime_balcony",
            name="Acoustic Chime Balcony",
            coord=Coord3D(-1, 2, 0),
            stratum=0,
            subtitle="Harmonic Bell Loft",
            description=(
                "Five tubular bronze carillon bells—engraved DO, RE, MI, SOL, and LA—hang above "
                "an acoustic floor grate that drops down toward the Whispering Dome on Stratum -1. "
                "Striking the bells in the proper four-note sequence unlocks the resonance seal on "
                "the Hall of the Seven Anchors."
            ),
            exits={
                "east": Exit("east", "z0_great_stairwell", "East to the Great Spiral Stairwell."),
                "south": Exit("south", "z0_pneumatic_locker_room", "South to the Central Pneumatic Locker Room."),
            },
            items=[],
            features={
                "bells": (
                    "Five tuned bronze bells: `do`, `re`, `mi`, `sol`, `la`. With the Chime Mallet in "
                    "hand, play a note using `play <note>` or `strike <note>` (e.g., `strike sol`, "
                    "`strike mi`, `strike do`, `strike la`) or all at once with `play sol mi do la`!"
                ),
            },
            ambient_hint="Find the `chime_mallet` in the Maintainer's Barracks and play the sequence heard in the Whispering Dome: `play sol mi do la`.",
        ),
        Room(
            id="z0_maintainer_barracks",
            name="Maintainer's Barracks",
            coord=Coord3D(1, 2, 0),
            stratum=0,
            subtitle="Horologists' Dormitory",
            description=(
                "Neatly made brass bedsteads and cedar footlockers line this quiet dormitory. "
                "On the watch-officer's table sit a felted rosewood mallet and half of an "
                "engraved brass cipher disc."
            ),
            exits={
                "west": Exit("west", "z0_great_stairwell", "West to the Great Spiral Stairwell."),
                "south": Exit("south", "z0_chrono_booth", "South into the Chronometer Control Booth."),
            },
            items=["chime_mallet", "torn_cipher_left"],
            features={
                "footlockers": "Contain neatly folded uniforms bearing the seven-spoked gear insignia of Aethelgard.",
            },
        ),
        Room(
            id="z0_pneumatic_locker_room",
            name="Pneumatic Locker Room",
            coord=Coord3D(-1, 1, 0),
            stratum=0,
            subtitle="Central Dispatch Exchange",
            description=(
                "The master pneumatic switching exchange of the Spire. Dozens of brass carrier "
                "tubes converge on a revolving carousel locker. Any item stashed here can be "
                "retrieved from any pneumatic terminal across the Spire (`stash <item>`, "
                "`retrieve <item>`, `locker`)."
            ),
            exits={
                "north": Exit("north", "z0_chime_balcony", "North to the Acoustic Chime Balcony."),
                "east": Exit("east", "z0_north_gear_gallery", "East into the North Gear-Train Gallery."),
                "south": Exit("south", "z0_tramway_concourse", "South to the West Tramway Concourse."),
            },
            items=["brass_gimbal"],
            features={
                "locker": (
                    "Master Pneumatic Carousel. Use `stash <item>` to store items out of your inventory, "
                    "or `retrieve <item>` to take them back."
                ),
            },
        ),
        Room(
            id="z0_north_gear_gallery",
            name="North Gear-Train Gallery",
            coord=Coord3D(0, 1, 0),
            stratum=0,
            subtitle="Primary Drive Linkage",
            description=(
                "Towering brass gear-trains transfer torque from the Vault of Weights to the "
                "Central Pendulum in the rotunda to the south. However, the drive train is "
                "halted: a primary spindle gap awaits a Heavy Beveled Escapement Gear."
            ),
            exits={
                "north": Exit("north", "z0_great_stairwell", "North to the Great Spiral Stairwell."),
                "west": Exit("west", "z0_pneumatic_locker_room", "West to the Pneumatic Locker Room."),
                "east": Exit("east", "z0_chrono_booth", "East into the Chronometer Control Booth."),
                "south": Exit("south", "z0_pendulum_rotunda", "South into the Central Pendulum Rotunda."),
            },
            items=[],
            features={
                "spindle": (
                    "An empty bronze drive shaft (`use beveled_gear on spindle`). Once fitted and "
                    "the pendulum brake is released, the Great Pendulum will resume its swing."
                ),
            },
            dynamic_flag_descriptions={
                "z0_gear_installed": (
                    "\n[bold yellow]✦ The Heavy Beveled Escapement Gear meshes cleanly on the primary spindle![/bold yellow]"
                )
            },
            ambient_hint="Install the `beveled_gear` (found in the Whispering Dome on Stratum -1) on the `spindle`.",
        ),
        Room(
            id="z0_chrono_booth",
            name="Chronometer Control Booth",
            coord=Coord3D(1, 1, 0),
            stratum=0,
            subtitle="Epoch Synchronizer",
            description=(
                "A glass-walled control booth overlooking the Atrium. Its mahogany console houses "
                "a four-wheel brass thumb-dial labeled 'EPOCH SYNCHRONIZER (0000–9999)'. Setting "
                "the proper four-digit code aligns the spiral stair lock to the Mnemonic Archives."
            ),
            exits={
                "north": Exit("north", "z0_maintainer_barracks", "North to the Maintainer's Barracks."),
                "west": Exit("west", "z0_north_gear_gallery", "West to the North Gear-Train Gallery."),
                "south": Exit("south", "z0_cartographer_wing", "South into the East Cartographer's Wing."),
            },
            items=[],
            features={
                "dial": (
                    "A four-wheel brass number dial (`dial <4-digit-code>` or `set dial <code>`). "
                    "Check the Chronometer Calibration Plaque in the Cartographer's Wing for the code."
                ),
            },
            dynamic_flag_descriptions={
                "z0_chrono_unlocked": (
                    "\n[bold yellow]✦ The Chronometer Dial clicks to 4719! Green synchronization lamps illuminate.[/bold yellow]"
                )
            },
            ambient_hint="Read the plaque in the Cartographer's Wing south of here, then enter `dial 4719`.",
        ),
        Room(
            id="z0_broken_bridge_west",
            name="Western Cantilever Span",
            coord=Coord3D(-2, 0, 0),
            stratum=0,
            subtitle="Outer Chasm Overlook",
            description=(
                "Out on the extended cantilever span, cold drafts swirl around the outer curtain "
                "wall of the Spire. Resting on a maintenance pedestal is a heavy 15-kg Lead "
                "Trim-Weight and a silver-copper cartridge fuse."
            ),
            exits={
                "east": Exit("east", "z0_tramway_concourse", "East back to the West Tramway Concourse."),
            },
            items=["lead_counterweight", "copper_fuse"],
            features={
                "overlook": "Through narrow lancet windows you see subterranean lightning flickering in the chasm.",
            },
        ),
        Room(
            id="z0_tramway_concourse",
            name="West Tramway Concourse",
            coord=Coord3D(-1, 0, 0),
            stratum=0,
            subtitle="Cantilever Drawbridge Station",
            description=(
                "A vaulted station platform bordering a deep interior drop. To the west, a "
                "retractable cantilever bridge leads to an outer equipment span, but its draw-chain "
                "is missing a coupler shackle. To the south lies the Vault of Weights."
            ),
            exits={
                "north": Exit("north", "z0_pneumatic_locker_room", "North to the Pneumatic Locker Room."),
                "east": Exit("east", "z0_pendulum_rotunda", "East into the Central Pendulum Rotunda."),
                "south": Exit("south", "z0_vault_of_weights", "South into the Vault of Weights."),
                "west": Exit(
                    "west",
                    "z0_broken_bridge_west",
                    "West onto the extended Cantilever Span.",
                    locked=True,
                    lock_id="west_bridge_lock",
                    unlock_item_id="repaired_coupler",
                    consume_key=True,
                    lock_message=(
                        "The western cantilever bridge is retracted! Its draw-winch is missing a "
                        "Pinned Tramway Coupler Shackle (`use repaired_coupler on west`)."
                    ),
                    unlock_message=(
                        "You fit the Pinned Tramway Coupler Shackle onto the draw-chain and haul the "
                        "lever! The Western Cantilever Span locks into place!"
                    ),
                ),
            },
            items=[],
            features={
                "winch": "Requires a Pinned Tramway Coupler Shackle (`broken_coupler` + `meteoric_pin`) or `pull bridge` if coupled.",
            },
            ambient_hint="Craft `repaired_coupler` (`broken_coupler` + `meteoric_pin`) and `use repaired_coupler on west` to reach the Lead Trim-Weight.",
        ),
        Room(
            id="z0_pendulum_rotunda",
            name="Central Pendulum Rotunda",
            coord=Coord3D(0, 0, 0),
            stratum=0,
            subtitle="The Heart of Aethelgard",
            description=(
                "You stand upon a circular brass gallery at exact coordinates (0, 0, 0). "
                "Suspended from the Spire's apex is the ten-ton Foucault Pendulum, designed to "
                "stabilize the temporal fault below. A spiral staircase coils upward around the "
                "pendulum cable toward the Mnemonic Archives (`Z = +1`), gated by an escapement "
                "interlock that opens only when the Pendulum is swinging and the Chronometer is set."
            ),
            exits={
                "north": Exit("north", "z0_north_gear_gallery", "North to the North Gear-Train Gallery."),
                "west": Exit("west", "z0_tramway_concourse", "West to the West Tramway Concourse."),
                "east": Exit("east", "z0_cartographer_wing", "East to the Cartographer's Wing."),
                "south": Exit("south", "z0_south_escapement", "South to the South Escapement Hall."),
                "up": Exit(
                    "up",
                    "p1_archive_rotunda",
                    "Ascend the Pendulum Stair to Stratum +1 (The Mnemonic Archives).",
                    locked=True,
                    lock_id="z0_pendulum_stair_lock",
                    lock_message=(
                        "The Archive Stair interlock is engaged! To unlock it, the Central Pendulum "
                        "must be swinging (install the Beveled Gear in the North Gallery, hang the "
                        "Lead Trim-Weight in the Vault of Weights, and release the brake in the South "
                        "Escapement) AND the Chronometer Dial must be set to `4719`."
                    ),
                ),
            },
            items=[],
            features={
                "pendulum": "A gleaming ten-ton sphere of gilded bronze hanging over a degree-marked floor rose.",
                "aperture": "A central crystal bullseye in the floor lets the vertical solar beam pass down to Stratum -3.",
            },
            dynamic_flag_descriptions={
                "z0_pendulum_running": (
                    "\n[bold yellow]✦ The Foucault Pendulum swings in majestic twelve-second arcs, "
                    "sending a stabilizing heartbeat through the entire Spire![/bold yellow]"
                )
            },
        ),
        Room(
            id="z0_cartographer_wing",
            name="East Cartographer's Wing",
            coord=Coord3D(1, 0, 0),
            stratum=0,
            subtitle="Hall of Elevation Models",
            description=(
                "Scale wireframe models of all seven strata hang from the coffered ceiling. "
                "Drafting tables display cross-sectional blueprints of the central solar shaft. "
                "To the east, glass doors open onto the Sun-Shaft Balcony; to the south stands "
                "the sealed portal of the Hall of the Seven Anchors."
            ),
            exits={
                "north": Exit("north", "z0_chrono_booth", "North to the Chronometer Control Booth."),
                "west": Exit("west", "z0_pendulum_rotunda", "West to the Central Pendulum Rotunda."),
                "east": Exit("east", "z0_sun_shaft_balcony", "East onto the Sun-Shaft Balcony."),
                "south": Exit(
                    "south",
                    "z0_hall_of_anchors",
                    "South into the Hall of the Seven Anchors.",
                    locked=True,
                    lock_id="anchor_hall_lock",
                    lock_message=(
                        "The acoustic lock on the Hall of Anchors is sealed! Strike the four-note "
                        "melody (`play sol mi do la`) on the Acoustic Chime Balcony using the Chime Mallet."
                    ),
                ),
            },
            items=["chronometer_plaque"],
            features={
                "models": "Wireframe models showing how the solar beam from Stratum +2 passes through Stratum 0 down to Stratum -3.",
            },
            ambient_hint="Read `chronometer_plaque` to learn the 4-digit Chronometer code (`4719`).",
        ),
        Room(
            id="z0_sun_shaft_balcony",
            name="Sun-Shaft Balcony",
            coord=Coord3D(2, 0, 0),
            stratum=0,
            subtitle="Optical Collimator Shutter",
            description=(
                "A semicircular brass balcony projecting into the vertical light-well. Mounted on "
                "the railing is the manual Shutter Lever that opens or closes the iris aperture "
                "between the upper Spire and the subterranean chasm."
            ),
            exits={
                "west": Exit("west", "z0_cartographer_wing", "West into the East Cartographer's Wing."),
            },
            items=["torn_cipher_right"],
            features={
                "shutter": (
                    "The Iris Shutter Lever (`pull shutter` or `open shutter`). Opening this shutter "
                    "is essential so the solar beam from the Botanical Domes (`Z = +2`) can reach the "
                    "Abyssal Solar Core (`Z = -3`)."
                ),
            },
            dynamic_flag_descriptions={
                "z0_shutter_open": (
                    "\n[bold yellow]✦ The massive brass iris shutter is wide open, giving a clear "
                    "vertical line of sight from the upper domes to the Abyss below![/bold yellow]"
                )
            },
            ambient_hint="Pull the shutter lever (`pull shutter`) to open the vertical light-well aperture, and take the right cipher half.",
        ),
        Room(
            id="z0_vault_of_weights",
            name="Vault of Weights",
            coord=Coord3D(-1, -1, 0),
            stratum=0,
            subtitle="Gravity Drive Chamber",
            description=(
                "Heavy chains descend through floor sheaves to drive the Atrium's clockwork. "
                "The primary weight cradle is nearly balanced, lacking only a 15-kg Lead Trim-Weight "
                "to bring the drive train to proper tension."
            ),
            exits={
                "north": Exit("north", "z0_tramway_concourse", "North to the West Tramway Concourse."),
                "east": Exit("east", "z0_south_escapement", "East to the South Escapement Hall."),
            },
            items=[],
            features={
                "cradle": (
                    "The Gravity Drive Weight Cradle (`use lead_counterweight on cradle`). "
                    "Requires the 15-kg Lead Trim-Weight from the Western Cantilever Span."
                ),
            },
            dynamic_flag_descriptions={
                "z0_weights_balanced": (
                    "\n[bold yellow]✦ The 15-kg Lead Trim-Weight hangs on the cradle, supplying full torque to the escapement![/bold yellow]"
                )
            },
        ),
        Room(
            id="z0_south_escapement",
            name="South Escapement Hall",
            coord=Coord3D(0, -1, 0),
            stratum=0,
            subtitle="Pendulum Brake Anchor",
            description=(
                "Here a massive deadbeat anchor escapement ticks—or waits to tick—against the "
                "pendulum's impulse pallet. A heavy iron Brake Lever clamps the pendulum shaft. "
                "To the east is the bronze side-door of the Hall of the Seven Anchors."
            ),
            exits={
                "north": Exit("north", "z0_pendulum_rotunda", "North to the Central Pendulum Rotunda."),
                "west": Exit("west", "z0_vault_of_weights", "West to the Vault of Weights."),
                "east": Exit(
                    "east",
                    "z0_hall_of_anchors",
                    "East into the Hall of the Seven Anchors.",
                    locked=True,
                    lock_id="anchor_hall_lock",
                    lock_message="The acoustic resonance lock on the Hall of Anchors is still engaged (`play sol mi do la` on the Chime Balcony).",
                ),
            },
            items=[],
            features={
                "brake": (
                    "The Pendulum Brake Lever (`pull brake` or `release brake`). Once the Beveled "
                    "Gear is installed in the North Gallery and the Lead Trim-Weight is hung in the "
                    "Vault of Weights, pulling this brake starts the Great Pendulum!"
                ),
            },
            ambient_hint="After installing the gear and hanging the weight, `pull brake` here to start the Great Pendulum.",
        ),
        Room(
            id="z0_hall_of_anchors",
            name="Hall of the Seven Anchors",
            coord=Coord3D(1, -1, 0),
            stratum=0,
            subtitle="Sanctum of the Architect",
            description=(
                "Seven marble plinths stand in a horseshoe around a sunken astrolabe mosaic, "
                "representing the seven strata of Aethelgard. Upon the fourth central plinth "
                "gleams a gilded brass Mnemonic Cylinder."
            ),
            exits={
                "north": Exit("north", "z0_cartographer_wing", "North to the East Cartographer's Wing."),
                "west": Exit("west", "z0_south_escapement", "West to the South Escapement Hall."),
            },
            items=["cylinder_4"],
            features={
                "plinths": "Each plinth shows the status of its stratum's mechanical and harmonic systems.",
            },
            ambient_hint="Take `cylinder_4` and play it on a Resonator (`play cylinder 4`).",
        ),
    ]
    return {r.id: r for r in rooms}
