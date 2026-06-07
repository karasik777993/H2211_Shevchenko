"""
Galactic Mission Generator
Author: Antigravity AI
Description: A procedural generator that designs unique space missions, difficulty ratings,
             and scaled rewards based on the cadet's level.
"""
import os
import random
import sys
import time


def init_terminal():
    """Initializes terminal support for ANSI colors, especially on Windows."""
    if os.name == 'nt':
        os.system('')


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Rarity levels
    COMMON = '\033[97m'  # Bright White
    RARE = '\033[94m'  # Bright Blue
    EPIC = '\033[95m'  # Bright Purple
    LEGENDARY = '\033[93m'  # Yellow/Orange
    ARTIFACT = '\033[91m'  # Red


# Mission Name Generators
NAME_PREFIXES = ["Operation", "Project", "Task Force", "Protocol", "Initiative", "Crusade", "Campaign", "Incursion",
                 "Assault", "Vanguard"]
NAME_ADJECTIVES = [
    "Silent", "Crimson", "Obsidian", "Quantum", "Shadow", "Apex", "Void", "Solar",
    "Nebula", "Tachyon", "Spectral", "Ghost", "Starlight", "Abyssal", "Titanium",
    "Frozen", "Eclipse", "Hyperion", "Aegis", "Chronos"
]
NAME_NOUNS = [
    "Storm", "Whisper", "Vortex", "Grip", "Sentinel", "Breach", "Reckoning",
    "Ascension", "Shield", "Strike", "Fist", "Dawn", "Ruin", "Legacy",
    "Horizon", "Specter", "Echo", "Prism", "Wrath", "Anomaly"
]
# Mission Descriptions & Components
LOCATIONS = [
    "the Outer Asteroid Belt of Sector-9",
    "the Event Horizon of the Cygnus-X Black Hole",
    "the toxic atmosphere of Planet Kepler-186f",
    "the sub-surface ocean of Europa",
    "an abandoned space station in the Dark Nebula",
    "the disputed borders of the Orion Syndicate",
    "the radioactive ruins of a forgotten homeworld",
    "the Lagrange point between binary stars",
    "the sub-orbital defense grid of Capital Prime",
    "the unexplored Void Space of Sector-108"
]
ENEMIES = [
    "Crimson Fleet Raiders",
    "Rogue AI Defense Drones",
    "Void-dwelling Behemoths",
    "Syndicate Mercenaries",
    "Kardashev-II Empire Scouts",
    "Cybernetic Scavengers",
    "Geth-type Nanite Swarms",
    "Spectral Phase Phantoms",
    "Interstellar Smugglers",
    "Rebel Splinter Cells"
]
TARGETS = [
    "a prototype Singularity Core",
    "stolen Starfleet encryption keys",
    "a captured High Council Diplomat",
    "a cache of raw Dark Matter crystals",
    "ancient alien archives containing warp coordinates",
    "the coordinates of a hidden superweapon",
    "a rogue genetic sequence sample",
    "experimental Cloaking Device schematics"
]
# Items mapping for Rewards
LOOT_TEMPLATES = {
    "COMMON": {
        "prefixes": ["Standard", "Surplus", "Basic", "Reliable", "Field-Tested"],
        "items": ["Laser Pistol", "Plasteel Shield", "Ion Battery", "Hacking Tool", "Repair Nanites"],
        "color": Colors.COMMON,
        "label": "Common"
    },
    "RARE": {
        "prefixes": ["Enhanced", "Military-Grade", "Specialist", "Advanced", "Tactical"],
        "items": ["Plasma Rifle", "Shield Matrix", "Tachyon Sensor", "Cloak Field Generator", "Heavy Plasteel Alloy"],
        "color": Colors.RARE,
        "label": "Rare"
    },
    "EPIC": {
        "prefixes": ["Prototype", "Vanguard-Spec", "Quantum-Tuned", "Overclocked", "High-Yield"],
        "items": ["Singularity Cannon", "Aegis Reflector", "Warp Engine Core", "Neural Interface Link",
                  "Nanite Swarm Injector"],
        "color": Colors.EPIC,
        "label": "Epic"
    },
    "LEGENDARY": {
        "prefixes": ["Hyperion-Class", "Ancient", "Star-Forged", "Elite", "Doomsday"],
        "items": ["Antimatter Decimator", "Gravity Well Projector", "Temporal Phase Engine", "AI Co-pilot Subroutine"],
        "color": Colors.LEGENDARY,
        "label": "Legendary"
    },
    "ARTIFACT": {
        "prefixes": ["Celestial", "Omega-Protocol", "Singularity-Infused", "Crystalline", "Void-Touched"],
        "items": ["Chronos Time-Bender", "Nova Core Reactor", "Reality-Warping Displace Shield",
                  "Archangel Strike Matrix"],
        "color": Colors.ARTIFACT,
        "label": "Artifact"
    }
}
OBJECTIVE_TEMPLATES = [
    "Infiltrate {location} and retrieve {target} before {enemy} detect your signature.",
    "Establish a defensive perimeter around {location} to protect the evacuation of allies from {enemy} waves.",
    "Conduct a high-risk reconnaissance sweep of {location} to extract data on {enemy} military strength.",
    "Neutralize a major supply hub of {enemy} situated in {location}.",
    "Assault a secure facility in {location} to rescue {target} currently guarded by {enemy}.",
    "Intercept an automated transport hauling {target} through {location} and secure the cargo.",
    "Investigate anomalous energy readings at {location} while defending your crew from {enemy} incursions.",
    "Sabotage the defensive battery shields of the {enemy} Dreadnought located near {location}."
]


