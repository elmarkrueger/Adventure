"""Puzzle state machine and interactive fixture handlers for Echoes of the Aethelgard Spire."""

from typing import Optional, Tuple
from engine.models import GameState, Room
from engine.world_builder import World


def update_cross_stratum_states(world: World, state: GameState) -> Optional[str]:
    """Recompute cross-level dependencies (Solar Beam, Pendulum, Steam Lift, Crown Core)."""
    messages = []

    # 1. Check Stratum -3 Sluice Drainage (A=Open, B=Closed, C=Open)
    if (
        not state.flags.get("n3_ossuary_drained")
        and state.flags.get("n3_sluice_valve_a") is True
        and state.flags.get("n3_sluice_valve_b") is False
        and state.flags.get("n3_sluice_valve_c") is True
    ):
        state.flags["n3_ossuary_drained"] = True
        state.puzzle_Solved_count += 1
        world.rooms["n3_sluice_control"].exits["north"].locked = False
        world.rooms["n3_echoing_sump"].exits["west"].locked = False
        messages.append(
            "[bold bright_cyan]✦ PUZZLE SOLVED: With Intake A and Outflow C open and Backflow B "
            "closed, a tremendous suction drains the black brine from the Drowned Ossuary![/bold bright_cyan]"
        )

    # 2. Check Stratum -2 Manifold Pressure
    psi = (
        state.flags.get("n2_valve_alpha", 0)
        + state.flags.get("n2_valve_beta", 0)
        + state.flags.get("n2_valve_gamma", 0)
    )
    state.flags["n2_current_psi"] = psi
    if psi >= 75 and not state.flags.get("n2_steam_press_online"):
        state.flags["n2_steam_press_online"] = True
    if psi == 120 and not state.flags.get("n2_atrium_lift_powered"):
        state.flags["n2_atrium_lift_powered"] = True
        state.puzzle_Solved_count += 1
        messages.append(
            "[bold orange1]✦ PUZZLE SOLVED: The Boiler Manifold hits a steady 120 PSI! High-pressure "
            "steam rushes south to pressurize the Central Steam Lift![/bold orange1]"
        )
        # If key already used on lift, unlock exit
        if state.flags.get("n2_lift_key_turned"):
            world.rooms["n2_pressure_vault"].exits["up"].locked = False

    # 3. Check Stratum 0 Pendulum & Archive Stair Interlock
    if (
        not state.flags.get("z0_pendulum_running")
        and state.flags.get("z0_gear_installed")
        and state.flags.get("z0_weights_balanced")
        and state.flags.get("z0_brake_released")
    ):
        state.flags["z0_pendulum_running"] = True
        state.puzzle_Solved_count += 1
        messages.append(
            "[bold yellow]✦ PUZZLE SOLVED: With the Beveled Gear meshed, the Trim-Weight hung, and "
            "the brake released, the ten-ton Foucault Pendulum swings to life with a deep, "
            "thunderous heartbeat![/bold yellow]"
        )

    if (
        state.flags.get("z0_pendulum_running")
        and state.flags.get("z0_chrono_dial") == "4719"
        and world.rooms["z0_pendulum_rotunda"].exits["up"].locked
    ):
        world.rooms["z0_pendulum_rotunda"].exits["up"].locked = False
        state.puzzle_Solved_count += 1
        messages.append(
            "[bold yellow]✦ INTERLOCK DISENGAGED: Synchronized to Epoch 4719 and driven by the "
            "Great Pendulum, the spiral staircase `up` from the Central Pendulum Rotunda to "
            "Stratum +1 (The Mnemonic Archives) unlocks![/bold yellow]"
        )

    # 4. Check Stratum +1 Paternoster Lift
    if (
        state.flags.get("p1_paternoster_fused")
        and state.flags.get("p1_cipher_wheel") == "MNEMOS"
        and world.rooms["p1_paternoster_landing"].exits["up"].locked
    ):
        world.rooms["p1_paternoster_landing"].exits["up"].locked = False
        state.puzzle_Solved_count += 1
        messages.append(
            "[bold orchid1]✦ PUZZLE SOLVED: With the Silver-Copper Fuse installed and the MNEMOS "
            "cipher aligned, the Paternoster Lift hums to life (`up` to Stratum +2)![/bold orchid1]"
        )

    # 5. Check Stratum +2 Solar Beam & Stratum -3 Solar Core
    if (
        state.flags.get("p2_mirror_north") == "center"
        and state.flags.get("p2_mirror_south") == "center"
        and state.flags.get("p2_prism_installed")
    ):
        if not state.flags.get("p2_solar_beam_active"):
            state.flags["p2_solar_beam_active"] = True
            state.puzzle_Solved_count += 1
            messages.append(
                "[bold bright_green]✦ PUZZLE SOLVED: The North and South Heliostats converge through "
                "the Focusing Optic! A dazzling column of golden sunlight shoots downward through "
                "the center of the Spire![/bold bright_green]"
            )
        if state.flags.get("z0_shutter_open") and not state.flags.get("n3_solar_core_awakened"):
            state.flags["n3_solar_core_awakened"] = True
            state.puzzle_Solved_count += 1
            messages.append(
                "[bold bright_yellow]✦ CROSS-STRATUM RESONANCE: Passing through the open Atrium "
                "Shutter at Stratum 0, the solar beam strikes the Abyssal Solar Core at Stratum -3 "
                "(730 meters below), awakening the deepest anchor of Aethelgard![/bold bright_yellow]"
            )

    # 6. Check Stratum +3 Astrolabe, Pylons & Crown Antechamber
    if (
        state.flags.get("p3_astrolabe_azimuth") == 240
        and state.flags.get("p3_astrolabe_altitude") == 65
        and not state.flags.get("p3_astrolabe_aligned")
    ):
        state.flags["p3_astrolabe_aligned"] = True
        state.puzzle_Solved_count += 1
        messages.append(
            "[bold sky_blue1]✦ PUZZLE SOLVED: Locked at Azimuth 240° and Altitude 65°, the Great "
            "Astrolabe catches the Zenith starlight and projects it onto the Crown seal![/bold sky_blue1]"
        )

    if (
        state.flags.get("p3_west_pylon_freq") == 432
        and state.flags.get("p3_east_pylon_freq") == 528
        and not state.flags.get("p3_pylons_synced")
    ):
        state.flags["p3_pylons_synced"] = True
        state.puzzle_Solved_count += 1
        messages.append(
            "[bold sky_blue1]✦ PUZZLE SOLVED: The West Pylon (432 Hz) and East Pylon (528 Hz) lock "
            "into a 96-Hertz harmonic interval, canceling the Chorister's phase drift![/bold sky_blue1]"
        )

    if (
        state.flags.get("p3_astrolabe_aligned")
        and state.flags.get("p3_pylons_synced")
        and state.flags.get("p3_capacitor_installed")
        and not state.flags.get("p3_core_unlocked")
    ):
        state.flags["p3_core_unlocked"] = True
        world.rooms["p3_core_antechamber"].exits["north"].locked = False
        state.puzzle_Solved_count += 1
        messages.append(
            "[bold bright_white]✦ APEX UNLOCKED: Starlight, Harmonic Resonance, and Captured "
            "Lightning converge! The blast portal `north` into The Resonance Crown swings open![/bold bright_white]"
        )

    return "\n".join(messages) if messages else None


