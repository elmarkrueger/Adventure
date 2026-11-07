"""Stratum -2: The Geothermal Foundry & Steamworks (13 Rooms, Z = -2)."""

from typing import Dict
from engine.models import Coord3D, Exit, Room


def get_rooms() -> Dict[str, Room]:
    rooms = [
        Room(
            id="n2_venting_chimney",
            name="Venting Chimney Base",
            coord=Coord3D(1, 2, -2),
            stratum=-2,
            subtitle="Geothermal Exhaust Flue",
            description=(
                "You emerge onto a grated iron catwalk inside a roaring brick-lined exhaust flue. "
                "Hot sulfurous air rises from the Abyss below and vents through louvered dampers. "
                "Your grappling hook's three steel prongs are wedged solidly into the stanchion at "
                "your feet. Iron doors lead west toward the lift landing and south into a coal bunker."
            ),
            exits={
                "down": Exit("down", "n3_whispering_fissure", "Descend the copper-core grappling rope to Stratum -3."),
                "west": Exit("west", "n2_lift_landing", "Through a riveted iron door to the Abyssal Lift Landing."),
                "south": Exit("south", "n2_coal_bunker", "Into the dusty gloom of the Coal Bunker."),
            },
            items=["wire_brush"],
            features={
                "dampers": "Massive cast-iron louvers clanking softly in the geothermal updraft.",
                "stanchion": "The iron rung-post holding your grappling line down to the Abyss.",
            },
        ),
        Room(
            id="n2_lift_landing",
            name="Abyssal Lift Landing",
            coord=Coord3D(0, 2, -2),
            stratum=-2,
            subtitle="Freight Transfer Deck",
            description=(
                "A broad deck of checkered cast-iron plates overlooks the vertical freight shaft "
                "descending into the Bioluminescent Abyss. Overhead pulley sheaves carry thick "
                "steel cables into the Winch Room to the west. Southward, the heat intensifies "
                "around the central Boiler Manifold."
            ),
            exits={
                "east": Exit("east", "n2_venting_chimney", "East to the Venting Chimney Base."),
                "west": Exit("west", "n2_winch_room", "West into the Counterweight Winch Room."),
                "south": Exit("south", "n2_boiler_manifold", "South into the roaring Boiler Manifold Hall."),
                "down": Exit(
                    "down",
                    "n3_lift_shaft_bottom",
                    "Take the freight cage down to Stratum -3.",
                    locked=True,
                    lock_id="n3_counterweight_lock",
                    lock_message="The freight lift cable is slack! Release the counterweight in the Winch Room to the west (`pull winch`).",
                ),
            },
            items=[],
            features={
                "sheaves": "Six-foot grooved iron wheels guiding the haul cable into the western winch room.",
                "resonator": "A foundry-grade Mnemonic Resonator horn mounted on a cast-iron pillar (`play <cylinder>`).",
            },
            dynamic_flag_descriptions={
                "n2_counterweight_released": (
                    "\n[bold orange1]✦ The Abyssal Freight Cage is coupled and ready (`down` to Stratum -3).[/bold orange1]"
                )
            },
        ),
        Room(
            id="n2_winch_room",
            name="Counterweight Winch Room",
            coord=Coord3D(-1, 2, -2),
            stratum=-2,
            subtitle="Hoist Machinery",
            description=(
                "Enormous toothed winding drums fill this oil-scented chamber. A ten-ton basalt "
                "counterweight hangs suspended from a ratcheted release lever labeled 'ABYSSAL HOIST "
                "CLUTCH'. To the south, a humming corridor leads toward the Steam Turbine Gallery."
            ),
            exits={
                "east": Exit("east", "n2_lift_landing", "East to the Abyssal Lift Landing."),
                "south": Exit("south", "n2_turbine_gallery", "South into the Steam Turbine Gallery."),
            },
            items=["insulated_gauntlets"],
            features={
                "winch": (
                    "A heavy iron clutch lever (`pull winch` or `use winch`). Pulling it drops the "
                    "counterweight into tension and permanently unlocks the lift between Stratum -2 and -3."
                ),
                "drums": "Coiled with greased steel hawser cable.",
            },
            ambient_hint="Pull the winch lever (`pull winch`) to restore the elevator shortcut down to Stratum -3, and take the Forge Gauntlets.",
        ),
        Room(
            id="n2_coal_bunker",
            name="Anthracite Coal Bunker",
            coord=Coord3D(1, 1, -2),
            stratum=-2,
            subtitle="Fuel Hopper Bay",
            description=(
                "Conical iron hoppers tower overhead, trickling black anthracite and reddish ferric "
                "scale onto conveyor chutes. Without your Phosphor Lantern, the coal dust makes this "
                "vault pitch-dark."
            ),
            dark=True,
            exits={
                "north": Exit("north", "n2_venting_chimney", "North to the Venting Chimney Base."),
                "west": Exit("west", "n2_boiler_manifold", "West into the Boiler Manifold Hall."),
                "south": Exit("south", "n2_cooling_vats", "South to the Obsidian Cooling Vats."),
            },
            items=["iron_oxide", "soot_plaque"],
            features={
                "hoppers": "Rust and ferric oxide have accumulated in bright red drifts beneath the chutes.",
                "chutes": "Gravity-fed fuel lines supplying the backup boilers.",
            },
        ),
        Room(
            id="n2_boiler_manifold",
            name="Boiler Manifold Hall",
            coord=Coord3D(0, 1, -2),
            stratum=-2,
            subtitle="Geothermal Pressure Junction",
            description=(
                "The air shimmers with dry heat around a towering copper-and-iron steam manifold. "
                "Three high-pressure wheel valves—marked ALPHA, BETA, and GAMMA—feed a master "
                "pressure gauge calibrated from 0 to 120 PSI. The valves are blistering hot to "
                "the bare touch."
            ),
            exits={
                "north": Exit("north", "n2_lift_landing", "North to the Abyssal Lift Landing."),
                "east": Exit("east", "n2_coal_bunker", "East into the Anthracite Coal Bunker."),
                "west": Exit("west", "n2_turbine_gallery", "West to the Steam Turbine Gallery."),
                "south": Exit("south", "n2_magma_siphon", "South onto the Magma Siphon Bridge."),
            },
            items=[],
            features={
                "valve_alpha": "High-pressure steam valve Alpha (+40 PSI). Toggle with `turn valve_alpha` (requires Forge Gauntlets).",
                "valve_beta": "High-pressure steam valve Beta (+35 PSI). Toggle with `turn valve_beta` (requires Forge Gauntlets).",
                "valve_gamma": "High-pressure steam valve Gamma (+45 PSI). Toggle with `turn valve_gamma` (requires Forge Gauntlets).",
                "gauge": "Reads the combined PSI of open valves. 75 PSI powers the Foundry Press; 120 PSI powers the Central Steam Lift.",
            },
            dynamic_flag_descriptions={
                "n2_atrium_lift_powered": (
                    "\n[bold orange1]✦ The manifold needle sits at a steady 120 PSI! High-pressure "
                    "steam now surges to both the Foundry Press and the Southern Steam Lift.[/bold orange1]"
                )
            },
            ambient_hint="With the Asbestos-Weave Forge Gauntlets in your inventory, turn `valve_alpha`, `valve_beta`, and `valve_gamma` to reach 120 PSI.",
        ),
        Room(
            id="n2_turbine_gallery",
            name="Steam Turbine Gallery",
            coord=Coord3D(-1, 1, -2),
            stratum=-2,
            subtitle="Rotary Dynamo Hall",
            description=(
                "Rows of brass-cased Parsons turbines whine softly along a tiled gallery. "
                "A precision metalworking lathe stands in the corner beside a workbench dusted "
                "with silvery shavings. To the west is the glazed door of the Forge-Master's Office."
            ),
            exits={
                "north": Exit("north", "n2_winch_room", "North to the Counterweight Winch Room."),
                "east": Exit("east", "n2_boiler_manifold", "East to the Boiler Manifold Hall."),
                "west": Exit("west", "n2_forgemaster_office", "West into the Forge-Master's Office."),
                "south": Exit("south", "n2_pneumatic_hub", "South to the Pneumatic Dispatch Hub."),
            },
            items=["aluminum_shavings", "forge_hammer"],
            features={
                "lathe": "A belt-driven precision lathe used to turn aluminum and brass fittings.",
                "turbines": "Their copper commutators hum with steady geothermal current.",
            },
        ),
        Room(
            id="n2_forgemaster_office",
            name="Forge-Master's Office",
            coord=Coord3D(-2, 1, -2),
            stratum=-2,
            subtitle="Foundry Command Post",
            description=(
                "Through reinforced mica windows, this elevated office commands a sweeping view "
                "of the foundry floor. A drafting table holds cast-iron calipers, a soot-stained "
                "ledger, and a shattered brass master key."
            ),
            exits={
                "east": Exit("east", "n2_turbine_gallery", "East to the Steam Turbine Gallery."),
            },
            items=["foundry_ledger", "broken_sanctum_key", "magnesium_ribbon"],
            features={
                "desk": (
                    "Pinned to the desk blotter is a note: 'The Atrium Lift Key snapped in the lock "
                    "during the evacuation. Use the refractory fire-clay in the Cooling Vats to take "
                    "an impression, then cast a replacement in Clock-Brass at the Magma Siphon.'"
                ),
            },
            ambient_hint="Read the `foundry_ledger` and take the `broken_sanctum_key` to cast a new key in clay and molten brass.",
        ),
        Room(
            id="n2_cooling_vats",
            name="Obsidian Cooling Vats",
            coord=Coord3D(1, 0, -2),
            stratum=-2,
            subtitle="Quenching & Molding Floor",
            description=(
                "Deep stone troughs of quenching oil and endothermic brine line this humid hall. "
                "Molders' benches along the east wall hold blocks of refractory fire-clay and "
                "cryogenic coolant canisters. Southward, a channel of glowing molten slag blocks "
                "access to the Slag Crucible Chamber."
            ),
            exits={
                "north": Exit("north", "n2_coal_bunker", "North to the Anthracite Coal Bunker."),
                "west": Exit("west", "n2_magma_siphon", "West onto the Magma Siphon Bridge."),
                "south": Exit(
                    "south",
                    "n2_slag_crucible",
                    "Across the solidified slag crust into the Slag Crucible Chamber.",
                    locked=True,
                    lock_id="slag_bridge_lock",
                    unlock_item_id="cryo_canister",
                    consume_key=True,
                    lock_message=(
                        "A river of white-hot molten slag overflows the southern trench! You must "
                        "quench and solidify it (`use cryo_canister on slag`) before crossing."
                    ),
                    unlock_message=(
                        "You hurl the Pressurized Frost-Salts Canister into the molten trench! With "
                        "a thunderous crackle of steam, the slag freezes into a solid basalt causeway!"
                    ),
                ),
            },
            items=["clay_blank", "cryo_canister"],
            features={
                "slag": "A bubbling trench of molten silicate blocking the southern archway (`use cryo_canister on slag`).",
                "vats": "Heavy iron quenching tanks smelling of mineral oil and frost-salts.",
            },
            ambient_hint="Use the `cryo_canister` on the `slag` (`use canister on slag`) to solidify a path south!",
        ),
        Room(
            id="n2_magma_siphon",
            name="Magma Siphon Bridge",
            coord=Coord3D(0, 0, -2),
            stratum=-2,
            subtitle="Heart of the Foundry",
            description=(
                "An arched bridge of refractory brick spans a dazzling column of tapped earth-magma "
                "drawn up through tungsten-lined siphons. Built into the bridge parapet is a "
                "high-intensity Smelting Furnace cradle designed to heat graphite crucibles to "
                "pouring temperature in seconds."
            ),
            exits={
                "north": Exit("north", "n2_boiler_manifold", "North to the Boiler Manifold Hall."),
                "east": Exit("east", "n2_cooling_vats", "East to the Obsidian Cooling Vats."),
                "west": Exit("west", "n2_pneumatic_hub", "West to the Pneumatic Dispatch Hub."),
                "south": Exit("south", "n2_pressure_vault", "South to the Pressure Regulation Vault."),
            },
            items=["empty_crucible"],
            features={
                "furnace": (
                    "The Magma Siphon Smelting Cradle (`use unheated_brass_crucible on furnace`). "
                    "Requires Asbestos-Weave Forge Gauntlets to safely retrieve the molten crucible."
                ),
                "siphon": "A blinding torrent of liquid rock circulating behind quartz-mica blast shields.",
            },
            ambient_hint="Combine `empty_crucible` + `brass_ingot`, then `use brass_crucible on furnace` to melt it!",
        ),
        Room(
            id="n2_pneumatic_hub",
            name="Pneumatic Dispatch Hub",
            coord=Coord3D(-1, 0, -2),
            stratum=-2,
            subtitle="Cross-Stratum Tube Terminal",
            description=(
                "Polished brass pneumatic tubes snake across the ceiling and converge on an "
                "air-powered storage carousel. Once the master Pneumatic Network is activated in "
                "the Atrium (or right here at the terminal), you can store and retrieve items "
                "across strata (`stash <item>` / `retrieve <item>` / `locker`)."
            ),
            exits={
                "north": Exit("north", "n2_turbine_gallery", "North to the Steam Turbine Gallery."),
                "east": Exit("east", "n2_magma_siphon", "East to the Magma Siphon Bridge."),
                "south": Exit("south", "n2_tram_dock", "South to the Foundry Tram Dock."),
            },
            items=["brass_ingot", "broken_coupler"],
            features={
                "locker": (
                    "The Pneumatic Storage Terminal. Use `stash <item>` to deposit an item into the "
                    "Spire's pneumatic network and `retrieve <item>` to withdraw it at any hub!"
                ),
                "tubes": "Pressurized brass conduits running vertically through all seven strata.",
            },
            ambient_hint="You can `stash <item>` and `retrieve <item>` at any Pneumatic Locker room to free up inventory slots!",
        ),
        Room(
            id="n2_slag_crucible",
            name="Slag Crucible Chamber",
            coord=Coord3D(1, -1, -2),
            stratum=-2,
            subtitle="Heavy Casting Pit",
            description=(
                "Beyond the frozen slag bridge lies a cavernous casting pit dominated by a tilted "
                "Bessemer converter. In the center of the floor stands a reinforced refractory "
                "pedestal cradling an amber-glass Mnemonic Cylinder."
            ),
            exits={
                "north": Exit("north", "n2_cooling_vats", "North across the frozen slag causeway."),
                "west": Exit("west", "n2_pressure_vault", "West into the Pressure Regulation Vault."),
            },
            items=["cylinder_2", "slag_nodule"],
            features={
                "converter": "A pear-shaped steel vessel lined with silica brick.",
                "pedestal": "Stamped: 'MEMORY ANCHOR II — THE FORGING OF THE CHORISTER'.",
            },
            ambient_hint="Take Mnemonic Cylinder II and play it at a Resonator (`play cylinder 2`).",
        ),
        Room(
            id="n2_pressure_vault",
            name="Pressure Regulation Vault",
            coord=Coord3D(0, -1, -2),
            stratum=-2,
            subtitle="Southern Steam Lift Base",
            description=(
                "Twin vertical steam cylinders flank a brass-and-iron elevator cab that ascends "
                "to the Sunken Aqueducts (`Z = -1`). The elevator gate is secured by a geometric "
                "Signet Lock, and its steam accumulator requires 120 PSI from the Boiler Manifold."
            ),
            exits={
                "north": Exit("north", "n2_magma_siphon", "North onto the Magma Siphon Bridge."),
                "east": Exit("east", "n2_slag_crucible", "East into the Slag Crucible Chamber."),
                "west": Exit("west", "n2_tram_dock", "West to the Foundry Tram Dock."),
                "up": Exit(
                    "up",
                    "n1_steam_vestibule",
                    "Ascend in the High-Pressure Steam Lift to Stratum -1.",
                    locked=True,
                    lock_id="n2_steam_lift_lock",
                    unlock_item_id="sanctum_key",
                    lock_message=(
                        "The Steam Lift gate is locked with a geometric Signet Lock (`use sanctum_key on up`), "
                        "and the steam accumulator requires 120 PSI from the Boiler Manifold!"
                    ),
                    unlock_message=(
                        "You insert the Cast Brass Sanctum Key into the gate lock and turn it! The "
                        "brass bolts retract with a resonant clank."
                    ),
                ),
            },
            items=[],
            features={
                "lift": "Requires both the Cast Brass Sanctum Key and 120 PSI steam pressure from the Boiler Manifold.",
                "accumulator": "A riveted steam reservoir gauge showing current manifold pressure.",
            },
            ambient_hint="Ensure all three Boiler Manifold valves are open (120 PSI) and unlock the lift with the Cast Brass Sanctum Key.",
        ),
        Room(
            id="n2_tram_dock",
            name="Foundry Tram Dock",
            coord=Coord3D(-1, -1, -2),
            stratum=-2,
            subtitle="Inclined Ore Railway",
            description=(
                "An inclined cog-railway platform where ore trams once hauled ingots up to the "
                "lower workshops. A derailed maintenance car sits beside a heavy hydraulic press."
            ),
            exits={
                "north": Exit("north", "n2_pneumatic_hub", "North to the Pneumatic Dispatch Hub."),
                "east": Exit("east", "n2_pressure_vault", "East to the Pressure Regulation Vault."),
            },
            items=["sluice_crank"],
            features={
                "press": "A steam-powered hydraulic press.",
                "tram": "Inside the cab of the maintenance car rests a Heavy Iron Lock-Crank for the Aqueduct locks above.",
            },
        ),
    ]
    return {r.id: r for r in rooms}