def get_rank_and_color(level):
    if level <= 5:
        return "Cadet Recruit", Colors.COMMON
    elif level <= 15:
        return "Cadet Officer", Colors.RARE
    elif level <= 30:
        return "Cadet Commander", Colors.EPIC
    elif level <= 50:
        return "Starfleet Captain", Colors.LEGENDARY
    else:
        return "Fleet Admiral", Colors.ARTIFACT


def generate_mission(level):
    """Generates a mission based on the cadet level."""
    # Determine cadet rank info
    rank, rank_color = get_rank_and_color(level)

    # Calculate difficulty value (level + variance)
    # Variance increases slightly with level
    variance_range = max(1, level // 10)
    diff_val = level + random.randint(-variance_range, variance_range + 1)
    diff_val = max(1, diff_val)  # Clamp to min 1

    # Map diff_val to difficulty descriptors
    if diff_val <= 3:
        difficulty_name = "Trivial"
        diff_color = Colors.COMMON
    elif diff_val <= 8:
        difficulty_name = "Easy"
        diff_color = Colors.GREEN
    elif diff_val <= 15:
        difficulty_name = "Standard"
        diff_color = Colors.BLUE
    elif diff_val <= 25:
        difficulty_name = "Challenging"
        diff_color = Colors.CYAN
    elif diff_val <= 40:
        difficulty_name = "Expert"
        diff_color = Colors.WARNING
    elif diff_val <= 60:
        difficulty_name = "Heroic"
        diff_color = Colors.EPIC
    elif diff_val <= 80:
        difficulty_name = "Legendary"
        diff_color = Colors.LEGENDARY
    elif diff_val <= 100:
        difficulty_name = "Mythic"
        diff_color = Colors.FAIL
    else:
        difficulty_name = "Apocalyptic"
        diff_color = Colors.FAIL

    # Calculate difficulty stars (1-10)
    stars_count = min(10, max(1, (diff_val - 1) // 10 + 1))
    stars_str = "★" * stars_count + "☆" * (10 - stars_count)

    # Choose name components
    prefix = random.choice(NAME_PREFIXES)
    adjective = random.choice(NAME_ADJECTIVES)
    noun = random.choice(NAME_NOUNS)
    mission_name = f"{prefix} {adjective} {noun}"

    # Choose objective details
    location = random.choice(LOCATIONS)
    enemy = random.choice(ENEMIES)
    target = random.choice(TARGETS)

    objective = random.choice(OBJECTIVE_TEMPLATES).format(
        location=location,
        enemy=enemy,
        target=target
    )

    # Determine Reward Scale
    # Credits base is scaled by level and difficulty multiplier
    scale_mult = diff_val / level if level > 0 else 1.0
    credits_base = level * 1200 + 500
    credits = int(credits_base * random.uniform(0.85, 1.15) * scale_mult)
    credits = max(100, credits)

    exp_base = level * 200 + 100
    exp = int(exp_base * random.uniform(0.9, 1.1) * scale_mult)
    exp = max(50, exp)

    # Determine item rarity based on difficulty value
    # Small chance to upgrade or downgrade rarity
    rarity_roll = random.random()
    if diff_val <= 5:
        rarities = ["COMMON"]
    elif diff_val <= 15:
        rarities = ["COMMON", "RARE"] if rarity_roll < 0.3 else ["RARE"]
    elif diff_val <= 30:
        rarities = ["RARE"] if rarity_roll < 0.25 else (["EPIC"] if rarity_roll > 0.8 else ["RARE", "EPIC"])
    elif diff_val <= 50:
        rarities = ["EPIC"] if rarity_roll < 0.2 else (["LEGENDARY"] if rarity_roll > 0.85 else ["EPIC", "LEGENDARY"])
    elif diff_val <= 80:
        rarities = ["LEGENDARY"] if rarity_roll < 0.15 else (
            ["ARTIFACT"] if rarity_roll > 0.9 else ["LEGENDARY", "ARTIFACT"])
    else:
        rarities = ["ARTIFACT"] if rarity_roll < 0.3 else ["ARTIFACT", "LEGENDARY"]

    chosen_rarity = random.choice(rarities)
    loot_data = LOOT_TEMPLATES[chosen_rarity]
    item_name = f"{random.choice(loot_data['prefixes'])} {random.choice(loot_data['items'])}"

    return {
        "name": mission_name,
        "rank": rank,
        "rank_color": rank_color,
        "difficulty_name": difficulty_name,
        "diff_color": diff_color,
        "diff_val": diff_val,
        "stars_str": stars_str,
        "objective": objective,
        "credits": credits,
        "exp": exp,
        "item_name": item_name,
        "item_rarity": loot_data["label"],
        "item_color": loot_data["color"]
    }


def print_animated_text(text, delay=0.015, color=""):
    """Prints text with a subtle typewriter animation for visual polish."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Colors.ENDC + "\n")


def display_mission(mission, level):
    # Print double border card layout
    border_len = 70

    print()
    print_animated_text("╔" + "═" * (border_len - 2) + "╗", 0.002, Colors.BLUE)

    # Title centered
    title = f"✉  INCOMING MISSION BRIEFING  ✉"
    padding = (border_len - 2 - len(title)) // 2
    print(
        f"{Colors.BLUE}║{Colors.ENDC}" + " " * padding + f"{Colors.BOLD}{Colors.HEADER}{title}{Colors.ENDC}" + " " * padding + f"{Colors.BLUE}║{Colors.ENDC}")

    print(f"{Colors.BLUE}╠" + "═" * (border_len - 2) + "╣" + f"{Colors.ENDC}")

    # Mission Details
    print_field("Mission Name", f"{Colors.BOLD}{Colors.CYAN}{mission['name']}{Colors.ENDC}", border_len)

    cadet_status = f"{mission['rank_color']}{mission['rank']}{Colors.ENDC} (Level {level})"
    print_field("Cadet Clearance", cadet_status, border_len)

    diff_status = f"{mission['diff_color']}{mission['difficulty_name']}{Colors.ENDC} (Rating: {mission['diff_val']}) {Colors.WARNING}{mission['stars_str']}{Colors.ENDC}"
    print_field("Difficulty", diff_status, border_len)

    print(f"{Colors.BLUE}╟" + "─" * (border_len - 2) + "╢" + f"{Colors.ENDC}")

    # Objective (handles wrapping if long)
    obj_label = "Objective"
    words = mission['objective'].split()
    lines = []
    current_line = []
    line_limit = border_len - 20  # Leave room for label and margins

    for word in words:
        if sum(len(w) + 1 for w in current_line) + len(word) <= line_limit:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))

    for i, line in enumerate(lines):
        label = obj_label if i == 0 else ""
        print_field(label, f"{Colors.COMMON}{line}{Colors.ENDC}", border_len)

    print(f"{Colors.BLUE}╟" + "─" * (border_len - 2) + "╢" + f"{Colors.ENDC}")

    # Rewards
    print_field("Rewards", f"{Colors.GREEN}{mission['credits']:,} Galactic Credits{Colors.ENDC}", border_len)
    print_field("", f"{Colors.GREEN}{mission['exp']:,} EXP{Colors.ENDC}", border_len)

    loot_str = f"{mission['item_color']}[{mission['item_rarity']}] {mission['item_name']}{Colors.ENDC}"
    print_field("", loot_str, border_len)

    print_animated_text("╚" + "═" * (border_len - 2) + "╝", 0.002, Colors.BLUE)
    print()


def print_field(label, value, border_len):
    """Prints a structured field aligned nicely with borders."""
    clean_label = f"  {label:<16}" if label else " " * 18
    # Calculate visible length of value (ignoring ANSI color codes)
    visible_val_len = 0
    in_ansi = False
    for char in value:
        if char == '\033':
            in_ansi = True
        elif in_ansi and char == 'm':
            in_ansi = False
        elif not in_ansi:
            visible_val_len += 1

    spaces_needed = border_len - 2 - len(clean_label) - visible_val_len
    # Ensure it fits
    if spaces_needed < 0:
        spaces_needed = 0

    print(f"{Colors.BLUE}║{Colors.ENDC}{clean_label}{value}" + " " * spaces_needed + f"{Colors.BLUE}║{Colors.ENDC}")


def save_mission_briefing(mission, level):
    """Saves the mission briefing to a readable text file."""
    filename = "mission_briefing.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("======================================================================\n")
            f.write("                      OFFICIAL STARFLEET BRIEFING                     \n")
            f.write("======================================================================\n\n")
            f.write(f"Mission Name:     {mission['name']}\n")
            f.write(f"Clearance Level:  Level {level} ({mission['rank']})\n")
            f.write(
                f"Difficulty:       {mission['difficulty_name']} (Rating: {mission['diff_val']}) {mission['stars_str']}\n\n")
            f.write("----------------------------------------------------------------------\n")
            f.write("OBJECTIVE:\n")
            f.write(f"{mission['objective']}\n")
            f.write("----------------------------------------------------------------------\n\n")
            f.write("AUTHORIZED REWARDS:\n")
            f.write(f"  - {mission['credits']:,} Galactic Credits\n")
            f.write(f"  - {mission['exp']:,} Experience Points (EXP)\n")
            f.write(f"  - [{mission['item_rarity']}] {mission['item_name']}\n\n")
            f.write("======================================================================\n")
            f.write("                GOOD LUCK, CADET. SECURE THE SECTOR.                  \n")
            f.write("======================================================================\n")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False


def main():
    init_terminal()

    # Beautiful ASCII Banner
    print(f"\n{Colors.BOLD}{Colors.HEADER}")
    print(r"  🌌  ______________________________________________________  🌌  ")
    print(r"     /  \                                                   \     ")
    print(r"    |    |     🌌  GALACTIC MISSION GENERATOR v1.0  🌌       |    ")
    print(r"     \__/___________________________________________________/     ")
    print(f"{Colors.ENDC}")

    print_animated_text("Ready to scan galactic databases for custom operations...", 0.01, Colors.CYAN)

    while True:
        try:
            print(f"\n{Colors.BOLD}{Colors.BLUE}>>> Enter Cadet Level (1-100) or 'exit' to log out: {Colors.ENDC}",
                  end="")
            user_input = input().strip()

            if user_input.lower() in ['exit', 'quit']:
                print_animated_text("\nLogging out... Stay safe in the black, Cadet.", 0.01, Colors.WARNING)
                break

            if not user_input:
                continue

            level = int(user_input)
            if level <= 0:
                print(f"{Colors.FAIL}Error: Cadet Level must be a positive integer (>= 1).{Colors.ENDC}")
                continue

            # Simulated loading animation
            print(f"\n{Colors.CYAN}[*] Connecting to Starfleet Command Database...", end="", flush=True)
            time.sleep(0.4)
            print("\r[*] Accessing Cadet clearance credentials...    ", end="", flush=True)
            time.sleep(0.4)
            print("\r[*] Running procedural sector scan...          ", end="", flush=True)
            time.sleep(0.4)
            print("\r[+] Mission parameters generated! Decrypting... ", flush=True)
            time.sleep(0.2)

            # Generate and display
            mission = generate_mission(level)
            display_mission(mission, level)

            # Ask to save or generate again
            print(f"{Colors.BOLD}Would you like to save this mission briefing to a file? (y/n): {Colors.ENDC}", end="")
            save_choice = input().strip().lower()
            if save_choice in ['y', 'yes']:
                if save_mission_briefing(mission, level):
                    print(f"{Colors.GREEN}[✓] Briefing saved successfully to 'mission_briefing.txt'!{Colors.ENDC}")
                else:
                    print(f"{Colors.FAIL}[✗] Failed to save briefing.{Colors.ENDC}")

        except ValueError:
            print(f"{Colors.FAIL}Error: Please enter a valid integer level (1-100).{Colors.ENDC}")
        except KeyboardInterrupt:
            print_animated_text("\n\nOperation aborted. Connection lost.", 0.01, Colors.FAIL)
            break


if __name__ == "__main__":
    main()