def handle_turn_or_pull(world: World, state: GameState, target: str) -> str:
    room = world.rooms[state.current_room_id]
    t = target.strip().lower()

    # --- STRATUM -3: Sluice Valves ---
    if room.id == "n3_sluice_control":
        if t in ("valve_a", "valve a", "a", "intake"):
            state.flags["n3_sluice_valve_a"] = not state.flags.get("n3_sluice_valve_a", False)
            status = "OPEN" if state.flags["n3_sluice_valve_a"] else "CLOSED"
            extra = update_cross_stratum_states(world, state)
            return f"You haul on Intake Bypass Valve A. It is now **{status}**." + (f"\n{extra}" if extra else "")
        if t in ("valve_b", "valve b", "b", "backflow"):
            state.flags["n3_sluice_valve_b"] = not state.flags.get("n3_sluice_valve_b", False)
            status = "OPEN" if state.flags["n3_sluice_valve_b"] else "CLOSED"
            extra = update_cross_stratum_states(world, state)
            return f"You turn Backflow Valve B. It is now **{status}**." + (f"\n{extra}" if extra else "")
        if t in ("valve_c", "valve c", "c", "spindle_c", "spindle c", "outflow"):
            if not state.flags.get("n3_wheel_attached"):
                return "Spindle C has no handwheel! Attach the Octagonal Bronze Valve Wheel first (`use valve_wheel on spindle_c`)."
            state.flags["n3_sluice_valve_c"] = not state.flags.get("n3_sluice_valve_c", False)
            status = "OPEN" if state.flags["n3_sluice_valve_c"] else "CLOSED"
            extra = update_cross_stratum_states(world, state)
            return f"You spin the newly fitted bronze wheel on Outflow Valve C. It is now **{status}**." + (f"\n{extra}" if extra else "")

    # --- STRATUM -2: Counterweight Winch & Steam Valves ---
    if room.id == "n2_winch_room" and any(k in t for k in ("winch", "lever", "clutch", "counterweight")):
        if state.flags.get("n2_counterweight_released"):
            return "The Abyssal Counterweight is already engaged and the freight lift is active."
        state.flags["n2_counterweight_released"] = True
        state.puzzle_Solved_count += 1
        world.rooms["n2_lift_landing"].exits["down"].locked = False
        world.rooms["n3_lift_shaft_bottom"].exits["up"].locked = False
        return (
            "[bold orange1]✦ You throw your weight against the iron clutch lever! Ten tons of "
            "basalt drop into tension with a deep boom, coupling the freight lift between "
            "Stratum -2 and Stratum -3![/bold orange1]"
        )

    if room.id == "n2_boiler_manifold":
        if any(k in t for k in ("alpha", "beta", "gamma", "valve", "all")):
            if "insulated_gauntlets" not in state.inventory:
                return (
                    "You reach for the steam valve, but recoil from the blistering heat! You need "
                    "the Asbestos-Weave Forge Gauntlets (from the Counterweight Winch Room) in your inventory."
                )
            if "alpha" in t:
                state.flags["n2_valve_alpha"] = 40 if state.flags.get("n2_valve_alpha", 0) == 0 else 0
                status = "OPEN (+40 PSI)" if state.flags["n2_valve_alpha"] else "CLOSED (0 PSI)"
                msg = f"Protected by your Forge Gauntlets, you turn Valve Alpha: **{status}**."
            elif "beta" in t:
                state.flags["n2_valve_beta"] = 35 if state.flags.get("n2_valve_beta", 0) == 0 else 0
                status = "OPEN (+35 PSI)" if state.flags["n2_valve_beta"] else "CLOSED (0 PSI)"
                msg = f"Protected by your Forge Gauntlets, you turn Valve Beta: **{status}**."
            elif "gamma" in t:
                state.flags["n2_valve_gamma"] = 45 if state.flags.get("n2_valve_gamma", 0) == 0 else 0
                status = "OPEN (+45 PSI)" if state.flags["n2_valve_gamma"] else "CLOSED (0 PSI)"
                msg = f"Protected by your Forge Gauntlets, you turn Valve Gamma: **{status}**."
            else:
                # Turn all open
                state.flags["n2_valve_alpha"] = 40
                state.flags["n2_valve_beta"] = 35
                state.flags["n2_valve_gamma"] = 45
                msg = "Protected by your Forge Gauntlets, you open Valves Alpha (+40), Beta (+35), and Gamma (+45)."
            extra = update_cross_stratum_states(world, state)
            total = state.flags["n2_current_psi"]
            return f"{msg} Total Manifold Pressure: **{total} PSI**." + (f"\n{extra}" if extra else "")

    # --- STRATUM -1: Canal Lock Winch ---
    if room.id == "n1_canal_lock_control" and any(k in t for k in ("winch", "lock", "crank", "gate")):
        if not state.flags.get("n1_crank_attached") and "sluice_crank" not in state.inventory:
            return "The lock winch spindle has no handle! Bring the Heavy Iron Lock-Crank from the Foundry Tram Dock."
        state.flags["n1_crank_attached"] = True
        state.flags["n1_canal_water_level"] = "high"
        state.flags["n1_waterwheel_engaged"] = True
        state.puzzle_Solved_count += 1
        world.rooms["n1_aqueduct_south"].exits["north"].locked = False
        world.rooms["n1_aqueduct_north"].exits["south"].locked = False
        return (
            "[bold dodger_blue1]✦ PUZZLE SOLVED: Fitting the Heavy Iron Lock-Crank to the winch, "
            "you wind open the upper miter gates! Turquoise water floods the canal to HIGH level, "
            "floating the central Pontoon Bridge into place and spinning the Waterwheel Dynamo![/bold dodger_blue1]"
        )

    # --- STRATUM 0: Shutter & Pendulum Brake ---
    if room.id == "z0_sun_shaft_balcony" and any(k in t for k in ("shutter", "lever", "iris", "aperture")):
        state.flags["z0_shutter_open"] = True
        extra = update_cross_stratum_states(world, state)
        return (
            "You haul back the brass Shutter Lever! The giant iris aperture in the central light-well "
            "retracts with a metallic whirr, opening a clear vertical path from Stratum +2 down to Stratum -3."
            + (f"\n{extra}" if extra else "")
        )

    if room.id == "z0_south_escapement" and any(k in t for k in ("brake", "lever", "pendulum")):
        state.flags["z0_brake_released"] = True
        extra = update_cross_stratum_states(world, state)
        if extra:
            return f"You release the heavy iron Pendulum Brake!\n{extra}"
        missing = []
        if not state.flags.get("z0_gear_installed"):
            missing.append("the Beveled Gear in the North Gear-Train Gallery")
        if not state.flags.get("z0_weights_balanced"):
            missing.append("the Lead Trim-Weight in the Vault of Weights")
        return (
            "You disengage the Pendulum Brake, though the pendulum still needs "
            + " and ".join(missing)
            + " before it can swing."
        )

    # --- STRATUM +1: Forbidden Index Secret Bookcase ---
    if room.id == "p1_west_stacks" and any(k in t for k in ("book", "treatise", "oblivion", "spine", "bookcase")):
        if state.flags.get("p1_secret_index_open"):
            return "The secret bookcase is already open to the west."
        state.flags["p1_secret_index_open"] = True
        state.puzzle_Solved_count += 1
        world.rooms["p1_west_stacks"].exits["west"].locked = False
        world.rooms["p1_west_stacks"].exits["west"].hidden = False
        return (
            "[bold orchid1]✦ PUZZLE SOLVED: You pull the spine of 'Treatise on Oblivion'. Counterweights "
            "rumble inside the wall as the entire western bookcase pivots open, revealing a hidden "
            "exit `west` into the Secret Vault![/bold orchid1]"
        )

    # --- STRATUM +2: Heliostat Mirrors ---
    if room.id == "p2_mirror_north" and "mirror" in t:
        state.flags["p2_mirror_north"] = "center"
        state.flags["p2_mirror_north_aligned"] = True
        extra = update_cross_stratum_states(world, state)
        return (
            "You crank the Northern Heliostat hand-wheel until its vernier locks on **CENTER**, "
            "aiming its blazing reflection directly into the Prism Refraction Tower!"
            + (f"\n{extra}" if extra else "")
        )

    if room.id == "p2_mirror_south" and "mirror" in t:
        state.flags["p2_mirror_south"] = "center"
        state.flags["p2_mirror_south_aligned"] = True
        extra = update_cross_stratum_states(world, state)
        return (
            "You crank the Southern Heliostat hand-wheel until its vernier locks on **CENTER**, "
            "aiming its concentrated beam directly into the Prism Refraction Tower!"
            + (f"\n{extra}" if extra else "")
        )

    return f"Turning or pulling '{target}' here has no obvious effect."


