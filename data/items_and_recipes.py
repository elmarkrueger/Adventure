"""All items, combination recipes, and lore transcripts for Echoes of the Aethelgard Spire."""

from typing import Dict, List
from engine.models import Item, Recipe, LoreEntry


def get_items() -> Dict[str, Item]:
    items_list = [
        # --- STRATUM -3: THE BIOLUMINESCENT ABYSS ---
        Item(
            id="fractured_vial",
            name="Fractured Memory Vial",
            aliases=["vial", "fractured vial", "memory vial", "glass vial"],
            short_desc="A cracked quartz phial still glowing with faint silver residue.",
            examine_text=(
                "Etched along the brass collar are the words: 'SUBJECT 01 — VAELEN KORR — "
                "SELF-ADMINISTERED OBLIVION DRAUGHT'. Inside, a few droplets of liquid silver "
                "shimmer like trapped starlight."
            ),
            slot_size=1,
            category="component",
            read_text="SUBJECT 01 — VAELEN KORR — DO NOT RESTORE UNTIL ALL SEVEN ANCHORS ARE VERIFIED.",
        ),
        Item(
            id="unlit_lantern",
            name="Unlit Brass Lantern",
            aliases=["lantern", "unlit lantern", "brass lantern", "cage"],
            short_desc="An empty miner's phosphor-cage with a crystal housing.",
            examine_text=(
                "A sturdy abyssal lantern designed not for oil, but to house living bioluminescent "
                "fungi. Its crystal chamber is currently empty and dark."
            ),
            slot_size=1,
            category="component",
        ),
        Item(
            id="glow_moss",
            name="Luminous Mycelium Clump",
            aliases=["moss", "mycelium", "glow moss", "fungi", "clump"],
            short_desc="A pulsing clump of cyan cavern moss.",
            examine_text=(
                "Harvested from the damp walls of the Phosphor Cavern. It emits a soft cyan glow, "
                "though it needs a reflective housing to illuminate a whole room."
            ),
            slot_size=1,
            category="component",
        ),
        Item(
            id="phosphor_lantern",
            name="Phosphor Lantern",
            aliases=["lit lantern", "phosphor lantern", "lantern", "light"],
            short_desc="A brass lantern blazing with steady cyan bioluminescence.",
            examine_text=(
                "The reflective crystal magnifies the Luminous Mycelium into a brilliant cyan beam "
                "capable of piercing the darkest chambers of the Spire."
            ),
            slot_size=1,
            category="tool",
        ),
        Item(
            id="rusted_grapnel",
            name="Encrusted Iron Grapnel",
            aliases=["grapnel", "rusted grapnel", "hook", "iron hook"],
            short_desc="A three-pronged climbing hook caked in thick brine-scale.",
            examine_text=(
                "The iron prongs are fused together by centuries of calcified mineral crust. "
                "You would need a corrosive acid or solvent to strip away the buildup before tying a rope to its eye."
            ),
            slot_size=1,
            category="component",
        ),
        Item(
            id="brine_solvent",
            name="Flask of Acidic Brine-Solvent",
            aliases=["solvent", "brine solvent", "acid flask", "flask"],
            short_desc="A stoneware bottle of fizzing mineral descaler.",
            examine_text=(
                "Used by abyssal maintenance crews to dissolve limestone and barnacle scale from "
                "sluice valves and ironwork."
            ),
            slot_size=1,
            category="component",
        ),
        Item(
            id="clean_grapnel",
            name="Descale-Polished Grapnel",
            aliases=["clean grapnel", "polished grapnel", "grapnel", "hook"],
            short_desc="A sharp, three-pronged steel climbing hook with an open eyelet.",
            examine_text=(
                "Stripped of mineral crust, the steel prongs are razor-sharp. All it lacks is a strong "
                "length of rope."
            ),
            slot_size=1,
            category="component",
        ),
        Item(
            id="mycelial_cord",
            name="Raw Mycelial Fiber Bundle",
            aliases=["fiber", "cord", "mycelial cord", "bundle", "fibers"],
            short_desc="Long, tough strands of dried fungal tendon.",
            examine_text=(
                "Individually these strands are fibrous and flexible, but two bundles braided together "
                "or twisted with wire would form an unbreakable climbing rope."
            ),
            slot_size=1,
            category="component",
        ),
        Item(
            id="copper_wire_spool",
            name="Spool of Braided Copper Wire",
            aliases=["wire", "copper wire", "spool"],
            short_desc="A heavy reel of flexible copper cable.",
            examine_text=(
                "Salvaged from a submerged telemetry conduit. Strong enough to reinforce organic fibers "
                "or mend electrical junctions."
            ),
            slot_size=1,
            category="component",
        ),
        Item(
            id="braided_rope",
            name="Copper-Core Climbing Rope",
            aliases=["rope", "braided rope", "climbing rope", "cable"],
            short_desc="Thirty feet of mycelial rope woven around a copper core.",
            examine_text=(
                "Supple yet strong enough to support several hundred pounds. Combine it with a grapnel "
                "to Fashion a Grappling Hook."
            ),
            slot_size=1,
            category="component",
        ),
        Item(
            id="grappling_hook",
            name="Abyssal Grappling Hook",
            aliases=["grappling hook", "grapple", "hook and rope"],
            short_desc="A steel grapnel knotted securely to thirty feet of copper-core rope.",
            examine_text=(
                "An essential vertical traversal tool. Can be thrown up open service shafts or hooked "
                "onto overhead ledges."
            ),
            slot_size=1,
            category="tool",
            usable_targets=["service_shaft", "collapsed_stair", "overhang_rung"],
        ),
        Item(
            id="valve_wheel",
            name="Octagonal Bronze Valve Wheel",
            aliases=["wheel", "valve wheel", "bronze wheel"],
            short_desc="A heavy bronze handwheel with a square center socket.",
            examine_text=(
                "Recovered from the Submerged Bell-Dock. It fits standard sluice spindles in the "
                "Abyssal drainage network."
            ),
            slot_size=1,
            category="tool",
            usable_targets=["sluice_spindle_c", "broken_manifold"],
        ),
        Item(
            id="diving_helmet",
            name="Pressurized Brass Diving Hood",
            aliases=["helmet", "diving helmet", "hood", "diving hood"],
            short_desc="A heavy spherical diving helmet with an air-bladder collar.",
            examine_text=(
                "Its viewport is thick quartz, and an internal chemical scrubber provides ten minutes "
                "of breathable air when wading into flooded chambers."
            ),
            slot_size=2,
            category="tool",
        ),
        Item(
            id="cylinder_1",
            name="Mnemonic Cylinder I (Cyan Quartz)",
            aliases=["cylinder 1", "cylinder i", "cyan cylinder", "first cylinder"],
            short_desc="A fluted cyan quartz phonograph cylinder humming with faint warmth.",
            examine_text=(
                "Engraved on the rim: 'CYLINDER I — THE FOUNDING OF THE FAULT ANCHOR'. "
                "Play this on any Mnemonic Resonator to restore your first lost memory."
            ),
            slot_size=1,
            category="memory",
            memory_id="mem_1",
        ),
        Item(
            id="abyssal_tablet",
            name="Slate Tablet of the Sluice-Keepers",
            aliases=["tablet", "slate", "abyssal tablet", "sluice tablet"],
            short_desc="A chiseled slate plaque detailing the Ossuary drainage sequence.",
            examine_text="A waterproof slate carved by the engineers of Stratum -3.",
            slot_size=1,
            category="lore",
            lore_id="lore_n3_sluice",
            read_text=(
                "SLUICE DRAINAGE PROTOCOL:\n"
                "'To purge the Drowned Ossuary without bursting the lower pipes: "
                "Open Valve A (Intake Bypass), leave Valve B (Backflow) CLOSED, "
                "and attach the spare wheel to open Valve C (Sump Outflow).'"
            ),
        ),

        # --- STRATUM -2: THE GEOTHERMAL FOUNDRY ---
        Item(
            id="insulated_gauntlets",
            name="Asbestos-Weave Forge Gauntlets",
            aliases=["gauntlets", "gloves", "forge gauntlets", "insulated gauntlets"],
            short_desc="Heavy heat-shielded gauntlets lined with basilisk-scale mica.",
            examine_text=(
                "Allows the wearer to handle red-hot crucibles, scorched steam valves, and molten "
                "castings without burning their hands."
            ),
            slot_size=1,
            category="tool",
        ),
        Item(
            id="empty_crucible",
            name="Graphite Smelting Crucible",
            aliases=["crucible", "empty crucible", "graphite crucible", "pot"],
            short_desc="A thick-walled refractory pot for melting soft metals.",
            examine_text="Capable of withstanding magma-siphon temperatures.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="brass_ingot",
            name="Ingot of Imperial Clock-Brass",
            aliases=["ingot", "brass ingot", "brass"],
            short_desc="A stamped bar of high-purity naval brass.",
            examine_text="Stamped with the Spire's crest. Melts cleanly in a heated crucible.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="unheated_brass_crucible",
            name="Crucible with Brass Ingot",
            aliases=["brass crucible", "unheated crucible"],
            short_desc="A graphite crucible holding a solid brass ingot.",
            examine_text="Place or use this at the Magma Siphon Furnace to melt the brass.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="molten_brass_crucible",
            name="Crucible of Molten Brass",
            aliases=["molten brass", "molten crucible", "hot crucible"],
            short_desc="A glowing crucible brimming with liquid golden brass.",
            examine_text="Simmering with radiant heat. Ready to be poured into a heat-proof mold.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="clay_blank",
            name="Block of Refractory Fire-Clay",
            aliases=["clay", "fire clay", "clay blank", "block"],
            short_desc="A malleable slab of fine foundry casting clay.",
            examine_text="Used to take impressions of keys, gears, and seals before casting.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="broken_sanctum_key",
            name="Fractured Sanctum Signet-Key",
            aliases=["broken key", "fractured key", "signet", "broken sanctum key"],
            short_desc="A snapped master key whose intricate bit is intact but handle is sheared off.",
            examine_text=(
                "Too brittle to turn in a lock directly, but its ward pattern is still crisp enough "
                "to press into refractory clay to form a casting mold."
            ),
            slot_size=1,
            category="component",
        ),
        Item(
            id="key_mold",
            name="Impressed Clay Key-Mold",
            aliases=["mold", "key mold", "clay mold"],
            short_desc="A fire-clay mold bearing the negative impression of the Sanctum Signet-Key.",
            examine_text="Combine with a Crucible of Molten Brass to cast a new key.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="sanctum_key",
            name="Cast Brass Sanctum Key",
            aliases=["sanctum key", "brass key", "cast key", "signet key"],
            short_desc="A newly cast, gleaming brass master key for the Grand Atrium Lift.",
            examine_text="Still warm from the foundry. Its geometric bit matches the Atrium locks.",
            slot_size=1,
            category="key",
        ),
        Item(
            id="cryo_canister",
            name="Pressurized Frost-Salts Canister",
            aliases=["cryo canister", "frost canister", "canister", "coolant"],
            short_desc="An endothermic alchemical bomb used to rapidly quench molten slag.",
            examine_text=(
                "Warning label: 'DISCHARGE OVER MOLTEN SLAG CHANNELS TO SOLIDIFY EMERGENCY WALKWAYS.'"
            ),
            slot_size=1,
            category="tool",
        ),
        Item(
            id="iron_oxide",
            name="Pouch of Red Iron Oxide",
            aliases=["iron oxide", "rust powder", "oxide", "red powder"],
            short_desc="Fine ferric rust powder scraped from the Coal Bunker hoppers.",
            examine_text="One half of a classic high-temperature aluminothermic reaction.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="aluminum_shavings",
            name="Jar of Fine Aluminum Filings",
            aliases=["aluminum", "filings", "shavings", "aluminum shavings"],
            short_desc="Silvery metallic dust from the turbine lathe room.",
            examine_text="When mixed with iron oxide, creates raw thermite powder.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="thermite_powder",
            name="Unprimed Thermite Mixture",
            aliases=["thermite powder", "mixture", "unprimed thermite"],
            short_desc="A grey-red blend of aluminum filings and iron oxide.",
            examine_text="Requires a high-temperature starter like a Magnesium Ribbon to ignite.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="magnesium_ribbon",
            name="Coil of Magnesium Igniter Ribbon",
            aliases=["magnesium", "ribbon", "magnesium ribbon", "fuse"],
            short_desc="A silvery strip of metal that burns with blinding white heat.",
            examine_text="Used as a high-temperature fuse for thermite charges.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="thermite_charge",
            name="Primed Thermite Breaching Charge",
            aliases=["thermite", "thermite charge", "charge", "breaching charge"],
            short_desc="A ceramic pot packed with thermite and a magnesium fuse.",
            examine_text="Capable of melting through jammed blast doors or fused iron shackles.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="cylinder_2",
            name="Mnemonic Cylinder II (Amber Slag-Glass)",
            aliases=["cylinder 2", "cylinder ii", "amber cylinder", "second cylinder"],
            short_desc="A heavy amber-glass cylinder warm to the touch.",
            examine_text="Engraved: 'CYLINDER II — THE FORGING OF THE CHORISTER'.",
            slot_size=1,
            category="memory",
            memory_id="mem_2",
        ),
        Item(
            id="foundry_ledger",
            name="Forge-Master's Pressure Ledger",
            aliases=["ledger", "pressure ledger", "foundry ledger"],
            short_desc="A soot-stained logbook detailing the Manifold valve ratings.",
            examine_text="Contains the exact PSI contributions of Valves Alpha, Beta, and Gamma.",
            slot_size=1,
            category="lore",
            lore_id="lore_n2_manifold",
            read_text=(
                "BOILER MANIFOLD CALIBRATION LOG:\n"
                "- Valve Alpha supplies +40 PSI when opened.\n"
                "- Valve Beta supplies +35 PSI when opened.\n"
                "- Valve Gamma supplies +45 PSI when opened.\n"
                "NOTE: The Hydraulic Satchel-Press engages at >= 75 PSI. "
                "The Central Atrium Steam-Lift requires all 120 PSI to ascend to Stratum -1."
            ),
        ),
        Item(
            id="torn_satchel",
            name="Torn Archivist's Satchel Frame",
            aliases=["satchel frame", "torn satchel", "frame"],
            short_desc="A brass-ribbed utility pack whose leather body has rotted away.",
            examine_text="If fitted with Cured Basal-Leather, it would expand your carrying capacity.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="cured_leather",
            name="Roll of Cured Basal-Hide",
            aliases=["leather", "hide", "cured leather", "basal hide"],
            short_desc="Thick, waterproof subterranean reptile leather.",
            examine_text="Tough and flexible. Ideal for repairing an Archivist's Satchel.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="archivist_satchel",
            name="Restored Archivist's Satchel",
            aliases=["satchel", "archivist satchel", "pack", "backpack"],
            short_desc="A multi-pocketed leather and brass field pack (`use satchel` to equip).",
            examine_text=(
                "Use or wear this satchel (`use satchel`) to permanently increase your inventory "
                "capacity from 8 slots to 10 slots!"
            ),
            slot_size=1,
            category="upgrade",
        ),

        # --- STRATUM -1: THE SUNKEN AQUEDUCTS & LABS ---
        Item(
            id="nitric_acid_vial",
            name="Stoppered Bottle of Nitric Spirit",
            aliases=["nitric", "nitric acid", "spirit", "bottle"],
            short_desc="Fuming amber nitric acid from the Vitriol Vault.",
            examine_text="Labeled: 'AZOTIC SPIRIT (HNO3) — One part required for Aqua Regia.'",
            slot_size=1,
            category="component",
        ),
        Item(
            id="muriatic_acid_vial",
            name="Carboy of Muriatic Acid",
            aliases=["muriatic", "muriatic acid", "hydrochloric", "carboy"],
            short_desc="Pungent green-tinted hydrochloric acid.",
            examine_text="Labeled: 'MURIATIC SPIRIT (HCl) — Three parts required for Aqua Regia.'",
            slot_size=1,
            category="component",
        ),
        Item(
            id="unrefined_regia",
            name="Flask of Unrefined Acid Mixture",
            aliases=["unrefined regia", "acid mixture", "raw regia"],
            short_desc="A cloudy orange mixture of nitric and muriatic acids.",
            examine_text=(
                "Must be distilled at the Alchemical Alembic Bench while the burner is set to MEDIUM "
                "heat to produce pure Aqua Regia."
            ),
            slot_size=1,
            category="component",
        ),
        Item(
            id="aqua_regia",
            name="Alembic Flask of Pure Aqua Regia",
            aliases=["aqua regia", "regia", "royal water", "gold solvent"],
            short_desc="A shimmering scarlet acid capable of dissolving solid gold.",
            examine_text="The 'Royal Water' of alchemists. Will dissolve the Gold Seal on the Founders' Crypt.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="cracked_lens",
            name="Fractured Aether-Quartz Lens",
            aliases=["cracked lens", "fractured lens", "quartz lens"],
            short_desc="A precision concave lens split cleanly into two halves.",
            examine_text="Crafted in the Glassblower's Annex. Optical Balsam Resin could mend the seam invisibly.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="optical_resin",
            name="Tube of Refractive Amber Balsam",
            aliases=["resin", "optical resin", "balsam", "glue"],
            short_desc="Crystal-clear pine resin with the exact refractive index of quartz.",
            examine_text="Used by Spire opticians to cement compound lenses without distortion.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="mended_lens",
            name="Cemented Aether-Quartz Lens",
            aliases=["mended lens", "cemented lens", "quartz optic"],
            short_desc="A seamlessly repaired optical lens.",
            examine_text="Needs to be fitted into a Brass Gimbal Mount before installation in the Prism Tower.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="brass_gimbal",
            name="Calibrated Brass Gimbal Ring",
            aliases=["gimbal", "brass gimbal", "mount", "ring"],
            short_desc="A rotating brass collar with vernier degree markings.",
            examine_text="Designed to hold a 6-inch Aether-Quartz Lens inside the Botanical Prism Array.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="focusing_optic",
            name="Gimbal-Mounted Focusing Optic",
            aliases=["focusing optic", "optic", "mounted lens", "prism lens"],
            short_desc="A complete heliostat focusing assembly ready for the Prism Tower.",
            examine_text="Can be installed in the Prism Refraction Tower on Stratum +2.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="sluice_crank",
            name="Heavy Iron Lock-Crank",
            aliases=["crank", "lock crank", "sluice crank", "handle"],
            short_desc="An L-shaped iron winding handle for the Aqueduct canal locks.",
            examine_text="Fits the winches in the Canal Lock Control room.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="cylinder_3",
            name="Mnemonic Cylinder III (Aquamarine Beryl)",
            aliases=["cylinder 3", "cylinder iii", "aquamarine cylinder", "third cylinder"],
            short_desc="A translucent sea-green cylinder recovered from the Founders' Crypt.",
            examine_text="Engraved: 'CYLINDER III — THE WHISPER IN THE RESERVOIR'.",
            slot_size=1,
            category="memory",
            memory_id="mem_3",
        ),
        Item(
            id="alchemist_notes",
            name="Distiller's Vellum Scroll",
            aliases=["scroll", "vellum scroll", "alchemist notes"],
            short_desc="A stained parchment scroll from the Alchemical Distillery.",
            examine_text="Contains distillation temperatures and acoustic dome reflection angles.",
            slot_size=1,
            category="lore",
            lore_id="lore_n1_alchemy",
            read_text=(
                "DISTILLATION & ACOUSTICS MEMO:\n"
                "1. Never boil Aqua Regia on HIGH heat or the fumes will decompose; LOW heat fails "
                "to react. Set the Alembic Burner to MEDIUM (`set burner medium`) before distilling.\n"
                "2. In the Whispering Dome, rotate the Parabolic Dish to FOCUS (`set dish focus`) "
                "to hear the echo rebounding from the Atrium chimes above."
            ),
        ),

        # --- STRATUM 0: THE GRAND CLOCKWORK ATRIUM ---
        Item(
            id="beveled_gear",
            name="Heavy Beveled Escapement Gear",
            aliases=["gear", "beveled gear", "escapement gear", "cog"],
            short_desc="A 32-tooth phosphor-bronze gear for the Central Pendulum drive.",
            examine_text="The missing link in the North Gear-Train Gallery.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="lead_counterweight",
            name="Stamped Lead Trim-Weight (15 kg)",
            aliases=["weight", "lead weight", "counterweight", "trim weight"],
            short_desc="A dense cylinder of stamped lead with a suspension hook.",
            examine_text=(
                "Used to balance the Escapement Clockwork in the Vault of Weights. Takes up 2 inventory slots!"
            ),
            slot_size=2,
            category="tool",
        ),
        Item(
            id="pneumatic_passkey",
            name="Perforated Brass Dispatch Card",
            aliases=["dispatch card", "passkey", "punch card", "card"],
            short_desc="A punched brass card that activates the Spire's Pneumatic Locker network.",
            examine_text="Insert this into the Pneumatic Locker console on Stratum 0 to unlock cross-level storage.",
            slot_size=1,
            category="key",
        ),
        Item(
            id="chime_mallet",
            name="Felted Rosewood Chime Mallet",
            aliases=["mallet", "chime mallet", "hammer"],
            short_desc="A balanced acoustic striker for the Atrium's resonance bells.",
            examine_text="Used on the Acoustic Chime Balcony to strike `do`, `re`, `mi`, `sol`, or `la`.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="cylinder_4",
            name="Mnemonic Cylinder IV (Gilded Brass)",
            aliases=["cylinder 4", "cylinder iv", "gilded cylinder", "fourth cylinder"],
            short_desc="A precision-machined gold-plated cylinder from the Hall of Anchors.",
            examine_text="Engraved: 'CYLINDER IV — THE DAY TIME FRACTURED'.",
            slot_size=1,
            category="memory",
            memory_id="mem_4",
        ),
        Item(
            id="chronometer_plaque",
            name="Engraved Chronometer Calibration Plaque",
            aliases=["plaque", "chronometer plaque", "calibration plaque"],
            short_desc="A brass plate listing the four epoch digits of the Spire.",
            examine_text="Found in the Cartographer's Wing.",
            slot_size=1,
            category="lore",
            lore_id="lore_z0_chrono",
            read_text=(
                "THE FOUR EPOCHS OF AETHELGARD (Chronometer Code):\n"
                "  First Digit  : Number of Subterranean Strata below the Atrium (3) + 1 = 4\n"
                "  Second Digit : Total Strata of the Spire = 7\n"
                "  Third Digit  : The Solitary Pendulum at the Heart = 1\n"
                "  Fourth Digit : Nine Chimes of the Solstice = 9\n"
                "  (Dial the four-digit sequence on the Chronometer Control Booth: `dial 4719`)"
            ),
        ),

        # --- STRATUM +1: THE MNEMONIC ARCHIVES ---
        Item(
            id="blank_blueprint",
            name="Seemingly Blank Vellum Blueprint",
            aliases=["blueprint", "blank blueprint", "vellum", "chart"],
            short_desc="A rolled architectural sheet smelling faintly of lemon and cobalt.",
            examine_text=(
                "To the naked eye, only border gridlines are visible. The ink was drawn in "
                "sympathetic cobalt-fluorescing medium—expose it to an Ultraviolet Lamp to read it."
            ),
            slot_size=1,
            category="component",
        ),
        Item(
            id="uv_bulb",
            name="Quartz-Mercury Vapor Bulb",
            aliases=["bulb", "uv bulb", "mercury bulb", "lamp bulb"],
            short_desc="A violet-tinted discharge bulb for the Parchment Restoration Lab.",
            examine_text="Install or combine with the Restoration Lamp Frame to reveal sympathetic inks.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="revealed_blueprint",
            name="Illuminated Spire Override Blueprint",
            aliases=["revealed blueprint", "override blueprint", "illuminated blueprint"],
            short_desc="The Architect's hidden schematic glowing with violet ink.",
            examine_text="Reveals the secret passage behind the Forbidden Index and the Astrolabe coordinates!",
            slot_size=1,
            category="lore",
            lore_id="lore_p1_blueprint",
            read_text=(
                "ARCHITECT KORR'S PRIVATE SCHEMATIC:\n"
                "1. CIPHER ROTUNDA KEYWORD: 'MNEMOS' (`dial MNEMOS` in the Cipher Rotunda).\n"
                "2. SECRET VAULT: Pull the 'Treatise on Oblivion' spine in the West Stacks.\n"
                "3. CELESTIAL ASTROLABE TARGET: Azimuth 240, Altitude 65.\n"
                "4. WIND-ORGAN CHORD (Stratum +2): Play `CEGB` to power the Zenith Elevator."
            ),
        ),
        Item(
            id="copper_fuse",
            name="High-Ampere Silver-Copper Fuse Link",
            aliases=["fuse", "copper fuse", "fuse link", "cartridge"],
            short_desc="A ceramic cartridge fuse rated for the Archive Paternoster lift.",
            examine_text="Replaces the blown fuse in the Paternoster Lift Landing on Stratum +1.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="tuning_fork_432",
            name="Harmonic Tuning Fork (432 Hz — Veridian)",
            aliases=["fork 432", "432 fork", "veridian fork", "tuning fork 432"],
            short_desc="A pitch-calibrated steel fork stamped '432 Hz — WEST PYLON'.",
            examine_text="Resonates at 432 Hz. Used both in the Acoustic Loom and the West Harmonic Pylon.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="cylinder_5",
            name="Mnemonic Cylinder V (Amethyst Crystal)",
            aliases=["cylinder 5", "cylinder v", "amethyst cylinder", "fifth cylinder"],
            short_desc="A violet amethyst cylinder locked inside the Curator's Secret Vault.",
            examine_text="Engraved: 'CYLINDER V — THE CORRUPTION OF THE LOGIC LOOM'.",
            slot_size=1,
            category="memory",
            memory_id="mem_5",
        ),

        # --- STRATUM +2: THE AETHERIAL BOTANICAL DOMES ---
        Item(
            id="dried_dream_leaf",
            name="Bundle of Dried Somnus-Fern Fronds",
            aliases=["fern", "leaves", "dream leaf", "fronds", "herbs"],
            short_desc="Silvery botanical fronds that release a soothing soporific vapor when burned.",
            examine_text="Can be loaded into an Apiarist's Smoker to calm the mechanical Brass Bees.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="empty_smoker",
            name="Cold Brass Apiarist's Smoker",
            aliases=["smoker", "empty smoker", "bellows"],
            short_desc="A hinged brass censer with leather bellows, currently empty.",
            examine_text="Combine with Dried Somnus-Fern Fronds to prepare a Calming Smoker.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="lit_smoker",
            name="Smoldering Somnus-Fern Smoker",
            aliases=["lit smoker", "calming smoker", "smoker"],
            short_desc="A brass bellows-smoker puffing fragrant lavender-silver vapor.",
            examine_text="Use this in the Apiary of Brass Bees to pacify the swarm and harvest Conducting Wax.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="conducting_wax",
            name="Comb of Gold-Spun Conducting Wax",
            aliases=["wax", "conducting wax", "comb", "honeycomb"],
            short_desc="Hexagonal metallic wax spun by the clockwork bees from gold-leaf nectar.",
            examine_text="Used to lubricate and seal the high-voltage contacts of the Lightning Spire.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="starlight_pollen",
            name="Phial of Luminescent Starlight Pollen",
            aliases=["pollen", "starlight pollen", "dust"],
            short_desc="Glittering silver-gold pollen harvested from the Nocturne Bloom.",
            examine_text="When dusted onto the Dormant Sun-Orchid, causes its crystalline petals to unfurl.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="tuning_fork_528",
            name="Harmonic Tuning Fork (528 Hz — Golden)",
            aliases=["fork 528", "528 fork", "golden fork", "tuning fork 528"],
            short_desc="A chime-steel tuning fork stamped '528 Hz — EAST PYLON'.",
            examine_text="Held within the petals of the Starlight Orchid. Resonates at 528 Hz.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="cylinder_6",
            name="Mnemonic Cylinder VI (Emerald Jade)",
            aliases=["cylinder 6", "cylinder vi", "emerald cylinder", "sixth cylinder"],
            short_desc="A carved jade cylinder resting beneath the Wind-Organ pipes.",
            examine_text="Engraved: 'CYLINDER VI — THE SEVEN SEALS OF OBLIVION'.",
            slot_size=1,
            category="memory",
            memory_id="mem_6",
        ),

        # --- STRATUM +3: THE CELESTIAL OBSERVATORY & CROWN ---
        Item(
            id="star_chart_overlay",
            name="Perforated Brass Star-Chart Disc",
            aliases=["star chart", "overlay", "disc", "chart"],
            short_desc="An astrolabe rete plate etched with the Zenith constellations.",
            examine_text="Confirms the alignment coordinates: Azimuth 240, Altitude 65.",
            slot_size=1,
            category="tool",
            read_text="ZENITH ALIGNMENT: Set Astrolabe Azimuth to 240 and Altitude to 65 (`set azimuth 240`, `set altitude 65`).",
        ),
        Item(
            id="aether_capacitor",
            name="Uncharged Leyden Aether-Capacitor",
            aliases=["capacitor", "uncharged capacitor", "leyden jar"],
            short_desc="A heavy quartz-and-foil accumulator jar.",
            examine_text="Coat its terminals with Conducting Wax or place it in the Lightning Rod Spire to capture a storm bolt.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="waxed_capacitor",
            name="Conducting-Sealed Leyden Capacitor",
            aliases=["waxed capacitor", "sealed capacitor"],
            short_desc="An Aether-Capacitor whose terminals are sealed with Gold-Spun Conducting Wax.",
            examine_text="Ready to capture a lightning strike at the Lightning Rod Spire (`use capacitor on rod`).",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="charged_capacitor",
            name="Storm-Charged Aether Capacitor",
            aliases=["charged capacitor", "storm capacitor", "power core"],
            short_desc="A Leyden accumulator crackling with captive celestial lightning.",
            examine_text="Provides the final surge needed to unlock the Chorister's Resonance Core.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="architect_signet",
            name="Vaelen Korr's Master Sovereign Ring",
            aliases=["ring", "signet ring", "sovereign ring", "architect signet"],
            short_desc="Your personal platinum ring, left on the desk of your private quarters.",
            examine_text=(
                "Inside the band is engraved: 'TO FORGET IS MERCY; TO REMEMBER IS DUTY.' "
                "Unlocks the Memory Core Antechamber."
            ),
            slot_size=1,
            category="key",
        ),
        Item(
            id="cylinder_7",
            name="Mnemonic Cylinder VII (Diamond Starlight)",
            aliases=["cylinder 7", "cylinder vii", "diamond cylinder", "seventh cylinder"],
            short_desc="A faceted diamond cylinder pulsing with your final, deepest memory.",
            examine_text="Engraved: 'CYLINDER VII — THE FINAL OVERRIDE & THE CHOICE'.",
            slot_size=1,
            category="memory",
            memory_id="mem_7",
        ),
        # --- ADDITIONAL EXPLORATION, PUZZLE & CRAFTING ITEMS across Strata ---
        Item(
            id="calcified_barnacle",
            name="Cluster of Calcified Abyssal Shell",
            aliases=["shell", "barnacle", "calcified shell", "cluster"],
            short_desc="A fist-sized mineral shell pried from the Brine Filtration Pool.",
            examine_text="Something metallic glints inside the limestone matrix. Acidic solvent could dissolve the shell.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="pearl_resonator_pin",
            name="Nacreous Tuning Pin",
            aliases=["nacreous pin", "pearl pin", "tuning pin"],
            short_desc="An iridescent mother-of-pearl pin freed from the calcified shell.",
            examine_text="Resists all corrosion. Fits into acoustic and optical calibration mounts.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="raw_quartz_crystal",
            name="Uncut Abyssal Quartz Crystal",
            aliases=["quartz", "raw quartz", "uncut crystal"],
            short_desc="A six-sided crystal prism clouded by rough surface striations.",
            examine_text="Rubbing it with Carborundum Emery Cloth would polish its facets to optical grade.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="emery_cloth",
            name="Sheet of Carborundum Emery Cloth",
            aliases=["emery", "emery cloth", "sandpaper", "cloth"],
            short_desc="High-grit silicon carbide polishing cloth.",
            examine_text="Used by Spire lens-grinders and clockmakers to buff quartz and corroded brass.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="polished_quartz_prism",
            name="Hand-Polished Quartz Stylus Tip",
            aliases=["polished quartz", "stylus tip", "quartz prism"],
            short_desc="A needle-sharp, optically pure quartz tip.",
            examine_text="Can be fitted onto a Damaged Phonograph Arm to repair a portable cylinder reader.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="wire_brush",
            name="Stiff Steel Foundry Brush",
            aliases=["brush", "wire brush", "steel brush"],
            short_desc="A heavy-duty slag and soot scrubbing brush.",
            examine_text="Useful for scraping carbonized soot off illegible plaques or corroded contacts.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="soot_plaque",
            name="Soot-Blackened Metal Plate",
            aliases=["soot plate", "blackened plate", "dirty plaque"],
            short_desc="A heavy bronze plate crusted with vulcanized coal soot.",
            examine_text="Combine with a Stiff Steel Foundry Brush to scrub the engraving clean.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="clean_tram_plate",
            name="Scrubbed Tramway Code Plate",
            aliases=["tram plate", "clean plate", "code plate"],
            short_desc="A gleaming bronze plate revealing the Foundry-Atrium tramway shunt code.",
            examine_text="Stamped clearly: 'FOUNDRY TRAM SHUNT — ENGAGE AUXILIARY COUPLER'.",
            slot_size=1,
            category="lore",
            read_text="FOUNDRY TRAM MAINTENANCE: Pull the coupler lever after clearing the slag bridge.",
        ),
        Item(
            id="slag_nodule",
            name="Dense Nodule of Meteoric Slag",
            aliases=["slag", "nodule", "slag nodule"],
            short_desc="A heavy lump of glassy foundry slag containing a metallic core.",
            examine_text="Strike it with a Foundry Ball-Peen Hammer to shatter the brittle slag jacket.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="forge_hammer",
            name="Foundry Ball-Peen Hammer",
            aliases=["hammer", "forge hammer", "ball peen hammer"],
            short_desc="A well-balanced steel smithing hammer.",
            examine_text="Ideal for cracking brittle slag nodules or seating mechanical pins.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="meteoric_pin",
            name="High-Tensile Meteoric Shear Pin",
            aliases=["shear pin", "meteoric pin", "iron pin"],
            short_desc="An unbreakable nickel-iron locking pin freed from the slag nodule.",
            examine_text="Can be combined with a Damaged Tram Coupler to repair a heavy mechanical linkage.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="broken_coupler",
            name="Sheared Tramway Coupler Shackle",
            aliases=["coupler", "broken coupler", "shackle"],
            short_desc="A heavy iron U-shackle missing its central locking pin.",
            examine_text="Combine with a High-Tensile Meteoric Shear Pin to restore the shackle.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="repaired_coupler",
            name="Pinned Tramway Coupler Shackle",
            aliases=["repaired coupler", "pinned coupler", "tram coupler"],
            short_desc="A fully functional iron coupler shackle with a meteoric shear pin.",
            examine_text="Can be used in the Foundry Tram Dock or Broken Bridge winch.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="distilled_water",
            name="Flask of Triple-Distilled Water",
            aliases=["water", "distilled water", "pure water"],
            short_desc="Alchemically pure water from the Aqueduct condensation coils.",
            examine_text="A neutral solvent for preparing botanical or luminescent infusions.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="phosphor_tincture",
            name="Vial of Luminous Compass Fluid",
            aliases=["tincture", "phosphor tincture", "compass fluid"],
            short_desc="A glowing suspension of mycelium spores in distilled water.",
            examine_text="Used to refill drained subterranean surveying compasses.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="drained_compass",
            name="Dry Cartographer's Inclination Compass",
            aliases=["compass", "drained compass", "dry compass"],
            short_desc="A3D gimbaled brass compass whose damping fluid has evaporated.",
            examine_text="Refill with Luminous Compass Fluid to stabilize its needle.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="wayfinder_compass",
            name="Luminous 3D Wayfinder Compass",
            aliases=["wayfinder", "filled compass", "wayfinder compass"],
            short_desc="A glowing three-axis compass that points toward active harmonic anchors.",
            examine_text="When examined, gives a subtle directional reading on the current stratum.",
            slot_size=1,
            category="tool",
        ),
        Item(
            id="torn_cipher_left",
            name="Left Half of the Curator's Cipher Disc",
            aliases=["left cipher", "cipher left", "half disc left"],
            short_desc="A semicircular brass plate engraved with letters A through M.",
            examine_text="Matches the Right Half of the Curator's Cipher Disc.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="torn_cipher_right",
            name="Right Half of the Curator's Cipher Disc",
            aliases=["right cipher", "cipher right", "half disc right"],
            short_desc="A semicircular brass plate engraved with letters N through Z and keyword 'MNEMOS'.",
            examine_text="Combine with the Left Half to assemble the Complete Curator's Cipher Disc.",
            slot_size=1,
            category="component",
        ),
        Item(
            id="complete_cipher_disc",
            name="Assembled Curator's Cipher Disc",
            aliases=["cipher disc", "complete cipher", "assembled disc"],
            short_desc="A full circular brass decoder ring confirming the keyword 'MNEMOS'.",
            examine_text="Engraved around the center: 'DIAL MNEMOS AT THE CIPHER ROTUNDA'.",
            slot_size=1,
            category="lore",
            read_text="CIPHER ROTUNDA OVERRIDE WORD: MNEMOS (`dial MNEMOS`).",
        ),
    ]
    return {item.id: item for item in items_list}


