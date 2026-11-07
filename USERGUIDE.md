# 📖 User Guide: *Echoes of the Aethelgard Spire*

Welcome to the official player manual for **Echoes of the Aethelgard Spire**. This guide covers the terminal user interface, complete command reference, 3D navigation, inventory and crafting mechanics, note-taking, save management, and optional spoiler-tagged hints for all seven strata.

---

## 📑 Table of Contents
1. [Story Premise & Objective](#1-story-premise--objective)
2. [Understanding the Terminal UI](#2-understanding-the-terminal-ui)
3. [Complete Command Reference](#3-complete-command-reference)
4. [3D Navigation & The Fog-of-War Mini-Map](#4-3d-navigation--the-fog-of-war-mini-map)
5. [Inventory Management, Dropping, & Pneumatic Lockers](#5-inventory-management-dropping--pneumatic-lockers)
6. [Item Combinations & Crafting](#6-item-combinations--crafting)
7. [Taking Field Notes & Reviewing Your Journal](#7-taking-field-notes--reviewing-your-journal)
8. [Save & Load System](#8-save--load-system)
9. [Multiple Endings Guide](#9-multiple-endings-guide)
10. [Spoiler-Protected Stratum & Recipe Reference](#10-spoiler-protected-stratum--recipe-reference)

---

## 1. Story Premise & Objective

You awaken on a wet black obsidian slab at the bottom of **The Aethelgard Spire** (`Stratum -3`, 420 meters below sea level) with complete amnesia. Beside you lies an empty phial labeled *SELF-ADMINISTERED OBLIVION DRAUGHT*.

As you explore the Spire's seven vertical levels (`Z = -3` up to `Z = +3`), you discover that there is **no combat**—your true adversary is the Spire's intricate web of mechanical, alchemical, optical, and harmonic locks that you yourself designed before erasing your own memory.

### Your Goals:
1. **Illuminate the Dark & Ascend**: Craft a working light source and climb from the Abyss (`Z = -3`) to the Celestial Observatory & Resonance Crown (`Z = +3`).
2. **Recover the 7 Mnemonic Cylinders**: Each stratum guards a crystalline phonograph cylinder containing a chapter of your erased past. Play them on any **Mnemonic Resonator** (`play cylinder <1-7>`) to restore your memories.
3. **Awaken the Cross-Stratum Solar Core**: Align the Heliostat Mirrors and Focusing Optic on `Z = +2` and open the Atrium Shutter on `Z = 0` so sunlight spears all the way down to the Abyssal Solar Core on `Z = -3`.
4. **Resolve the Crisis at the Apex**: Enter the Resonance Crown at `(0, 2, +3)` and activate the Chorister Core (`activate core`).

---

## 2. Understanding the Terminal UI

The game interface is divided into four distinct panels that automatically adapt their color theme to your current stratum:

### A. Telemetry Header Bar (Top)
- **Stratum & Biome Name**: Displays which of the 7 vertical strata you are currently exploring.
- **Pos `(X, Y, Z)` & Elevation**: Your exact 3D grid coordinates and vertical elevation in meters relative to Datum Zero (`0m`).
- **Inventory Gauge**: Visual progress bar (`[██████░░] 6/8 Slots`) showing how much carrying capacity you have used.
- **Memories (`◈◈◈◇◇◇◇`)**: Shows how many of the 7 Mnemonic Cylinders you have played back.
- **Notes / Explored / Turns**: Tracks your recorded field notes, total discovered chambers out of 88, and turn count.

### B. Chamber View (Left Panel)
- **Room Title & Description**: Atmospheric description of your current location, including dynamic updates when puzzles are solved (e.g., drained floodwaters, spinning turbines, active solar beams).
- **✦ Fixtures**: Interactive objects built into the room (e.g., `[valve_a]`, `[furnace]`, `[alembic]`, `[resonator]`, `[locker]`). You can inspect (`x <fixture>`) or interact with (`turn`, `pull`, `set`, `use <item> on <fixture>`) any listed fixture.
- **❖ Items Here**: Portable items currently lying on the floor, along with their slot size (`1 slot` or `2 slots`).
- **⇄ Exits**: Available horizontal (`NORTH`, `SOUTH`, `EAST`, `WEST`) and vertical (`UP ↕`, `DOWN ↕`) exits. Locked exits are highlighted in red (`[NORTH: Drowned Ossuary (Locked)]`).
- **✎ Room Note**: If you have written a field note in this chamber, the most recent note is pinned directly to the room view.
- **Action Feedback**: Appears at the bottom of the Chamber View after every command.

### C. Fog-of-War Mini-Map (Right Panel)
- Displays a live 2D coordinate grid of your current vertical stratum (`Z`).
- **Only shows chambers you have visited**, plus `[?]` markers for unexplored rooms directly connected to a visited room.

### D. Quick Command Footer (Bottom)
- A persistent cheat-sheet of the most common commands.

---

## 3. Complete Command Reference

The parser accepts natural commands and shorthand aliases (case-insensitive):

### Navigation
| Command | Shorthand / Aliases | Description |
| :--- | :--- | :--- |
| `north` | `n`, `go north` | Move one chamber north (`Y + 1`) |
| `south` | `s`, `go south` | Move one chamber south (`Y - 1`) |
| `east` | `e`, `go east` | Move one chamber east (`X + 1`) |
| `west` | `w`, `go west` | Move one chamber west (`X - 1`) |
| `up` | `u`, `climb`, `ascend` | Ascend one vertical stratum (`Z + 1`) |
| `down` | `d`, `descend` | Descend one vertical stratum (`Z - 1`) |

### Observation & Inspection
| Command | Shorthand / Aliases | Description |
| :--- | :--- | :--- |
| `look` | `l` | Refresh the current chamber description |
| `examine <target>` | `x <target>`, `inspect`, `search` | Examine an inventory item, floor item, room fixture, or exit |
| `read <item>` | `study <item>`, `decipher` | Read text on tablets, ledgers, scrolls, plaques, or blueprints |

### Inventory, Dropping, & Storage
| Command | Shorthand / Aliases | Description |
| :--- | :--- | :--- |
| `inventory` | `i`, `inv` | List all carried items, slot sizes, and Pneumatic Locker contents |
| `take <item>` | `get <item>`, `grab`, `pick up` | Pick up an item from the current chamber |
| `take all` | `get all` | Pick up all items in the room until inventory slots are full |
| `drop <item>` | `discard <item>`, `leave` | Drop an item onto the current chamber's floor (persists forever) |
| `stash <item>` | `deposit <item>`, `store` | Store an item in the Pneumatic Locker network (at any `[locker]` room) |
| `retrieve <item>` | `withdraw <item>`, `fetch` | Retrieve a stored item from the Pneumatic Locker network |
| `locker` | — | View all items currently stored inside the Pneumatic Locker network |

### Item Combination & Crafting
| Command | Shorthand / Aliases | Description |
| :--- | :--- | :--- |
| `combine <A> with <B>` | `craft <A> with <B>`, `mix <A> and <B>` | Combine two items in your inventory (or room) to create a new item |

### Puzzle & Fixture Interactions
| Command | Examples | Description |
| :--- | :--- | :--- |
| `use <item>` | `use satchel` | Use a standalone upgrade or item |
| `use <item> on <target>` | `use grappling_hook on shaft`<br>`use sanctum_key on up`<br>`use unrefined_regia on alembic` | Use a tool, key, or reagent on a room fixture or locked exit |
| `turn <target>` | `turn valve_a`<br>`turn valve_alpha`<br>`turn mirror_north` | Turn a valve wheel, winch, or mirror |
| `pull <target>` | `pull winch`<br>`pull shutter`<br>`pull brake`<br>`pull treatise` | Pull a mechanical lever, clutch, shutter, or secret book spine |
| `set <target> <value>` | `set burner medium`<br>`set dish focus`<br>`set mirror_north center`<br>`set astrolabe 240 65` | Adjust a burner, parabolic dish, heliostat mirror, or astrolabe |
| `dial <value>` | `dial 4719`<br>`dial MNEMOS` | Enter a numeric code or cipher keyword on a dial/rotunda |
| `play <target>` | `play cylinder 1`<br>`play sol mi do la`<br>`play CEGB` | Play a Mnemonic Cylinder on a Resonator, strike chimes, or play the Wind-Organ |
| `insert cylinders` | `use cylinder_7 on core` | Load carried Mnemonic Cylinders into the Chorister Core at the Apex |
| `activate core` | — | Trigger the final culmination sequence inside The Resonance Crown |

### Map, Notebook, & Journal
| Command | Examples | Description |
| :--- | :--- | :--- |
| `map` | `m` | Open the detailed Fog-of-War map & room list for your current stratum |
| `map <z>` | `map -3`, `map 0`, `map +2` | Inspect the Fog-of-War map for any previously visited stratum (`-3` to `+3`) |
| `map vertical` | `map spire`, `map all` | View a vertical cross-section of all 7 strata and exploration percentages |
| `note add <text>` | `note <text>` | Pin a new note to your current room and 3D coordinates |
| `note tag <tag> <text>` | `note tag code Chrono is 4719` | Record a note with a custom category tag |
| `notes` | `note list` | List all recorded notes across the Spire |
| `notes <filter>` | `notes code`, `notes sluice` | Filter notes by tag, room name, or keyword |
| `note del <id>` | `note delete 2` | Delete a note by its ID number |
| `journal` | `lore`, `memories` | Read all unlocked Lore Documents and restored Mnemonic Cylinder transcripts |

### System & Assistance
| Command | Shorthand | Description |
| :--- | :--- | :--- |
| `hint` | `clue` | Receive a context-sensitive hint for your current room or stratum |
| `status` | `score`, `progress` | View overall exploration stats, puzzles solved, and Solar Core status |
| `save [slot]` | `save`, `save before_lift` | Save your game to `quicksave` (default) or a custom named slot |
| `load [slot]` | `load`, `load autosave` | Load a saved game from `quicksave` or a named slot |
| `saves` | — | List all available save slots with timestamps and metadata |
| `help` | `h`, `?` | Display the in-game command summary |
| `quit` | `q`, `exit` | Exit the game |

---

## 4. 3D Navigation & The Fog-of-War Mini-Map

Every chamber in the Spire occupies a unique 3D coordinate `(X, Y, Z)`:
- `X` runs **West (`-`)** to **East (`+`)**.
- `Y` runs **South (`-`)** to **North (`+`)**.
- `Z` runs **Down (`-3`)** to **Up (`+3`)**.

### Mini-Map Legend
- `[★]` — **Your Current Position**
- `[●]` — **Explored Chamber**
- `[▲]` — **Explored Chamber with an UP (`Z + 1`) connection**
- `[▼]` — **Explored Chamber with a DOWN (`Z - 1`) connection**
- `[↕]` — **Explored Chamber with both UP and DOWN connections**
- `[♦]` — **Explored Chamber containing portable items on the floor**
- `[✎]` — **Explored Chamber where you have pinned a Field Note**
- `[?]` — **Unexplored Chamber** adjacent to a visited room
- `───` / ` │ ` — **Open Passageway**
- `─╫─` / ` ╫ ` — **Locked Doorway or Barrier**

> **Tip:** Whenever you drop an item (`drop <item>`), that chamber's icon on the mini-map changes to `[♦]`, and typing `map` lists the exact items waiting in each explored room on that stratum!

---

## 5. Inventory Management, Dropping, & Pneumatic Lockers

1. **8-Slot Starting Capacity**: Most items occupy `1 slot`, while heavy equipment (such as the *Pressurized Brass Diving Hood* or the *15-kg Lead Trim-Weight*) occupies `2 slots`.
2. **Expanding to 10 Slots**: On Stratum -3, you can find the **Torn Archivist's Satchel Frame** (in the *Drowned Ossuary*) and the **Roll of Cured Basal-Hide** (in the *Calcified Cistern*). Combine them (`combine torn_satchel with cured_leather`) and run `use satchel` to permanently expand your capacity to **10 slots**!
3. **Dropping Items**: You can `drop <item>` in any chamber. Dropped items never despawn and are indexed on your full stratum map (`map`).
4. **Pneumatic Dispatch Lockers**: Five chambers across the Spire feature a `[locker]` terminal (*Pneumatic Dispatch Hub* on `Z = -2`, *Pneumatic Locker Room* on `Z = 0`, *Curator's Private Study* on `Z = +1`, *Celestial Elevator Lobby* on `Z = +2`, and *Observatory Arrival Platform* on `Z = +3`). Any item you `stash <item>` at one terminal can be retrieved via `retrieve <item>` at any other terminal!

---

## 6. Item Combinations & Crafting

To combine two items, use:
```text
combine <item_a> with <item_b>
```
- Order does not matter (`combine lantern with moss` is identical to `combine moss with lantern`).
- Partial item names work (`combine grapnel with solvent`).
- Most combinations can be performed anywhere, while a few specialized processes require a room fixture (for example, melting the brass ingot in the crucible uses the `furnace` at the *Magma Siphon Bridge*: `use brass_crucible on furnace`).
- Combining two 1-slot items into a single crafted item frees up an inventory slot!

---

## 7. Taking Field Notes & Reviewing Your Journal

As you explore the Spire, you will encounter valve calibration numbers, four-note acoustic melodies, cipher keywords, and astrolabe coordinates.
- **Write a quick note**: `note add Boiler valves: Alpha=40, Beta=35, Gamma=45`
- **Write a tagged note**: `note tag cipher Rotunda word is MNEMOS`
- **Review all notes**: `notes`
- **Search notes by tag or word**: `notes cipher`
- **Delete a completed note**: `note del 1`
- **Review Lore & Cylinders**: Type `journal` at any time to re-read every tablet, ledger, scroll, blueprint, and Mnemonic Cylinder you have discovered—even if you later dropped or stashed the physical lore item to save inventory space!

---

## 8. Save & Load System

- **Quick Save**: Type `save` to save immediately to `saves/quicksave.json`.
- **Named Save Slots**: Type `save <name>` (e.g., `save stratum_0_start`) to create a separate save file in `saves/`.
- **Automatic Autosaves**: Every time you climb `up` or descend `down` into a new vertical stratum, the game automatically writes to `saves/autosave.json`.
- **Listing & Loading**: Type `saves` to see all available save slots with their room name, stratum, memory count, and timestamp, then type `load <name>` to resume.

---

## 9. Multiple Endings Guide

When you reach **The Resonance Crown (Apex)** at `(0, 2, +3)` and run `activate core`, the ending you achieve depends on your thoroughness across the Spire:

1. **🌟 True Ending — *The Harmonic Synthesis of Aethelgard***:
   - **Requirements**: Recover all **7 Mnemonic Cylinders** (`cylinder_1` through `cylinder_7`) **AND** awaken the **Abyssal Solar Core** on Stratum -3 (by aligning both Heliostat Mirrors to `center` and installing the `focusing_optic` on Stratum +2 while the Atrium `shutter` on Stratum 0 is open).
2. **🔷 Standard Ending — *Restoration of the Sovereign Anchor***:
   - **Requirements**: Recover at least **5 of the 7 Mnemonic Cylinders** and activate the core (without awakening the Abyssal Solar Core or missing 1–2 cylinders).
3. **🔶 Fallback Ending — *The Oblivion Containment Purge***:
   - **Requirements**: Activate the core with fewer than 5 Mnemonic Cylinders recovered.

---

## 10. Spoiler-Protected Stratum & Recipe Reference

<details>
<summary><strong>🔍 Click to Reveal: Key Crafting Recipes (Spoilers)</strong></summary>

| Result Item | Ingredient A | Ingredient B | Notes |
| :--- | :--- | :--- | :--- |
| **Phosphor Lantern** | `unlit_lantern` | `glow_moss` | Essential light source for dark rooms |
| **Descale-Polished Grapnel** | `rusted_grapnel` | `brine_solvent` | Step 1 of Grappling Hook |
| **Copper-Core Climbing Rope** | `mycelial_cord` | `copper_wire_spool` | Step 2 of Grappling Hook |
| **Abyssal Grappling Hook** | `clean_grapnel` | `braided_rope` | Climbs the Whispering Fissure (`Z=-3` to `Z=-2`) |
| **Restored Archivist's Satchel** | `torn_satchel` | `cured_leather` | `use satchel` for **10 inventory slots** |
| **Crucible with Brass Ingot** | `empty_crucible` | `brass_ingot` | Melt at Magma Siphon (`use crucible on furnace`) |
| **Impressed Clay Key-Mold** | `clay_blank` | `broken_sanctum_key` | Mold for the Steam Lift key |
| **Cast Brass Sanctum Key** | `molten_brass_crucible` | `key_mold` | Unlocks the Steam Lift (`Z=-2` to `Z=-1`) |
| **High-Tensile Meteoric Shear Pin** | `slag_nodule` | `forge_hammer` | Cracks the slag nodule |
| **Pinned Tramway Coupler Shackle** | `broken_coupler` | `meteoric_pin` | Extends the Western Cantilever Span (`Z=0`) |
| **Flask of Unrefined Acid Mixture** | `nitric_acid_vial` | `muriatic_acid_vial` | Distill at Alembic on `medium` heat -> **Aqua Regia** |
| **Cemented Aether-Quartz Lens** | `cracked_lens` | `optical_resin` | Step 1 of Focusing Optic |
| **Gimbal-Mounted Focusing Optic** | `mended_lens` | `brass_gimbal` | Install in Prism Tower (`Z=+2`) |
| **Illuminated Spire Blueprint** | `blank_blueprint` | `uv_bulb` | Combine in Parchment Restoration Lab (`Z=+1`) |
| **Smoldering Somnus-Fern Smoker** | `empty_smoker` | `dried_dream_leaf` | Calms the Brass Bees in the Apiary (`Z=+2`) |
| **Conducting-Sealed Capacitor** | `aether_capacitor` | `conducting_wax` | Charge at Lightning Rod Spire (`Z=+3`) |

</details>

<details>
<summary><strong>🗺️ Click to Reveal: Stratum-by-Stratum Puzzle Solutions (Spoilers)</strong></summary>

- **Stratum -3 (The Bioluminescent Abyss)**:
  1. Craft the `phosphor_lantern` (`unlit_lantern` + `glow_moss`).
  2. Grab `valve_wheel` from the *Submerged Bell-Dock*. In *Sluice Control Niche*, `turn valve_a`, keep `valve_b` closed, and `use valve_wheel on spindle_c` to drain the *Drowned Ossuary*. Collect **Cylinder I** and `torn_satchel`.
  3. Craft `archivist_satchel` (`torn_satchel` + `cured_leather`) and `use satchel`.
  4. Craft `grappling_hook` and `use grappling_hook on shaft` in *Whispering Fissure*, then go `up`.
- **Stratum -2 (The Geothermal Foundry)**:
  1. In *Counterweight Winch Room*, `pull winch` and take `insulated_gauntlets`.
  2. In *Boiler Manifold Hall*, open `valve_alpha`, `valve_beta`, and `valve_gamma` (120 PSI).
  3. Quench the molten slag in *Obsidian Cooling Vats* (`use cryo_canister on slag`) and go south to collect **Cylinder II** and `slag_nodule`.
  4. Cast `sanctum_key` (`empty_crucible` + `brass_ingot` -> melt at `furnace` -> combine with `key_mold`), then `use sanctum_key on up` in *Pressure Regulation Vault*.
- **Stratum -1 (The Sunken Aqueducts & Labs)**:
  1. In *Canal Lock Control*, `use sluice_crank on lock_winch` to float the pontoon bridge.
  2. In *Whispering Acoustic Dome*, `set dish focus` (reveals chime sequence `SOL - MI - DO - LA`) and take `beveled_gear`.
  3. Mix `nitric_acid_vial` + `muriatic_acid_vial`, `set burner medium` in *Alchemical Distillery*, and `use unrefined_regia on alembic` to get `aqua_regia`.
  4. In *Glassblower's Annex*, `use aqua_regia on north` to enter *Sunken Crypt of the Founders* and collect **Cylinder III**. Ascend at *Aqueduct Spiral Stair*.
- **Stratum 0 (The Grand Clockwork Atrium)**:
  1. Take `chime_mallet` from *Maintainer's Barracks*, go to *Acoustic Chime Balcony*, and `play sol mi do la` to unlock *Hall of the Seven Anchors* (**Cylinder IV**).
  2. In *Sun-Shaft Balcony*, `pull shutter` to open the vertical solar aperture.
  3. In *North Gear-Train Gallery*, `use beveled_gear on spindle`. In *Chronometer Control Booth*, `dial 4719`.
  4. In *West Tramway Concourse*, `use repaired_coupler on west`, take `lead_counterweight` and `copper_fuse`, hang the weight in *Vault of Weights* (`use lead_counterweight on cradle`), and `pull brake` in *South Escapement Hall*. Ascend from *Central Pendulum Rotunda*.
- **Stratum +1 (The Mnemonic Archives)**:
  1. In *West Stacks*, `pull treatise` to open the *Secret Vault* (**Cylinder V** and `tuning_fork_432`).
  2. Combine `blank_blueprint` (from *Curator's Study*) with `uv_bulb` (from *Listening Booths*) in *Parchment Restoration Lab*.
  3. In *Cipher Rotunda*, `dial MNEMOS`. In *Paternoster Lift Landing*, `use copper_fuse on fusebox` and go `up`.
- **Stratum +2 (The Aetherial Botanical Domes)**:
  1. `set mirror_north center`, `set mirror_south center`, and `use focusing_optic on cradle` in *Prism Refraction Tower* (this awakens the Abyssal Solar Core on Stratum -3!).
  2. `use starlight_pollen on orchid` in *Starlight Orchid Grove* to get `tuning_fork_528`.
  3. `use lit_smoker on hive` in *Apiary of Brass Bees* to get `conducting_wax`.
  4. In *Wind-Organ Loft*, take **Cylinder VI** and `play CEGB` to power the Celestial Elevator (`up`).
- **Stratum +3 (The Celestial Observatory & Crown)**:
  1. In *Architect's Living Quarters*, take `architect_signet` and **Cylinder VII** (`play cylinder_7`).
  2. Combine `aether_capacitor` + `conducting_wax` and `use waxed_capacitor on rod` at *Lightning Rod Spire*.
  3. At *Astrolabe Calibration Deck*, `set astrolabe 240 65`.
  4. At *West Harmonic Pylon*, `use tuning_fork_432 on pylon`. At *East Harmonic Pylon*, `use tuning_fork_528 on pylon`.
  5. Unlock *Memory Core Antechamber* (`use architect_signet on north`), `use charged_capacitor on receptacle`, move `north` into *The Resonance Crown*, and run `activate core`!

</details>