def handle_set_or_dial(world: World, state: GameState, target_and_val: str) -> str:
    room = world.rooms[state.current_room_id]
    raw = target_and_val.strip()
    lower = raw.lower()

    # Stratum -1: Alembic Burner
    if room.id == "n1_alchemical_distillery" and any(k in lower for k in ("burner", "heat", "low", "medium", "high", "off")):
        for lvl in ("low", "medium", "high", "off"):
            if lvl in lower:
                state.flags["n1_alembic_temp"] = lvl
                return (
                    f"You adjust the Alembic gas-spirit burner valve to **{lvl.upper()}** heat."
                    + (" The platinum retort simmers at the ideal temperature for Aqua Regia distillation!" if lvl == "medium" else "")
                )

    # Stratum -1: Whispering Dome Dish
    if room.id == "n1_whispering_dome" and any(k in lower for k in ("dish", "focus", "mirror", "parabolic")):
        state.flags["n1_whisper_angle"] = "focus"
        return (
            "[bold dodger_blue1]✦ You rotate the bronze Parabolic Dish to its exact focal point! "
            "Descending through the acoustic tube from the Atrium above, a ghostly four-note "
            "carillon melody rings out clearly: 'SOL — MI — DO — LA'.[/bold dodger_blue1]"
        )

    # Stratum 0: Chronometer Booth Dial (4719)
    if room.id == "z0_chrono_booth":
        digits = "".join(ch for ch in raw if ch.isdigit())
        if len(digits) == 4:
            state.flags["z0_chrono_dial"] = digits
            if digits == "4719":
                state.flags["z0_chrono_unlocked"] = True
                extra = update_cross_stratum_states(world, state)
                return (
                    "[bold yellow]✦ You dial 4-7-1-9 on the Epoch Synchronizer! Solenoids clack "
                    "into alignment across the Atrium![/bold yellow]"
                    + (f"\n{extra}" if extra else "")
                )
            return f"You set the Chronometer dial to {digits}, but the synchronization lamp remains dark."
        return "Specify a 4-digit code to dial on the Chronometer (e.g., `dial 4719`)."

    # Stratum +1: Cipher Rotunda (MNEMOS)
    if room.id == "p1_cipher_rotunda":
        tokens = raw.replace("cipher_wheel", "").replace("cipher", "").replace("wheel", "").replace("dial", "").strip().upper()
        if not tokens:
            return "Specify a 6-letter word to align on the Cipher Rotunda rings (e.g., `dial MNEMOS`)."
        word = tokens.split()[-1]
        state.flags["p1_cipher_wheel"] = word
        if word == "MNEMOS":
            state.flags["p1_cipher_solved"] = True
            extra = update_cross_stratum_states(world, state)
            return (
                "[bold orchid1]✦ The six brass letter-rings lock onto M-N-E-M-O-S with a resonant "
                "chord! The cryptographic canopy seal disengages![/bold orchid1]"
                + (f"\n{extra}" if extra else "")
            )
        return f"You align the brass rings to '{word}', but the lock does not yield."

    # Stratum +2: Heliostat Mirrors
    if room.id == "p2_mirror_north":
        for pos in ("center", "east", "west"):
            if pos in lower:
                state.flags["p2_mirror_north"] = pos
                state.flags["p2_mirror_north_aligned"] = (pos == "center")
                extra = update_cross_stratum_states(world, state)
                return f"You set the Northern Heliostat Mirror to **{pos.upper()}**." + (f"\n{extra}" if extra else "")

    if room.id == "p2_mirror_south":
        for pos in ("center", "east", "west"):
            if pos in lower:
                state.flags["p2_mirror_south"] = pos
                state.flags["p2_mirror_south_aligned"] = (pos == "center")
                extra = update_cross_stratum_states(world, state)
                return f"You set the Southern Heliostat Mirror to **{pos.upper()}**." + (f"\n{extra}" if extra else "")

    # Stratum +2: Wind-Organ
    if room.id == "p2_wind_organ_loft" and any(k in lower for k in ("cegb", "organ", "chord")):
        if "cegb" in lower.replace("-", "").replace(" ", ""):
            state.flags["p2_wind_organ_chord"] = "CEGB"
            state.flags["p2_elevator_powered"] = True
            world.rooms["p2_elevator_lobby"].exits["up"].locked = False
            state.puzzle_Solved_count += 1
            return (
                "[bold bright_green]✦ PUZZLE SOLVED: You depress C, E, G, and B on the Wind-Organ "
                "console! High-altitude winds rush through the thirty-foot pipes in a thunderous "
                "major-seventh chord, spinning the Aeolian dynamo and unlocking the Celestial "
                "Elevator (`up` from the Elevator Lobby)![/bold bright_green]"
            )

    # Stratum +3: Great Astrolabe (Azimuth 240, Altitude 65)
    if room.id == "p3_astrolabe_deck":
        nums = [int(s) for s in raw.replace("°", " ").split() if s.isdigit()]
        if "240" in raw and "65" in raw:
            state.flags["p3_astrolabe_azimuth"] = 240
            state.flags["p3_astrolabe_altitude"] = 65
        elif "azimuth" in lower and nums:
            state.flags["p3_astrolabe_azimuth"] = nums[-1]
        elif "altitude" in lower and nums:
            state.flags["p3_astrolabe_altitude"] = nums[-1]
        elif len(nums) == 2:
            state.flags["p3_astrolabe_azimuth"] = nums[0]
            state.flags["p3_astrolabe_altitude"] = nums[1]
        else:
            return "Set the Astrolabe with `set azimuth 240` and `set altitude 65` (or `set astrolabe 240 65`)."
        az = state.flags.get("p3_astrolabe_azimuth", 0)
        alt = state.flags.get("p3_astrolabe_altitude", 0)
        extra = update_cross_stratum_states(world, state)
        return f"Astrolabe Verniers set to **Azimuth {az}°, Altitude {alt}°**." + (f"\n{extra}" if extra else "")

    # Stratum +3: West & East Harmonic Pylons
    if room.id == "p3_west_pylon" and "432" in lower:
        state.flags["p3_west_pylon_freq"] = 432
        state.flags["p3_west_pylon_tuned"] = True
        extra = update_cross_stratum_states(world, state)
        return "You tune the West Harmonic Pylon resonator to **432 Hz**!" + (f"\n{extra}" if extra else "")

    if room.id == "p3_east_pylon" and "528" in lower:
        state.flags["p3_east_pylon_freq"] = 528
        state.flags["p3_east_pylon_tuned"] = True
        extra = update_cross_stratum_states(world, state)
        return "You tune the East Harmonic Pylon resonator to **528 Hz**!" + (f"\n{extra}" if extra else "")

    return f"You cannot set or dial '{raw}' here."