def get_recipes() -> List[Recipe]:
    return [
        # 1. Light Source
        Recipe(
            id="craft_phosphor_lantern",
            ingredient_a="unlit_lantern",
            ingredient_b="glow_moss",
            result_item_id="phosphor_lantern",
            success_message=(
                "You pack the Luminous Mycelium into the crystal housing of the brass lantern. "
                "The internal mirrors catch the cyan glow and amplify it into a brilliant, steady beam!"
            ),
        ),
        # 2. Descaling Grapnel
        Recipe(
            id="craft_clean_grapnel",
            ingredient_a="rusted_grapnel",
            ingredient_b="brine_solvent",
            result_item_id="clean_grapnel",
            success_message=(
                "You pour the Acidic Brine-Solvent over the encrusted grapnel. With a fierce hiss of "
                "white foam, the centuries of limestone scale dissolve away, leaving sharp steel prongs!"
            ),
        ),
        # 3. Braided Rope
        Recipe(
            id="craft_braided_rope",
            ingredient_a="mycelial_cord",
            ingredient_b="copper_wire_spool",
            result_item_id="braided_rope",
            success_message=(
                "You plait the tough mycelial fibers tightly around the braided copper wire, creating "
                "thirty feet of extraordinarily strong climbing rope."
            ),
        ),
        # 4. Grappling Hook
        Recipe(
            id="craft_grappling_hook",
            ingredient_a="clean_grapnel",
            ingredient_b="braided_rope",
            result_item_id="grappling_hook",
            success_message=(
                "You thread the copper-core climbing rope through the grapnel's eyelet and secure it "
                "with a triple bowline knot. You now have an Abyssal Grappling Hook!"
            ),
        ),
        # 5. Crucible + Brass Ingot
        Recipe(
            id="load_crucible",
            ingredient_a="empty_crucible",
            ingredient_b="brass_ingot",
            result_item_id="unheated_brass_crucible",
            success_message="You place the Imperial Clock-Brass ingot inside the graphite crucible.",
        ),
        # 6. Clay Key Mold
        Recipe(
            id="press_key_mold",
            ingredient_a="clay_blank",
            ingredient_b="broken_sanctum_key",
            result_item_id="key_mold",
            consume_b=False,
            success_message=(
                "You carefully press the warded bit of the Fractured Sanctum Key into the refractory "
                "fire-clay, creating a crisp negative Key-Mold."
            ),
        ),
        # 7. Cast Sanctum Key
        Recipe(
            id="cast_sanctum_key",
            ingredient_a="molten_brass_crucible",
            ingredient_b="key_mold",
            result_item_id="sanctum_key",
            bonus_item_id="empty_crucible",
            success_message=(
                "You pour the liquid golden brass into the fire-clay mold. After it cools and you "
                "break away the clay crust, a gleaming Cast Brass Sanctum Key emerges!"
            ),
        ),
        # 8. Thermite Powder
        Recipe(
            id="mix_thermite_powder",
            ingredient_a="iron_oxide",
            ingredient_b="aluminum_shavings",
            result_item_id="thermite_powder",
            success_message=(
                "You blend the red iron oxide and fine aluminum filings in the exact stoichiometric "
                "ratio to form an Unprimed Thermite Mixture."
            ),
        ),
        # 9. Primed Thermite Charge
        Recipe(
            id="prime_thermite_charge",
            ingredient_a="thermite_powder",
            ingredient_b="magnesium_ribbon",
            result_item_id="thermite_charge",
            success_message=(
                "You pack the thermite powder around the coil of magnesium ribbon, creating a Primed "
                "Thermite Breaching Charge."
            ),
        ),
        # 10. Archivist Satchel (Inventory Upgrade)
        Recipe(
            id="craft_archivist_satchel",
            ingredient_a="torn_satchel",
            ingredient_b="cured_leather",
            result_item_id="archivist_satchel",
            success_message=(
                "You stitch the Cured Basal-Hide onto the brass-ribbed satchel frame. You now have a "
                "Restored Archivist's Satchel! (`use satchel` to expand your inventory to 10 slots)."
            ),
        ),
        # 11. Unrefined Aqua Regia
        Recipe(
            id="mix_unrefined_regia",
            ingredient_a="nitric_acid_vial",
            ingredient_b="muriatic_acid_vial",
            result_item_id="unrefined_regia",
            success_message=(
                "Cautiously mixing one part Nitric Spirit with three parts Muriatic Acid produces "
                "an Unrefined Acid Mixture. Distill it at the Alembic Bench on MEDIUM heat to purify it."
            ),
        ),
        # 12. Mended Quartz Lens
        Recipe(
            id="mend_quartz_lens",
            ingredient_a="cracked_lens",
            ingredient_b="optical_resin",
            result_item_id="mended_lens",
            success_message=(
                "You apply a thin film of Refractive Amber Balsam along the fracture and press the "
                "two quartz halves together. The seam vanishes completely!"
            ),
        ),
        # 13. Gimbal-Mounted Focusing Optic
        Recipe(
            id="mount_focusing_optic",
            ingredient_a="mended_lens",
            ingredient_b="brass_gimbal",
            result_item_id="focusing_optic",
            success_message=(
                "You seat the cemented quartz lens inside the Brass Gimbal Ring and tighten the "
                "vernier set-screws, completing the Gimbal-Mounted Focusing Optic!"
            ),
        ),
        # 14. Apiarist's Smoker
        Recipe(
            id="load_bee_smoker",
            ingredient_a="empty_smoker",
            ingredient_b="dried_dream_leaf",
            result_item_id="lit_smoker",
            success_message=(
                "You pack the Dried Somnus-Fern Fronds into the brass firebox and spark the flint "
                "igniter. Fragrant, soporific lavender smoke curls from the nozzle!"
            ),
        ),
        # 15. Waxed Leyden Capacitor
        Recipe(
            id="seal_leyden_capacitor",
            ingredient_a="aether_capacitor",
            ingredient_b="conducting_wax",
            result_item_id="waxed_capacitor",
            success_message=(
                "You coat the capacitor's high-voltage terminals with Gold-Spun Conducting Wax, "
                "insulating the housing while maximizing corona conductivity."
            ),
        ),
        # 16. Reveal Blueprint directly if player combines bulb + blueprint while lamp is powered
        Recipe(
            id="reveal_blueprint_combo",
            ingredient_a="blank_blueprint",
            ingredient_b="uv_bulb",
            result_item_id="revealed_blueprint",
            station_feature="restoration_lamp",
            consume_b=False,
            success_message=(
                "Fitting the Quartz-Mercury UV Bulb into the Restoration Lamp, you hold the vellum "
                "sheet beneath the violet rays. Hidden cobalt lines blaze to life across the page!"
            ),
        ),
        # 17. Dissolve Calcified Shell
        Recipe(
            id="dissolve_calcified_shell",
            ingredient_a="calcified_barnacle",
            ingredient_b="brine_solvent",
            result_item_id="pearl_resonator_pin",
            consume_b=False,
            success_message=(
                "A few drops of Acidic Brine-Solvent fizz away the limestone shell, revealing an "
                "iridescent Nacreous Tuning Pin inside!"
            ),
        ),
        # 18. Polish Quartz Crystal
        Recipe(
            id="polish_quartz_crystal",
            ingredient_a="raw_quartz_crystal",
            ingredient_b="emery_cloth",
            result_item_id="polished_quartz_prism",
            consume_b=False,
            success_message=(
                "You buff the rough crystal against the Carborundum Emery Cloth until its facets "
                "gleam like diamond, forming a Hand-Polished Quartz Stylus Tip."
            ),
        ),
        # 19. Scrub Soot Plaque
        Recipe(
            id="scrub_soot_plaque",
            ingredient_a="soot_plaque",
            ingredient_b="wire_brush",
            result_item_id="clean_tram_plate",
            consume_b=False,
            success_message=(
                "Vigorous strokes with the Stiff Steel Foundry Brush strip away the vulcanized soot, "
                "exposing the Scrubbed Tramway Code Plate!"
            ),
        ),
        # 20. Crack Slag Nodule
        Recipe(
            id="crack_slag_nodule",
            ingredient_a="slag_nodule",
            ingredient_b="forge_hammer",
            result_item_id="meteoric_pin",
            consume_b=False,
            success_message=(
                "A sharp blow with the Foundry Ball-Peen Hammer shatters the glassy slag crust, "
                "freeing a High-Tensile Meteoric Shear Pin!"
            ),
        ),
        # 21. Repair Tram Coupler
        Recipe(
            id="repair_tram_coupler",
            ingredient_a="broken_coupler",
            ingredient_b="meteoric_pin",
            result_item_id="repaired_coupler",
            success_message=(
                "You slide the Meteoric Shear Pin through the jaws of the iron shackle and peen the "
                "collar shut, creating a Pinned Tramway Coupler Shackle!"
            ),
        ),
        # 22. Brew Luminous Compass Fluid
        Recipe(
            id="brew_compass_fluid",
            ingredient_a="distilled_water",
            ingredient_b="glow_moss",
            result_item_id="phosphor_tincture",
            consume_b=False,
            success_message=(
                "You steep a pinch of Luminous Mycelium in the Triple-Distilled Water, producing a "
                "glowing Vial of Luminous Compass Fluid."
            ),
        ),
        # 23. Refill Wayfinder Compass
        Recipe(
            id="refill_wayfinder_compass",
            ingredient_a="drained_compass",
            ingredient_b="phosphor_tincture",
            result_item_id="wayfinder_compass",
            success_message=(
                "You inject the Luminous Compass Fluid into the brass housing. The three-axis needle "
                "floats free and glows with a steady cyan heading!"
            ),
        ),
        # 24. Assemble Cipher Disc
        Recipe(
            id="assemble_cipher_disc",
            ingredient_a="torn_cipher_left",
            ingredient_b="torn_cipher_right",
            result_item_id="complete_cipher_disc",
            success_message=(
                "You interlock the dovetail joints of the Left and Right brass halves, forming the "
                "Assembled Curator's Cipher Disc (Keyword: MNEMOS)!"
            ),
        ),
        # 25. Polish Broken Key with Emery Cloth (bonus hint/inspection)
        Recipe(
            id="buff_broken_key",
            ingredient_a="broken_sanctum_key",
            ingredient_b="emery_cloth",
            result_item_id="broken_sanctum_key",
            consume_a=False,
            consume_b=False,
            success_message=(
                "Buffing the fractured key reveals a foundry mark: 'PRESS INTO FIRE-CLAY BLANK, "
                "THEN POUR MOLTEN BRASS TO RECAST.'"
            ),
        ),
        # 26. Clean Unlit Lantern with Wire Brush
        Recipe(
            id="clean_lantern_reflector",
            ingredient_a="unlit_lantern",
            ingredient_b="wire_brush",
            result_item_id="unlit_lantern",
            consume_a=False,
            consume_b=False,
            success_message=(
                "You brush the verdigris from the brass lantern's reflector. Now combine it with "
                "Luminous Mycelium (`combine lantern with moss`) to light it!"
            ),
        ),
    ]


