# Changelog

All notable changes, architectural milestones, and current project status for **Echoes of the Aethelgard Spire** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Current Status Summary] — Ready / v1.0.0 Complete
- **Overall State**: Production-ready, 100% playable and verified from initial awakening (`(0, 0, -3)`) to all three endings at the Apex (`(0, 2, +3)`).
- **World Scale**: **7 vertical strata (`Z = -3` to `Z = +3`)** containing **88 interconnected chambers** with verified 3D coordinate geometry.
- **Item & Crafting Catalog**: **92 unique items** and **26 item-combination recipes**.
- **Test Coverage**: 5/5 automated test suites passing (`test_world_and_walkthrough.py`), including a 150+ step end-to-end golden-path walkthrough.

---

## [1.0.0] - 2026-11-07

### Added
- **Core 3D World Engine (`engine/models.py`, `engine/world_builder.py`)**:
  - Implemented 3D coordinate grid (`Coord3D(x, y, z)`) supporting six-axis navigation (`north`, `south`, `east`, `west`, `up`, `down`).
  - Added automated graph validator checking coordinate uniqueness, unit directional deltas, and item/exit integrity across all 88 chambers.
- **Seven Vertical Strata (`data/stratum_*.py`)**:
  - **Stratum -3 (-420m)**: *The Bioluminescent Abyss* (12 chambers) — Awakening Slab, Phosphor Cavern, Survivor's Alcove, Sluice Control Niche, Brine Filtration Pool, Calcified Cistern, Echoing Sump, Mycelial Suspension Bridge, Submerged Bell-Dock, Drowned Ossuary, Whispering Fissure, Abyssal Lift Shaft.
  - **Stratum -2 (-280m)**: *The Geothermal Foundry & Steamworks* (13 chambers) — Venting Chimney Base, Abyssal Lift Landing, Counterweight Winch Room, Anthracite Coal Bunker, Boiler Manifold Hall, Steam Turbine Gallery, Forge-Master's Office, Obsidian Cooling Vats, Magma Siphon Bridge, Pneumatic Dispatch Hub, Slag Crucible Chamber, Pressure Regulation Vault, Foundry Tram Dock.
  - **Stratum -1 (-130m)**: *The Sunken Aqueducts & Alchemical Labs* (13 chambers) — Steam Lift Vestibule, Botanical Drainage Basin, Sluice Gate Overlook, Waterwheel Dynamo Hall, Grand Aqueduct South, Alchemical Distillery, Vitriol Storage Vault, Canal Lock Control, Grand Aqueduct North, Glassblower's Annex, Whispering Acoustic Dome, Aqueduct Spiral Stair, Sunken Crypt of the Founders.
  - **Stratum 0 (0m Datum)**: *The Grand Clockwork Atrium & Hall of Anchors* (14 chambers) — Great Spiral Stairwell, Acoustic Chime Balcony, Maintainer's Barracks, Pneumatic Locker Room, North Gear-Train Gallery, Chronometer Control Booth, Western Cantilever Span, West Tramway Concourse, Central Pendulum Rotunda, East Cartographer's Wing, Sun-Shaft Balcony, Vault of Weights, South Escapement Hall, Hall of the Seven Anchors.
  - **Stratum +1 (+140m)**: *The Mnemonic Archives & Scriptorium* (13 chambers) — Archive Rotunda, South Stacks, Parchment Restoration Lab, Phonograph Listening Booths, East Stacks, West Stacks (Forbidden Index), Secret Vault, North Stacks, Acoustic Loom Chamber, Curator's Private Study, Paternoster Lift Landing, Cipher Rotunda, Upper Gallery Overlook.
  - **Stratum +2 (+310m)**: *The Aetherial Botanical Domes & Prism Arrays* (12 chambers) — Conservatory Central Dome, Heliostat Mirror Ring North, Spore Condenser Lab, Hydroponic Reservoir, Prism Refraction Tower, Starlight Orchid Grove, Apiary of Brass Bees, Heliostat Mirror Ring South, Wind-Organ Loft, Hanging Root Catwalk, Celestial Elevator Lobby, Cloud-Pier Lookout.
  - **Stratum +3 (+500m)**: *The Celestial Observatory & Resonance Crown* (11 chambers) — Observatory Arrival Platform, Star-Charting Rotunda, Architect's Living Quarters, Astrolabe Calibration Deck, Zenith Glass Bridge, Equatorial Telescope Dome, Lightning Rod Spire, West Harmonic Pylon, Memory Core Antechamber, East Harmonic Pylon, The Resonance Crown (Apex).
- **Item, Crafting, & Inventory System (`data/items_and_recipes.py`, `engine/commands.py`)**:
  - Created 92 items across tool, component, key, lore, memory cylinder, and upgrade categories.
  - Created 26 item-combination recipes (`combine <itemA> with <itemB>`).
  - Enforced 8-slot starting inventory cap with persistent room floor dropping (`drop <item>`), a craftable 10-slot backpack upgrade (`archivist_satchel`), and a cross-stratum Pneumatic Locker system (`stash`, `retrieve`, `locker`).
- **Cross-Stratum Puzzle State Machine (`engine/puzzles.py`)**:
  - Implemented 30+ environmental and logic puzzles, including hydraulic sluice drainage, geothermal PSI manifold balancing, refractory key casting, Aqua Regia distillation, carillon bell sequences, Foucault pendulum restoration, ultraviolet blueprint revelation, heliostat solar beam collimation from `Z = +2` through `Z = 0` down to `Z = -3`, armillary astrolabe alignment, dual harmonic pylon tuning (`432 Hz` / `528 Hz`), and three distinct endings at the Chorister Core.
  - Added context-sensitive spoiler-light `hint` command.
- **Rich Split-Screen Terminal UI & Fog-of-War Mini-Map (`engine/ui.py`)**:
  - Designed dynamic biome-colored `rich` dashboard with telemetry header, chamber viewport, and live side-by-side Fog-of-War Mini-Map.
  - Implemented strict fog-of-war filtering so only visited rooms (`[★]`, `[●]`, `[▲]`, `[▼]`, `[↕]`, `[♦]`, `[✎]`) and directly adjacent unknown rooms (`[?]`) are displayed.
  - Added full-stratum map viewer (`map [z]`) and vertical Spire cross-section (`map vertical`).
  - Configured automatic UTF-8 stream handling for Windows PowerShell and Command Prompt.
- **Player Field Notebook & Lore Journal (`engine/commands.py`)**:
  - Added coordinate-pinned note creation (`note add <text>`), custom tags (`note tag <tag> <text>`), search/filtering (`notes <query>`), note deletion (`note del <id>`), and a persistent Lore & Memory Cylinder Journal (`journal`).
- **Save & Load System (`engine/save_system.py`)**:
  - Implemented JSON serialization with SHA-256 integrity checksums, named save slots (`save <slot>`, `load <slot>`, `saves`), and automatic `autosave` on every vertical stratum transition.
- **Automated Verification Suite (`tests/test_world_and_walkthrough.py`)**:
  - Added unit and integration tests verifying 3D world geometry, inventory capacity limits, mini-map fog-of-war, notebook operations, save/load round-trips, and a complete golden-path playthrough across all 7 strata.
- **Documentation**:
  - Added [README.md](./README.md), [USERGUIDE.md](./USERGUIDE.md), and [CHANGELOG.md](./CHANGELOG.md).