def handle_play_or_strike(world: World, state: GameState, arg: str) -> str:
    room = world.rooms[state.current_room_id]
    lower = arg.strip().lower()

    # 1. Playing a Mnemonic Cylinder (works in any room with a resonator or anywhere if player holds it)
    matched_cyl = world.match_item_in_list(lower, state.inventory + room.items)
    if matched_cyl and world.items[matched_cyl].category == "memory":
        item = world.items[matched_cyl]
        lore_entry = world.lore[item.memory_id]
        cyl_num = lore_entry.cylinder_number
        if cyl_num not in state.memories_restored:
            state.memories_restored.append(cyl_num)
            state.memories_restored.sort()
        if lore_entry.id not in state.unlocked_lore:
            state.unlocked_lore.append(lore_entry.id)
        return (
            f"[bold bright_cyan]═══ RESTORED MEMORY ({len(state.memories_restored)}/7): {lore_entry.title} ═══[/bold bright_cyan]\n"
            f"{lore_entry.text}"
        )

    # 2. Playing the Chime Bells on Stratum 0
    if room.id == "z0_chime_balcony":
        if "chime_mallet" not in state.inventory:
            return "You need the Felted Rosewood Chime Mallet (from the Maintainer's Barracks) to strike the resonance bells!"
        notes_found = [n for n in lower.replace("-", " ").replace(",", " ").split() if n in ("do", "re", "mi", "sol", "la")]
        if not notes_found:
            return "Specify which bell(s) to strike (`do`, `re`, `mi`, `sol`, `la`), e.g. `play sol mi do la`."
        seq = state.flags.get("z0_chime_sequence", [])
        seq.extend(notes_found)
        seq = seq[-4:]
        state.flags["z0_chime_sequence"] = seq
        if seq == ["sol", "mi", "do", "la"]:
            world.rooms["z0_cartographer_wing"].exits["south"].locked = False
            world.rooms["z0_south_escapement"].exits["east"].locked = False
            state.puzzle_Solved_count += 1
            return (
                "[bold yellow]✦ PUZZLE SOLVED: You strike SOL — MI — DO — LA on the bronze carillon! "
                "The harmonic chord echoes across the Atrium, unsealing the Hall of the Seven Anchors![/bold yellow]"
            )
        return f"The bronze bells ring out: **{' - '.join(n.upper() for n in seq)}**."

    # 3. Playing the Wind-Organ on Stratum +2
    if room.id == "p2_wind_organ_loft":
        if "cegb" in lower.replace("-", "").replace(" ", ""):
            return handle_set_or_dial(world, state, "organ CEGB")
        return "You press a few keys on the Wind-Organ, producing a breathy chord. (Hint: Play the four-note chord from the Architect's Blueprint: `play CEGB`)."

    return f"You aren't sure how to play '{arg}' here."