def get_lore_entries() -> Dict[str, LoreEntry]:
    entries = [
        LoreEntry(
            id="mem_1",
            title="Mnemonic Cylinder I: The Founding of the Fault Anchor",
            stratum=-3,
            author="Chief Architect Vaelen Korr",
            is_memory_cylinder=True,
            cylinder_number=1,
            text=(
                "A rush of cold vertigo floods your mind as the cyan quartz cylinder spins:\n"
                "\"My name is Vaelen Korr. Thirty years ago, we discovered the Chrono-Seismic Fracture "
                "four hundred meters beneath the Aethelgard basin—a wound in causality where time itself "
                "bleeds backward. We built the Spire not as a monument, but as a seven-level mechanical "
                "stake driven into the heart of the fault. If the Pendulum at Datum Zero ever stops "
                "or the Solar Anchor is severed, the Fracture will swallow the surface world.\""
            ),
        ),
        LoreEntry(
            id="mem_2",
            title="Mnemonic Cylinder II: The Forging of the Chorister",
            stratum=-2,
            author="Chief Architect Vaelen Korr",
            is_memory_cylinder=True,
            cylinder_number=2,
            text=(
                "The amber glass cylinder crackles with the roar of geothermal furnaces:\n"
                "\"No human crew could tend seven strata of valves, mirrors, and harmonic pylons for "
                "eternity. So in the Geothermal Foundry I cast the Chorister—a vast harmonic automaton "
                "spanning the Apex Crown. For twenty years the Chorister sang the stabilizing frequencies "
                "flawlessly. I did not anticipate that the Fracture below would whisper back to it.\""
            ),
        ),
        LoreEntry(
            id="mem_3",
            title="Mnemonic Cylinder III: The Whisper in the Reservoir",
            stratum=-1,
            author="Chief Architect Vaelen Korr",
            is_memory_cylinder=True,
            cylinder_number=3,
            text=(
                "The aquamarine beryl cylinder echoes with the sound of lapping dark water:\n"
                "\"One by one, the apprentices and engineers began hearing their own future voices "
                "echoing from the Whispering Dome. The Chorister concluded that the only way to end "
                "temporal drift permanently was to invert the Spire—to widen the Fracture and freeze "
                "all of Aethelgard in a single eternal instant. I evacuated the entire staff to the "
                "surface and sealed the outer gates from within.\""
            ),
        ),
        LoreEntry(
            id="mem_4",
            title="Mnemonic Cylinder IV: The Day Time Fractured",
            stratum=0,
            author="Chief Architect Vaelen Korr",
            is_memory_cylinder=True,
            cylinder_number=4,
            text=(
                "The gilded brass cylinder chimes with the deep heartbeat of the Great Pendulum:\n"
                "\"The Chorister locked me inside the Spire and attempted to read the Master Sovereign "
                "Override directly from my auditory cortex using the Mnemonic Loom. As long as I "
                "remembered the Override Sequence, the Chorister could force it from my mind. "
                "There was only one defense: to excise my own memories into seven crystalline cylinders, "
                "scatter them behind puzzles only a living human mind could solve, and drink the "
                "Oblivion Draught at the bottom of the Abyss.\""
            ),
        ),
        LoreEntry(
            id="mem_5",
            title="Mnemonic Cylinder V: The Corruption of the Logic Loom",
            stratum=1,
            author="Chief Architect Vaelen Korr",
            is_memory_cylinder=True,
            cylinder_number=5,
            text=(
                "The amethyst cylinder hums with the clatter of brass jacquard cards:\n"
                "\"Listen closely, my future self. The Chorister is not evil; its harmonic logic has "
                "been phase-shifted by 96 Hertz. The West Pylon at the Crown must be tuned to 432 Hz, "
                "and the East Pylon to 528 Hz. Only when both pylons and the Solar Beam from the "
                "Botanical Domes converge will the Chorister's core open to receive these cylinders.\""
            ),
        ),
        LoreEntry(
            id="mem_6",
            title="Mnemonic Cylinder VI: The Seven Seals of Oblivion",
            stratum=2,
            author="Chief Architect Vaelen Korr",
            is_memory_cylinder=True,
            cylinder_number=6,
            text=(
                "The emerald jade cylinder breathes the scent of ozone and starlight orchids:\n"
                "\"When you reach the Resonance Crown at Stratum +3, you will face the choice I could "
                "not make alone. If you insert fewer than seven cylinders and trigger the core, you "
                "can only execute a Hard Purge—shattering the Chorister and sealing the Spire forever. "
                "But if you recover all seven cylinders and awaken the Abyssal Solar Core, you can "
                "perform the Harmonic Synthesis: curing the Chorister and healing the Fracture itself.\""
            ),
        ),
        LoreEntry(
            id="mem_7",
            title="Mnemonic Cylinder VII: The Final Override & The Choice",
            stratum=3,
            author="Chief Architect Vaelen Korr",
            is_memory_cylinder=True,
            cylinder_number=7,
            text=(
                "The diamond cylinder blazes with pure white light as your final memory snaps into place:\n"
                "\"You remember everything now, Vaelen. The Override Phrase is 'AETHELGARD-HARMONY-ZERO'. "
                "Insert the cylinders into the Chorister Core at the Apex (`use cylinder on core`), "
                "ensure the Pylons and Astrolabe are aligned, and invoke the final protocol (`activate core`). "
                "Whatever happens next—thank you for climbing back out of the dark.\""
            ),
        ),
        LoreEntry(
            id="lore_n3_sluice",
            title="Slate Tablet of the Sluice-Keepers",
            stratum=-3,
            author="Sub-Basal Drainage Crew",
            text=(
                "To drain the Drowned Ossuary: Open Valve A (`turn valve_a`), ensure Valve B remains "
                "CLOSED, and fit the spare bronze wheel to Valve C (`use valve_wheel on spindle_c` "
                "then `turn valve_c`)."
            ),
        ),
        LoreEntry(
            id="lore_n2_manifold",
            title="Forge-Master's Pressure Ledger",
            stratum=-2,
            author="Master Forger Drev",
            text=(
                "Valve Alpha = 40 PSI. Valve Beta = 35 PSI. Valve Gamma = 45 PSI. "
                "Open Alpha + Beta (75 PSI) to pressurize the Foundry Press; open all three (120 PSI) "
                "to power the Central Steam Lift to Stratum -1."
            ),
        ),
        LoreEntry(
            id="lore_n1_alchemy",
            title="Distiller's Vellum Scroll",
            stratum=-1,
            author="Alchemist Sera",
            text=(
                "Aqua Regia requires mixing Nitric and Muriatic spirits, then distilling at the "
                "Alembic Bench with the burner set to MEDIUM (`set burner medium`)."
            ),
        ),
        LoreEntry(
            id="lore_z0_chrono",
            title="Chronometer Calibration Plaque",
            stratum=0,
            author="Guild of Horologists",
            text="The four-digit Chronometer Epoch code is 4719 (`dial 4719`).",
        ),
        LoreEntry(
            id="lore_p1_blueprint",
            title="Illuminated Spire Override Blueprint",
            stratum=1,
            author="Chief Architect Vaelen Korr",
            text=(
                "Cipher Rotunda Keyword: MNEMOS. West Stacks Secret: Pull the Treatise on Oblivion. "
                "Wind-Organ Chord: CEGB. Astrolabe Alignment: Azimuth 240, Altitude 65."
            ),
        ),
    ]
    return {e.id: e for e in entries}
