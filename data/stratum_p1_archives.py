"""Stratum +1: The Mnemonic Archives & Scriptorium (13 Rooms, Z = +1)."""

from typing import Dict
from engine.models import Coord3D, Exit, Room


def get_rooms() -> Dict[str, Room]:
    rooms = [
        Room(
            id="p1_archive_rotunda",
            name="Archive Rotunda",
            coord=Coord3D(0, 0, 1),
            stratum=1,
            subtitle="The Hall of Crystalline Memory",
            description=(
                "Spiral iron stairs deliver you into a soaring octagonal library lit by violet "
                "clerestory windows. Three-story walnut bookshelves and brass cylinder racks radiate "
                "toward the four cardinal points. In the center of the rotunda, the pendulum cable "
                "passes silently through a velvet-lined floor well."
            ),
            exits={
                "down": Exit("down", "z0_pendulum_rotunda", "Descend the Pendulum Stair to Stratum 0."),
                "north": Exit("north", "p1_north_stacks", "North into the History Stacks."),
                "south": Exit("south", "p1_south_stacks", "South into the Alchemy & Restoration Stacks."),
                "east": Exit("east", "p1_east_stacks", "East into the Optics & Acoustics Stacks."),
                "west": Exit("west", "p1_west_stacks", "West into the Forbidden Index Stacks."),
            },
            items=[],
            features={
                "resonator": "The Master Archival Resonator sits on an inlaid lectern (`play <cylinder>`).",
                "directory": (
                    "A brass directory plaque: 'NORTH: History & Cipher Rotunda | SOUTH: Restoration "
                    "Lab & Listening Booths | EAST: Acoustic Loom | WEST: Curator's Study & Index'."
                ),
            },
        ),
        Room(
            id="p1_south_stacks",
            name="South Stacks (Alchemy & Material Arts)",
            coord=Coord3D(0, -1, 1),
            stratum=1,
            subtitle="Folio Aisles",
            description=(
                "Tall shelves bound in tooled morocco leather smell of beeswax and aged vellum. "
                "To the east, violet light flickers from the Parchment Restoration Lab; to the "
                "west, soundproofed booths line a carpeted corridor."
            ),
            exits={
                "north": Exit("north", "p1_archive_rotunda", "North to the Archive Rotunda."),
                "east": Exit("east", "p1_restoration_lab", "East into the Parchment Restoration Lab."),
                "west": Exit("west", "p1_listening_booths", "West to the Phonograph Listening Booths."),
            },
            items=["dried_dream_leaf"],
            features={
                "herbarium": (
                    "An open botanical folio preserves pressed fronds of Somnus-Fern ('Used by "
                    "Botanical Dome apiarists to pacify clockwork bees')."
                ),
            },
        ),
        Room(
            id="p1_restoration_lab",
            name="Parchment Restoration Lab",
            coord=Coord3D(1, -1, 1),
            stratum=1,
            subtitle="Ultraviolet Inspection Studio",
            description=(
                "Slanted glass light-tables and humidifying trays fill this conservation studio. "
                "Mounted over the central bench is a hooded Ultraviolet Restoration Lamp used to "
                "read sympathetic cobalt inks—though its socket requires a Quartz-Mercury Vapor Bulb."
            ),
            exits={
                "west": Exit("west", "p1_south_stacks", "West to the South Stacks."),
                "north": Exit("north", "p1_east_stacks", "North into the East Stacks."),
            },
            items=[],
            features={
                "restoration_lamp": (
                    "An ultraviolet inspection hood (`use uv_bulb on lamp`, then `use blank_blueprint on lamp`, "
                    "or simply `combine blank_blueprint with uv_bulb` here)."
                ),
            },
            ambient_hint="Combine `blank_blueprint` with `uv_bulb` here (or `use uv_bulb on lamp`) to reveal the Architect's hidden schematic!",
        ),
        Room(
            id="p1_listening_booths",
            name="Phonograph Listening Booths",
            coord=Coord3D(-1, -1, 1),
            stratum=1,
            subtitle="Auditory Carrels",
            description=(
                "Velvet-draped acoustic carrels allow scholars to play back wax and quartz cylinders "
                "in private. In the third booth sits a spare Quartz-Mercury Vapor Bulb inside a "
                "padded velvet case."
            ),
            exits={
                "east": Exit("east", "p1_south_stacks", "East to the South Stacks."),
                "north": Exit("north", "p1_west_stacks", "North into the West Stacks."),
            },
            items=["uv_bulb"],
            features={
                "resonator": "A high-fidelity carrel Resonator (`play <cylinder>`).",
                "carrels": "Soundproofed with quilted horsehair and perforated brass panels.",
            },
        ),
        Room(
            id="p1_east_stacks",
            name="East Stacks (Optics & Harmonics)",
            coord=Coord3D(1, 0, 1),
            stratum=1,
            subtitle="Treatises on Light & Sound",
            description=(
                "Copper-plate engravings of heliostat mirrors and tuning forks hang between the "
                "bookcases. A staircase at the northern end leads into the rhythmic clicking of "
                "the Acoustic Loom Chamber."
            ),
            exits={
                "west": Exit("west", "p1_archive_rotunda", "West to the Archive Rotunda."),
                "south": Exit("south", "p1_restoration_lab", "South to the Parchment Restoration Lab."),
                "north": Exit("north", "p1_acoustic_loom", "North into the Acoustic Loom Chamber."),
            },
            items=[],
            features={
                "engravings": (
                    "One diagram reads: 'To awaken the Abyssal Solar Core, set both North and South "
                    "Heliostat Mirrors on Stratum +2 to CENTER, install the Focusing Optic in the "
                    "Prism Tower, and ensure the Atrium Shutter on Stratum 0 is OPEN.'"
                ),
            },
        ),
        Room(
            id="p1_west_stacks",
            name="West Stacks (The Forbidden Index)",
            coord=Coord3D(1 * -1, 0, 1),
            stratum=1,
            subtitle="Restricted Catalog",
            description=(
                "Chained folios and lead-sealed scroll cases line this shadowed aisle. Along the "
                "western wall stands a floor-to-ceiling bookcase whose central shelf holds a "
                "curiously unchained volume titled 'Treatise on Oblivion'."
            ),
            exits={
                "east": Exit("east", "p1_archive_rotunda", "East to the Archive Rotunda."),
                "south": Exit("south", "p1_listening_booths", "South to the Phonograph Listening Booths."),
                "north": Exit("north", "p1_curator_study", "North into the Curator's Private Study."),
                "west": Exit(
                    "west",
                    "p1_secret_vault",
                    "Through the pivoted bookcase into the Secret Vault.",
                    locked=True,
                    hidden=True,
                    lock_id="secret_bookcase_lock",
                    lock_message="Only a solid wall of bookshelves is visible to the west.",
                ),
            },
            items=[],
            features={
                "bookcase": (
                    "Among the chained tomes stands a heavy spine titled 'Treatise on Oblivion' "
                    "(`pull book` or `pull treatise`)."
                ),
                "treatise": "The spine is hinged to a hidden brass counter-latch (`pull treatise`).",
            },
            dynamic_flag_descriptions={
                "p1_secret_index_open": (
                    "\n[bold orchid1]✦ The western bookcase has swung open on concealed pivots, "
                    "revealing a passage `west` into the Secret Vault![/bold orchid1]"
                )
            },
            ambient_hint="Pull the 'Treatise on Oblivion' (`pull treatise` or `pull book`) to open the secret bookcase to the west!",
        ),
        Room(
            id="p1_secret_vault",
            name="Secret Vault behind the Index",
            coord=Coord3D(-2, 0, 1),
            stratum=1,
            subtitle="Architect's Hidden Depository",
            description=(
                "A windowless stone strongroom hidden behind the false bookcase. In the center "
                "stands a velvet-lined reliquary holding an amethyst Mnemonic Cylinder and a "
                "calibrated 432 Hz Harmonic Tuning Fork."
            ),
            exits={
                "east": Exit("east", "p1_west_stacks", "East through the pivoted bookcase to the West Stacks."),
            },
            items=["cylinder_5", "tuning_fork_432"],
            features={
                "reliquary": "Inscribed: 'MEMORY ANCHOR V — THE CORRUPTION OF THE LOGIC LOOM'.",
            },
            ambient_hint="Take `cylinder_5` and `tuning_fork_432`!",
        ),
        Room(
            id="p1_north_stacks",
            name="North Stacks (Annals of the Spire)",
            coord=Coord3D(0, 1, 1),
            stratum=1,
            subtitle="Chronicle Alcoves",
            description=(
                "Marble busts of previous Spire Curators gaze down upon glass display cases "
                "chronicling three decades of subterranean stabilization. Northward, a bronze "
                "archway opens into the Cipher Rotunda."
            ),
            exits={
                "south": Exit("south", "p1_archive_rotunda", "South to the Archive Rotunda."),
                "east": Exit("east", "p1_acoustic_loom", "East into the Acoustic Loom Chamber."),
                "west": Exit("west", "p1_curator_study", "West into the Curator's Private Study."),
                "north": Exit("north", "p1_cipher_rotunda", "North into the Cipher Rotunda."),
            },
            items=[],
            features={
                "busts": "The final plinth bears your own likeness: 'VAELEN KORR — CHIEF MNEMONIC ARCHITECT'.",
            },
        ),
        Room(
            id="p1_acoustic_loom",
            name="Acoustic Loom Chamber",
            coord=Coord3D(1, 1, 1),
            stratum=1,
            subtitle="Jacquard Memory Weaver",
            description=(
                "A room-sized mechanical loom weaves perforated brass punch-cards and phosphor-bronze "
                "wires, translating sound waves into physical grooves on quartz cylinders. A "
                "resonance calibration fork-mount on its side awaits a 432 Hz reference pitch."
            ),
            exits={
                "south": Exit("south", "p1_east_stacks", "South to the East Stacks."),
                "west": Exit("west", "p1_north_stacks", "West to the North Stacks."),
                "north": Exit("north", "p1_upper_gallery", "North to the Upper Gallery Overlook."),
            },
            items=[],
            features={
                "loom": (
                    "The Jacquard Memory Weaver. Use `tuning_fork_432` on the `loom` (`use tuning_fork_432 on loom`) "
                    "to synchronize its harmonic read-head."
                ),
            },
            dynamic_flag_descriptions={
                "p1_loom_tuned": (
                    "\n[bold orchid1]✦ Tuned to 432 Hz, the Acoustic Loom purrs in perfect harmony![/bold orchid1]"
                )
            },
        ),
        Room(
            id="p1_curator_study",
            name="Curator's Private Study",
            coord=Coord3D(-1, 1, 1),
            stratum=1,
            subtitle="Sanctum of Mnemos",
            description=(
                "A circular study panelled in bog-oak. A celestial globe stands beside an ornate "
                "partner's desk where a rolled vellum blueprint rests under a brass paperweight. "
                "To the north lies the Paternoster Lift Landing."
            ),
            exits={
                "south": Exit("south", "p1_west_stacks", "South to the West Stacks."),
                "east": Exit("east", "p1_north_stacks", "East to the North Stacks."),
                "north": Exit("north", "p1_paternoster_landing", "North to the Paternoster Lift Landing."),
            },
            items=["blank_blueprint"],
            features={
                "desk": (
                    "Carved into the desk frieze is the motto: 'MNEMOS IS THE KEY THAT OPENS THE UPPER CANOPY'."
                ),
                "locker": "An auxiliary Pneumatic Dispatch Tube terminal (`stash <item>`, `retrieve <item>`, `locker`).",
            },
            ambient_hint="Take `blank_blueprint` and inspect it under the UV Lamp in the Restoration Lab (or combine it with `uv_bulb`).",
        ),
        Room(
            id="p1_paternoster_landing",
            name="Paternoster Lift Landing",
            coord=Coord3D(-1, 2, 1),
            stratum=1,
            subtitle="Continuous Chain Elevator",
            description=(
                "A vertical loop of open mahogany passenger compartments rises toward the "
                "Aetherial Botanical Domes (`Z = +2`). The lift motor is currently halted: its "
                "fuse box holds a blown ceramic fuse, and its security interlock is tied to the "
                "Cipher Rotunda to the east."
            ),
            exits={
                "south": Exit("south", "p1_curator_study", "South to the Curator's Private Study."),
                "east": Exit("east", "p1_cipher_rotunda", "East into the Cipher Rotunda."),
                "up": Exit(
                    "up",
                    "p2_conservatory_dome",
                    "Step into the rising Paternoster cab to Stratum +2.",
                    locked=True,
                    lock_id="p1_paternoster_lock",
                    lock_message=(
                        "The Paternoster Lift is motionless! You must both install the High-Ampere "
                        "Silver-Copper Fuse Link (`use copper_fuse on fusebox`) AND dial the keyword "
                        "`MNEMOS` in the Cipher Rotunda to the east."
                    ),
                ),
            },
            items=[],
            features={
                "fusebox": (
                    "An open slate switchboard missing a working cartridge fuse (`use copper_fuse on fusebox`)."
                ),
            },
            dynamic_flag_descriptions={
                "p1_paternoster_fused": (
                    "\n[bold orchid1]✦ The Silver-Copper Fuse Link glows warmly inside the switchboard![/bold orchid1]"
                )
            },
            ambient_hint="Install `copper_fuse` (from the Western Cantilever Span on Stratum 0) into `fusebox`, and dial `MNEMOS` in the Cipher Rotunda.",
        ),
        Room(
            id="p1_cipher_rotunda",
            name="Cipher Rotunda",
            coord=Coord3D(0, 2, 1),
            stratum=1,
            subtitle="Cryptographic Interlock",
            description=(
                "Six concentric brass letter-rings surround a central pedestal like a giant "
                "mechanical astrolabe. Rotating the rings spells a six-letter security keyword "
                "that releases the upper canopy lock."
            ),
            exits={
                "south": Exit("south", "p1_north_stacks", "South to the North Stacks."),
                "west": Exit("west", "p1_paternoster_landing", "West to the Paternoster Lift Landing."),
                "east": Exit("east", "p1_upper_gallery", "East to the Upper Gallery Overlook."),
            },
            items=[],
            features={
                "cipher_wheel": (
                    "Six rotating brass letter-rings (`dial <word>` or `set cipher <word>`). "
                    "Both the Assembled Cipher Disc and the Illuminated Blueprint reveal the keyword: `MNEMOS`."
                ),
            },
            dynamic_flag_descriptions={
                "p1_cipher_solved": (
                    "\n[bold orchid1]✦ The six brass rings align on M-N-E-M-O-S! The upper canopy interlock disengages![/bold orchid1]"
                )
            },
            ambient_hint="Enter `dial MNEMOS` to unlock the cryptographic seal!",
        ),
        Room(
            id="p1_upper_gallery",
            name="Upper Gallery Overlook",
            coord=Coord3D(1, 2, 1),
            stratum=1,
            subtitle="Clerestory Balcony",
            description=(
                "From this high wrought-iron balcony, you can look up through a glazed oculus into "
                "the emerald foliage of the Botanical Domes above. On a gardener's bench rests a "
                "cold brass apiarist's smoker."
            ),
            exits={
                "south": Exit("south", "p1_acoustic_loom", "South to the Acoustic Loom Chamber."),
                "west": Exit("west", "p1_cipher_rotunda", "West to the Cipher Rotunda."),
            },
            items=["empty_smoker"],
            features={
                "oculus": "Sunlight filters down through giant fern canopies and glass prisms above.",
            },
            ambient_hint="Combine `empty_smoker` with `dried_dream_leaf` (from the South Stacks) to craft the Smoldering Somnus-Fern Smoker.",
        ),
    ]
    return {r.id: r for r in rooms}