def handle_use_item(world: World, state: GameState, item_id: str, target: Optional[str]) -> str:
    room = world.rooms[state.current_room_id]
    item = world.items[item_id]
    t = (target or "").strip().lower()

    # 1. Upgrade item: Restored Archivist's Satchel
    if item_id == "archivist_satchel":
        state.inventory.remove("archivist_satchel")
        state.max_inventory_slots = 10
        return (
            "[bold bright_green]✦ UPGRADE EQUIPPED: You strap on the Restored Archivist's Satchel! "
            "Your maximum inventory capacity has permanently increased from 8 slots to 10 slots![/bold bright_green]"
        )

    # 2. Memory Cylinders -> play them or insert into Chorister Core
    if item.category == "memory":
        if room.id == "p3_resonance_crown" and (not t or "core" in t or "chorister" in t or "drum" in t):
            inserted = state.flags.get("p3_cylinders_inserted", [])
            if item_id not in inserted:
                inserted.append(item_id)
                state.flags["p3_cylinders_inserted"] = inserted
                state.inventory.remove(item_id)
            return (
                f"[bold bright_white]✦ You seat {item.name} into the Chorister's Mnemonic Core Drum "
                f"({len(inserted)}/7 cylinders loaded). Type `activate core` when ready![/bold bright_white]"
            )
        return handle_play_or_strike(world, state, item.id)

    # 3. Check if item unlocks any locked exit in the current room
    for dir_name, ex in room.exits.items():
        if ex.locked and ex.unlock_item_id == item_id:
            if not t or dir_name in t or any(w in t for w in ("door", "gate", "lock", "shaft", "slag", "seal", "lift", "bridge", "portal", "north", "south", "east", "west", "up", "down")):
                # Special check for n2_pressure_vault steam lift: needs key AND 120 PSI
                if room.id == "n2_pressure_vault" and dir_name == "up":
                    state.flags["n2_lift_key_turned"] = True
                    if not state.flags.get("n2_atrium_lift_powered"):
                        return (
                            f"{ex.unlock_message}\nHowever, the steam gauge reads under 120 PSI! "
                            "Open all three valves (`Alpha`, `Beta`, `Gamma`) in the Boiler Manifold Hall so the lift can ascend."
                        )
                ex.locked = False
                ex.hidden = False
                # Also unlock reverse exit if locked with same lock_id
                target_room = world.rooms[ex.target_room_id]
                for rev_ex in target_room.exits.values():
                    if rev_ex.lock_id and rev_ex.lock_id == ex.lock_id:
                        rev_ex.locked = False
                if ex.consume_key and item_id in state.inventory:
                    state.inventory.remove(item_id)
                state.puzzle_Solved_count += 1
                return f"[bold bright_green]✦ {ex.unlock_message}[/bold bright_green]"

    # 4. Room-specific fixture interactions
    # Stratum -3: Valve Wheel on Spindle C
    if room.id == "n3_sluice_control" and item_id == "valve_wheel":
        state.inventory.remove("valve_wheel")
        state.flags["n3_wheel_attached"] = True
        state.flags["n3_sluice_valve_c"] = True
        extra = update_cross_stratum_states(world, state)
        return (
            "You slide the Octagonal Bronze Valve Wheel onto Spindle C and crank it **OPEN**!"
            + (f"\n{extra}" if extra else "")
        )

    # Stratum -3: Diving Helmet allows entering Drowned Ossuary even if not drained
    if item_id == "diving_helmet" and room.id in ("n3_sluice_control", "n3_echoing_sump"):
        world.rooms["n3_sluice_control"].exits["north"].locked = False
        world.rooms["n3_echoing_sump"].exits["west"].locked = False
        return (
            "You seal the Pressurized Brass Diving Hood over your shoulders! You can now wade "
            "directly into the Drowned Ossuary."
        )

    # Stratum -2: Smelting Brass in Magma Siphon Furnace
    if room.id == "n2_magma_siphon" and item_id in ("unheated_brass_crucible", "brass_ingot"):
        if item_id == "brass_ingot" and "empty_crucible" in state.inventory:
            state.inventory.remove("empty_crucible")
            state.inventory.remove("brass_ingot")
            state.inventory.append("unheated_brass_crucible")
            item_id = "unheated_brass_crucible"
        if item_id == "unheated_brass_crucible":
            if "insulated_gauntlets" not in state.inventory:
                return (
                    "The Magma Siphon cradle radiates blinding heat! You need the Asbestos-Weave "
                    "Forge Gauntlets in your inventory to safely handle the molten crucible."
                )
            state.inventory.remove("unheated_brass_crucible")
            state.inventory.append("molten_brass_crucible")
            return (
                "[bold orange1]✦ Wearing your Forge Gauntlets, you lower the crucible into the "
                "magma siphon cradle! Within moments the Clock-Brass melts into a glowing golden "
                "liquid (`molten_brass_crucible`). Combine it with `key_mold` to cast the Sanctum Key![/bold orange1]"
            )

    # Stratum -1: Distilling Unrefined Regia at Alembic
    if room.id == "n1_alchemical_distillery" and item_id == "unrefined_regia":
        temp = state.flags.get("n1_alembic_temp", "off")
        if temp != "medium":
            return (
                f"The Alembic burner is currently set to **{temp.upper()}**. According to the "
                "Distiller's Vellum Scroll, you must set the burner to **MEDIUM** (`set burner medium`) "
                "before distilling Aqua Regia!"
            )
        state.inventory.remove("unrefined_regia")
        state.inventory.append("aqua_regia")
        state.puzzle_Solved_count += 1
        return (
            "[bold dodger_blue1]✦ PUZZLE SOLVED: You pour the Unrefined Acid Mixture into the "
            "platinum retort over a steady MEDIUM flame. Scarlet droplets condense into the "
            "receiving flask—you have distilled pure **Aqua Regia**![/bold dodger_blue1]"
        )

    # Stratum -1: Sluice Crank in Canal Lock Control
    if room.id == "n1_canal_lock_control" and item_id == "sluice_crank":
        return handle_turn_or_pull(world, state, "winch")

    # Stratum 0: Beveled Gear in North Gear Gallery
    if room.id == "z0_north_gear_gallery" and item_id == "beveled_gear":
        state.inventory.remove("beveled_gear")
        state.flags["z0_gear_installed"] = True
        extra = update_cross_stratum_states(world, state)
        return (
            "[bold yellow]✦ You slide the Heavy Beveled Escapement Gear onto the primary drive "
            "spindle! Its phosphor-bronze teeth mesh cleanly with the Atrium gear-train.[/bold yellow]"
            + (f"\n{extra}" if extra else "")
        )

    # Stratum 0: Lead Trim-Weight in Vault of Weights
    if room.id == "z0_vault_of_weights" and item_id == "lead_counterweight":
        state.inventory.remove("lead_counterweight")
        state.flags["z0_weights_balanced"] = True
        extra = update_cross_stratum_states(world, state)
        return (
            "[bold yellow]✦ You hook the 15-kg Lead Trim-Weight onto the gravity drive cradle! "
            "The drive chains hum with balanced tension (and 2 inventory slots are freed!).[/bold yellow]"
            + (f"\n{extra}" if extra else "")
        )

    # Stratum 0: Chime Mallet on Chime Balcony
    if room.id == "z0_chime_balcony" and item_id == "chime_mallet":
        return handle_play_or_strike(world, state, "sol mi do la")

    # Stratum +1: UV Bulb or Blank Blueprint in Restoration Lab
    if room.id == "p1_restoration_lab" and item_id in ("uv_bulb", "blank_blueprint"):
        if item_id == "uv_bulb":
            state.flags["p1_uv_lamp_powered"] = True
            if "blank_blueprint" in state.inventory:
                state.inventory.remove("blank_blueprint")
                state.inventory.append("revealed_blueprint")
                return (
                    "[bold orchid1]✦ You screw the Quartz-Mercury UV Bulb into the Restoration Lamp "
                    "and hold the seemingly blank blueprint beneath the violet rays! Sympathetic "
                    "cobalt lines blaze into view (`revealed_blueprint`)![/bold orchid1]"
                )
            return "You fit the Quartz-Mercury UV Bulb into the Restoration Lamp. Bring the Blank Blueprint here to inspect it!"
        if item_id == "blank_blueprint":
            if state.flags.get("p1_uv_lamp_powered") or "uv_bulb" in state.inventory:
                state.inventory.remove("blank_blueprint")
                state.inventory.append("revealed_blueprint")
                return (
                    "[bold orchid1]✦ Under the ultraviolet rays of the Restoration Lamp, hidden "
                    "cobalt ink blazes across the vellum (`revealed_blueprint`)! Read it with `read blueprint`.[/bold orchid1]"
                )
            return "The Restoration Lamp has no bulb! Find the Quartz-Mercury Vapor Bulb in the Listening Booths first."

    # Stratum +1: Tuning Fork 432 Hz on Acoustic Loom
    if room.id == "p1_acoustic_loom" and item_id == "tuning_fork_432":
        state.flags["p1_loom_tuned"] = True
        return (
            "[bold orchid1]✦ You strike the 432 Hz Veridian Tuning Fork against the Acoustic Loom's "
            "calibration mount! The Jacquard weave aligns, etching a reminder on its brass tape: "
            "'WEST PYLON: 432 HZ | EAST PYLON: 528 HZ'.[/bold orchid1]"
        )

    # Stratum +1: Copper Fuse in Paternoster Landing
    if room.id == "p1_paternoster_landing" and item_id == "copper_fuse":
        state.inventory.remove("copper_fuse")
        state.flags["p1_paternoster_fused"] = True
        extra = update_cross_stratum_states(world, state)
        return (
            "[bold orchid1]✦ You snap the High-Ampere Silver-Copper Fuse Link into the switchboard! "
            "Power flows to the Paternoster motor![/bold orchid1]"
            + (f"\n{extra}" if extra else "")
        )

    # Stratum +2: Focusing Optic in Prism Refraction Tower
    if room.id == "p2_prism_tower" and item_id == "focusing_optic":
        state.inventory.remove("focusing_optic")
        state.flags["p2_prism_installed"] = True
        extra = update_cross_stratum_states(world, state)
        return (
            "[bold bright_green]✦ You lock the Gimbal-Mounted Focusing Optic into the central "
            "collimator cradle![/bold bright_green]"
            + (f"\n{extra}" if extra else "")
        )

    # Stratum +2: Starlight Pollen on Sovereign Orchid
    if room.id == "p2_orchid_grove" and item_id == "starlight_pollen":
        state.inventory.remove("starlight_pollen")
        state.flags["p2_orchid_pollinated"] = True
        room.items.append("tuning_fork_528")
        state.puzzle_Solved_count += 1
        return (
            "[bold bright_green]✦ PUZZLE SOLVED: You dust the luminescent Starlight Pollen across "
            "the Sovereign Orchid! With a crystalline chime, its quartz petals unfurl, revealing "
            "the **Harmonic Tuning Fork (528 Hz — Golden)** inside (`take fork 528`)![/bold bright_green]"
        )

    # Stratum +2: Lit Smoker in Apiary of Brass Bees
    if room.id == "p2_apiary" and item_id == "lit_smoker":
        state.flags["p2_bees_calmed"] = True
        if "conducting_wax" not in room.items and "conducting_wax" not in state.inventory:
            room.items.append("conducting_wax")
        state.puzzle_Solved_count += 1
        return (
            "[bold bright_green]✦ PUZZLE SOLVED: You pump clouds of soothing Somnus-Fern vapor into "
            "the copper skeps! The clockwork bees fold their wings in dormancy, exposing a "
            "**Comb of Gold-Spun Conducting Wax** (`take wax`)![/bold bright_green]"
        )

    # Stratum +3: Waxed Capacitor on Lightning Rod
    if room.id == "p3_lightning_spire" and item_id == "waxed_capacitor":
        state.inventory.remove("waxed_capacitor")
        state.inventory.append("charged_capacitor")
        state.flags["p3_lightning_captured"] = True
        state.puzzle_Solved_count += 1
        return (
            "[bold sky_blue1]✦ PUZZLE SOLVED: You clamp the Conducting-Sealed Leyden Capacitor to "
            "the platinum lightning rod! A blinding bolt of violet storm-lightning arcs from the "
            "clouds straight into the jar, giving you a **Storm-Charged Aether Capacitor**![/bold sky_blue1]"
        )

    # Stratum +3: Tuning Forks on West & East Harmonic Pylons
    if room.id == "p3_west_pylon" and item_id == "tuning_fork_432":
        return handle_set_or_dial(world, state, "432")

    if room.id == "p3_east_pylon" and item_id == "tuning_fork_528":
        return handle_set_or_dial(world, state, "528")

    # Stratum +3: Charged Capacitor in Core Antechamber
    if room.id == "p3_core_antechamber" and item_id == "charged_capacitor":
        state.inventory.remove("charged_capacitor")
        state.flags["p3_capacitor_installed"] = True
        extra = update_cross_stratum_states(world, state)
        return (
            "[bold sky_blue1]✦ You lock the Storm-Charged Aether Capacitor into the high-voltage "
            "receptacle! Celestial current surges into the Crown bus-bars![/bold sky_blue1]"
            + (f"\n{extra}" if extra else "")
        )

    return f"Using {item.name} here has no effect."


