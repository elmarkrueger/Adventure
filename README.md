# ❖ Echoes of the Aethelgard Spire

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python)
![UI Library](https://img.shields.io/badge/UI-Rich%20Terminal-bright_cyan?style=flat-square)
![World Scale](https://img.shields.io/badge/World-7%20Strata%20%7C%2088%20Chambers-gold?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

> *"Cold brine laps against your fingers. You open your eyes to a cathedral of wet black basalt four hundred meters beneath the earth. You cannot remember your name, how you descended into this chasm, or why your hand clutches an empty quartz phial labeled 'OBLIVION DRAUGHT'..."*

**Echoes of the Aethelgard Spire** is a vast, non-combat, 3D terminal text adventure written in Python. Set inside a mile-deep subterranean-to-celestial clockwork and alchemical megastructure, the game challenges you to navigate horizontally (`N`, `S`, `E`, `W`) and vertically (`UP`, `DOWN`) across **seven distinct vertical strata (`Z = -3` to `Z = +3`)**, solve interconnected mechanical, optical, alchemical, and acoustic puzzles, manage a strict slot-limited inventory, chart a fog-of-war mini-map, take field notes, and recover the seven crystalline **Mnemonic Cylinders** holding your erased past.

---

## ✨ Key Features

- **Vast 3D Vertical World (7 Strata, 88 Interconnected Chambers)**:
  - Ascend nearly a kilometer from **The Bioluminescent Abyss (`Z = -3`, -420m)** through **The Geothermal Foundry (`Z = -2`)**, **The Sunken Aqueducts & Alchemical Labs (`Z = -1`)**, **The Grand Clockwork Atrium (`Z = 0`, Datum Horizon)**, **The Mnemonic Archives (`Z = +1`)**, and **The Aetherial Botanical Domes (`Z = +2`)** to **The Celestial Observatory & Resonance Crown (`Z = +3`, +500m)**.
- **Non-Combat Environmental & Cross-Level Puzzles (30+ Puzzles)**:
  - Actions on one vertical stratum physically affect levels above or below—align heliostat mirrors on `Z = +2` and open the iris shutter on `Z = 0` to fire a concentrated solar beam 730 meters down into the Abyssal Solar Core on `Z = -3`, or balance high-pressure geothermal steam valves on `Z = -2` to power lifts ascending to `Z = -1`.
- **Tactical Inventory & Deep Item Crafting (92 Items, 26 Recipes)**:
  - Manage a strict **8-slot inventory limit** (upgradable to **10 slots** by crafting and equipping the *Restored Archivist's Satchel*).
  - Combine items (`combine <itemA> with <itemB>`), drop items persistently on any chamber floor (`drop <item>`), or send items across strata via the **Pneumatic Dispatch Locker Network** (`stash <item>` / `retrieve <item>`).
- **Polished `rich` Split-Screen Terminal UI**:
  - Dynamic color palettes tailored to each stratum's biome.
  - Real-time header telemetry (3D coordinates `(X, Y, Z)`, elevation meter, visual slot gauge, restored memory counter, exploration progress).
- **Live Fog-of-War Mini-Map**:
  - Automatically renders an ASCII/Unicode 2D grid of your current stratum showing **only the chambers you have already explored** (`[★]`, `[●]`, `[▲]`, `[▼]`, `[↕]`, `[♦]`, `[✎]`), locked doors (`╫`), and directly adjacent unexplored rooms (`[?]`).
  - Inspect any explored level (`map -3` through `map +3`) or view a vertical cross-section of the entire Spire (`map vertical`).
- **In-Game Architect's Field Notebook & Lore Journal**:
  - Pin custom, coordinate-stamped notes to any room (`note add <text>`, `note tag <tag> <text>`), search/filter notes (`notes <keyword>`), and review recovered lore documents and memory transcripts (`journal`).
- **Multi-Slot Save & Autosave System**:
  - Save progress anytime to named JSON slots (`save <slot_name>`, `load <slot_name>`, `saves`) with SHA-256 integrity verification, plus automatic `autosave` whenever you transition between vertical strata.

---

## 🖥️ Terminal UI Preview

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║ ❖ THE AETHELGARD SPIRE │ Stratum -3: The       Pos: (1, 0, -3) │ Elev: -420m ║
║ Bioluminescent Abyss                                       (Sub-Basal Chasm) ║
║ Inventory: [█░░░░░░░] 1/8 Slots │ Memories:      Notes: 1 │ Explored: 2/88 │ ║
║ ◇◇◇◇◇◇◇ (0/7)                                                       Turns: 2 ║
╚══════════════════════════════════════════════════════════════════════════════╝
╭───────────────── Chamber View ──────────────────╮╭─ Fog-of-War Mini-Map (Z =─╮
│ PHOSPHOR CAVERN  — Bioluminescent Grotto        ││        [?]   [?]          │
│ ──────────────────────────────────────────────… ││         │     │           │
│ Curtains of cyan and cerulean mycelium drape    ││  [?]───[♦]───[★]          │
│ from the vaulted limestone ceiling, bathing the ││               │           │
│ wet rock in an eerie, dreamlike twilight.       ││              [?]          │
│                                                 ││ ────────────────────────… │
│ ✦ Fixtures : [canopy]  [fissures]               ││ Elev: +3· +2· +1· 0· -1·  │
│ ❖ Items Here:                                   ││ -2·  -3★                  │
│   • Uncut Abyssal Quartz Crystal (1 slot)       ││ ★ You  ● Visited  ♦ Item  │
│                                                 ││ ? Unknown                 │
│ ⇄ Exits     : [WEST] Obsidian Awakening Slab    ││ ▲ Up   ▼ Down     ╫       │
│               [NORTH] Unexplored  [SOUTH] Unexp ││ Locked ✎ Note             │
│ ✎ Room Note : "Crafted lantern here"            │╰─ Type 'map' for full lege─╯
╰─────────────────────────────────────────────────╯                             
╭──────────────────────────────────────────────────────────────────────────────╮
│ Commands: n/s/e/w/u/d Move │ x <obj> Examine │ take/drop <item> │ combine    │
│ <a> with <b> │ use <item> on <obj> │ map [z] │ note add <txt> │ inv │ hint   │
╰──────────────────────────────────────────────────────────────────────────────╯
```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+** (tested on Python 3.14)
- **[`rich`](https://github.com/Textualize/rich)** library for terminal rendering:
  ```bash
  pip install rich
  ```

### Running the Game
Clone the repository and run `main.py`:

```bash
python main.py
```

### Command-Line Options
You can also jump directly into a new game, load a specific save slot, or enable screen-clearing between turns:

```bash
# Start a new expedition immediately (skip startup prompt)
python main.py --new

# Load a specific save slot (e.g., autosave or quicksave)
python main.py --load autosave

# Clear the terminal screen between every turn
python main.py --clear
```

---

## 🗺️ The Seven Strata of Aethelgard

| Stratum | Elevation | Biome / Title | Chambers | Key Mechanics & Themes |
| :---: | :---: | :--- | :---: | :--- |
| **Z = +3** | `+500m` | **The Celestial Observatory & Crown** | 11 | Great Armillary Astrolabe, Harmonic Pylons (432/528 Hz), Storm Capacitor, Chorister Core |
| **Z = +2** | `+310m` | **The Aetherial Botanical Domes** | 12 | Heliostat Mirror Rings, Prism Refraction Tower, Clockwork Apiary, Aeolian Wind-Organ |
| **Z = +1** | `+140m` | **The Mnemonic Archives** | 13 | Sympathetic UV Blueprints, Cipher Rotunda, Secret Bookcase, Acoustic Jacquard Loom |
| **Z =  0** | `   0m` | **The Grand Clockwork Atrium** | 14 | Foucault Pendulum, Epoch Chronometer, Resonance Chimes, Gravity Weights, Solar Shutter |
| **Z = -1** | `-130m` | **The Sunken Aqueducts & Labs** | 13 | Canal Miter Locks, Pontoon Bridge, Aqua Regia Distillation, Parabolic Whispering Dome |
| **Z = -2** | `-280m` | **The Geothermal Foundry** | 13 | High-Pressure Steam Manifold, Magma Siphon Smelting, Cryo-Slag Quenching, Freight Winch |
| **Z = -3** | `-420m` | **The Bioluminescent Abyss** | 12 | Bioluminescent Lantern Crafting, 3-Valve Sluice Drainage, Grappling Shaft, Solar Core |

---

## 📂 Project Structure

```text
Adventure/
├── main.py                          # Entry point, title screen, CLI args, main loop
├── README.md                        # Project overview and quick start
├── USERGUIDE.md                     # Comprehensive player manual & command guide
├── CHANGELOG.md                     # Release history and current feature status
├── engine/
│   ├── __init__.py
│   ├── models.py                    # Serializable dataclasses (Coord3D, Room, Item, Recipe, Note, GameState)
│   ├── world_builder.py             # Loads and validates all 7 strata (88 rooms, 92 items, 26 recipes)
│   ├── commands.py                  # Natural-language parser and command handlers
│   ├── puzzles.py                   # Multi-room & cross-stratum puzzle state machines and endings
│   ├── ui.py                        # Rich split-screen dashboard & Fog-of-War 3D mini-map renderer
│   └── save_system.py               # Multi-slot JSON save/load with SHA-256 checksums & autosave
├── data/
│   ├── __init__.py
│   ├── items_and_recipes.py         # All 92 items, 26 crafting recipes, and lore/memory transcripts
│   ├── stratum_n3_abyss.py          # Stratum -3 rooms & fixtures (Z = -3)
│   ├── stratum_n2_geothermal.py     # Stratum -2 rooms & fixtures (Z = -2)
│   ├── stratum_n1_aqueducts.py      # Stratum -1 rooms & fixtures (Z = -1)
│   ├── stratum_0_sanctum.py         # Stratum  0 rooms & fixtures (Z =  0)
│   ├── stratum_p1_archives.py       # Stratum +1 rooms & fixtures (Z = +1)
│   ├── stratum_p2_arboretum.py      # Stratum +2 rooms & fixtures (Z = +2)
│   └── stratum_p3_observatory.py    # Stratum +3 rooms & fixtures (Z = +3)
├── saves/                           # Created automatically when saving games (.json)
└── tests/
    └── test_world_and_walkthrough.py # Automated test suite & 100% golden-path walkthrough verifier
```

---

## 🧪 Running Automated Tests

The repository includes an automated test suite that validates:
1. **3D Coordinate & Graph Integrity** across all 88 rooms, 92 items, and 26 recipes.
2. **Inventory Slot Limits**, item dropping, and the 10-slot satchel upgrade.
3. **Fog-of-War Mini-Map** filtering and coordinate-pinned field notes.
4. **Save/Load Round-Trip** serialization accuracy.
5. **Full Golden-Path Playthrough** from awakening at `(0, 0, -3)` to achieving the **True Harmonic Synthesis** ending at `(0, 2, +3)`.

Run the test suite with:
```bash
python -m unittest discover -s tests -v
```

---

## 📖 Documentation
For complete gameplay instructions, command syntax, inventory tips, and puzzle hints, see the **[User Guide (USERGUIDE.md)](./USERGUIDE.md)** and **[Changelog (CHANGELOG.md)](./CHANGELOG.md)**.