def handle_activate_core(world: World, state: GameState) -> str:
    room = world.rooms[state.current_room_id]
    if room.id != "p3_resonance_crown":
        return "You must be standing inside The Resonance Crown (Apex) on Stratum +3 to activate the Chorister Core."

    # Auto-insert any memory cylinders currently in inventory
    inserted = state.flags.get("p3_cylinders_inserted", [])
    for item_id in list(state.inventory):
        if world.items[item_id].category == "memory":
            if item_id not in inserted:
                inserted.append(item_id)
                cyl_num = world.lore[world.items[item_id].memory_id].cylinder_number
                if cyl_num not in state.memories_restored:
                    state.memories_restored.append(cyl_num)
            state.inventory.remove(item_id)
    state.flags["p3_cylinders_inserted"] = inserted
    total_memories = len(set(inserted) | {f"cylinder_{m}" for m in state.memories_restored})
    solar_awake = state.flags.get("n3_solar_core_awakened", False)

    state.game_won = True
    if total_memories >= 7 and solar_awake:
        state.ending_type = "TRUE_HARMONIC_SYNTHESIS"
        return (
            "[bold bright_white]╔══════════════════════════════════════════════════════════════════════╗\n"
            "║           TRUE ENDING: THE HARMONIC SYNTHESIS OF AETHELGARD          ║\n"
            "╚══════════════════════════════════════════════════════════════════════╝[/bold bright_white]\n\n"
            "All seven Mnemonic Cylinders spin in unison inside the Chorister's core drum. "
            "Seven hundred and thirty meters below, the awakened Abyssal Solar Core answers with "
            "a pillar of golden light that rises through all seven strata—uniting the Abyss, the "
            "Foundry, the Aqueducts, the Clockwork Atrium, the Archives, the Botanical Domes, and "
            "the Celestial Crown into a single resonant chord.\n\n"
            "The Chorister's corrupted dissonance dissolves into a pure polyphonic symphony. Below "
            "the earth, the Chrono-Seismic Fracture knits shut forever. Your mind and memories are "
            "whole once more, Chief Architect Vaelen Korr. You have saved Aethelgard."
        )
    elif total_memories >= 5:
        state.ending_type = "ARCHITECTS_RESTORATION"
        return (
            "[bold sky_blue1]╔══════════════════════════════════════════════════════════════════════╗\n"
            "║              ENDING: RESTORATION OF THE SOVEREIGN ANCHOR             ║\n"
            "╚══════════════════════════════════════════════════════════════════════╝[/bold sky_blue1]\n\n"
            f"With {total_memories} of your 7 Mnemonic Cylinders restored, you speak the Override "
            "Sequence into the Chorister's harmonic horn. The great automaton bows to your command, "
            "locking the Foucault Pendulum and the twin Pylons into a stable containment cycle.\n\n"
            "Though a few fragments of your past remain locked in the lower depths (or the Abyssal "
            "Solar Core slumbers on Stratum -3), the Fracture is contained and the Spire stands "
            "safe under your stewardship!"
        )
    else:
        state.ending_type = "EMERGENCY_PURGE"
        return (
            "[bold orange1]╔══════════════════════════════════════════════════════════════════════╗\n"
            "║                ENDING: THE OBLIVION CONTAINMENT PURGE                ║\n"
            "╚══════════════════════════════════════════════════════════════════════╝[/bold orange1]\n\n"
            f"With only {total_memories}/7 Mnemonic Cylinders recovered, you cannot reweave the "
            "Chorister's full harmonic matrix—so you trigger the Emergency Containment Purge. "
            "The Storm-Charged Capacitor shatters the Chorister's logic rings and drops the "
            "pendulum anchors, sealing the Fracture behind solid stone forever.\n\n"
            "The world above is safe, though who you once were remains a mystery among the stars. "
            "(Tip: Explore all 7 strata to collect all 7 Cylinders and awaken the Abyssal Solar Core "
            "for the True Harmonic Synthesis ending!)"
        )


def get_contextual_hint(world: World, state: GameState) -> str:
    room = world.rooms[state.current_room_id]
    if room.dark and "phosphor_lantern" not in state.inventory and "phosphor_lantern" not in room.items:
        return (
            "💡 [bold cyan]HINT:[/bold cyan] This chamber is pitch-dark! Return to the Awakening Slab "
            "and Phosphor Cavern on Stratum -3 to combine `unlit_lantern` with `glow_moss`."
        )
    if room.ambient_hint:
        return f"💡 [bold cyan]HINT ({room.name}):[/bold cyan] {room.ambient_hint}"

    # Stratum-level fallback hints
    z = room.stratum
    if z == -3:
        return (
            "💡 [bold cyan]STRATUM -3 HINT:[/bold cyan] Drain the Drowned Ossuary from Sluice Control "
            "(Open A, Close B, attach `valve_wheel` from the Submerged Bell-Dock to Spindle C and Open C) "
            "to get Cylinder I. Craft `grappling_hook` (`rusted_grapnel` + `brine_solvent` -> `clean_grapnel`, "
            "`mycelial_cord` + `copper_wire_spool` -> `braided_rope`) to climb the Whispering Fissure!"
        )
    if z == -2:
        return (
            "💡 [bold cyan]STRATUM -2 HINT:[/bold cyan] Take the `insulated_gauntlets` from the Winch Room "
            "(and `pull winch`). Open all three Boiler Manifold valves (120 PSI). Quench the molten slag "
            "in Cooling Vats with `cryo_canister`. Press `broken_sanctum_key` into `clay_blank`, melt "
            "`brass_ingot` in `empty_crucible` at the Magma Siphon furnace, and combine to cast `sanctum_key`!"
        )
    if z == -1:
        return (
            "💡 [bold cyan]STRATUM -1 HINT:[/bold cyan] Use `sluice_crank` in Canal Lock Control to raise "
            "the water level. Combine `nitric_acid_vial` + `muriatic_acid_vial`, `set burner medium` in the "
            "Alchemical Distillery, and `use unrefined_regia on alembic` to make `aqua_regia` for the Founders' Crypt!"
        )
    if z == 0:
        return (
            "💡 [bold cyan]STRATUM 0 HINT:[/bold cyan] Install `beveled_gear` in the North Gallery, use "
            "`repaired_coupler` on the West Tramway bridge to get `lead_counterweight` for the Vault of Weights, "
            "`pull brake` in South Escapement, `dial 4719` in the Chronometer Booth, and `pull shutter` on the Sun-Shaft Balcony!"
        )
    if z == 1:
        return (
            "💡 [bold cyan]STRATUM +1 HINT:[/bold cyan] Pull the 'Treatise on Oblivion' in the West Stacks "
            "(`pull treatise`). Reveal `blank_blueprint` with `uv_bulb` in the Restoration Lab. Install "
            "`copper_fuse` in the Paternoster Landing and `dial MNEMOS` in the Cipher Rotunda!"
        )
    if z == 2:
        return (
            "💡 [bold cyan]STRATUM +2 HINT:[/bold cyan] Set `mirror_north` and `mirror_south` to `center`, "
            "and install `focusing_optic` in the Prism Tower. Use `starlight_pollen` on the Orchid for "
            "`tuning_fork_528`. Use `lit_smoker` in the Apiary for `conducting_wax`. Play `CEGB` on the Wind-Organ!"
        )
    return (
        "💡 [bold cyan]STRATUM +3 HINT:[/bold cyan] Unlock the Antechamber with `architect_signet`. "
        "Align the Astrolabe (`set astrolabe 240 65`), tune West Pylon (`432`) and East Pylon (`528`), "
        "charge `waxed_capacitor` at the Lightning Spire, use `charged_capacitor` in the Antechamber, "
        "and `activate core` in the Resonance Crown!"
    )
