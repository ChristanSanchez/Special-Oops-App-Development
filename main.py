from backend.mapquest_service import get_route


# Terminal colors
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"


# MapQuest turnType directions
def get_direction_arrow(turn_type):
    arrows = {
        0: "↑",    # Straight
        1: "↗",    # Slight right
        2: "→",    # Right
        3: "↘",    # Sharp right
        4: "↩",    # Reverse
        5: "↙",    # Sharp left
        6: "←",    # Left
        7: "↖",    # Slight left
        8: "↩",    # Right U-turn
        9: "↩",    # Left U-turn
        10: "↗",   # Right merge
        11: "↖",   # Left merge
        12: "↑",   # Straight merge
        13: "↑",   # Straight
        14: "→",   # Right off ramp
        15: "←",   # Left off ramp
        16: "→",   # Right fork
        17: "←",   # Left fork
        18: "↑"    # Straight fork
    }

    return arrows.get(turn_type, "•")


def print_header():
    print("\n")
    print(CYAN + "╔══════════════════════════════════════════════╗" + RESET)
    print(CYAN + "║" + RESET + "            MAPQUEST ROUTE FINDER             " + CYAN + "║" + RESET)
    print(CYAN + "╠══════════════════════════════════════════════╣" + RESET)
    print(CYAN + "║" + RESET + "  Find the best route between two locations   " + CYAN + "║" + RESET)
    print(CYAN + "╚══════════════════════════════════════════════╝" + RESET)


def select_unit():
    while True:
        print("\n" + BLUE + "DISTANCE UNIT" + RESET)
        print("┌──────────────────────────────┐")
        print("│ [1] Miles                    │")
        print("│ [2] Kilometers               │")
        print("└──────────────────────────────┘")

        choice = input("Select an option [1-2]: ").strip()

        if choice == "1":
            return "m", "miles"

        if choice == "2":
            return "k", "kilometers"

        print(RED + "Invalid choice. Please enter 1 or 2." + RESET)


def select_route_type():
    while True:
        print("\n" + BLUE + "ROUTE TYPE" + RESET)
        print("┌──────────────────────────────┐")
        print("│ [1] ⚡ Fastest               │")
        print("│ [2] 📏 Shortest              │")
        print("└──────────────────────────────┘")

        choice = input("Select an option [1-2]: ").strip()

        if choice == "1":
            return "fastest"

        if choice == "2":
            return "shortest"

        print(RED + "Invalid choice. Please enter 1 or 2." + RESET)


def show_route_error(error_message):

    error_lower = error_message.lower()

    if "connect" in error_lower or "connection" in error_lower:
        title = "CONNECTION ERROR"
        message = "Unable to connect to MapQuest."
        suggestion = "Please check your internet connection."

    elif "api key" in error_lower or "unauthorized" in error_lower:
        title = "AUTHENTICATION ERROR"
        message = "The MapQuest API key is invalid."
        suggestion = "Please check your API key configuration."

    elif "valid route" in error_lower:
        title = "ROUTE NOT FOUND"
        message = "No valid route could be found."
        suggestion = "Please check the locations and try again."

    elif "empty" in error_lower:
        title = "INVALID INPUT"
        message = "A location was left empty."
        suggestion = "Please enter both locations."

    else:
        title = "ROUTE SEARCH FAILED"
        message = "MapQuest was unable to process the request."
        suggestion = "Please check your locations and try again."

    print("\n")

    print(RED + "╔══════════════════════════════════════════════╗" + RESET)
    print(RED + "║                                              ║" + RESET)
    print(RED + "║                     ✖✖✖                      ║" + RESET)
    print(RED + "║                     ✖✖✖                      ║" + RESET)
    print(RED + "║                     ✖✖✖                      ║" + RESET)
    print(RED + "║                                              ║" + RESET)
    print(RED + "║         " + title.center(28) + "         ║" + RESET)
    print(RED + "║                                              ║" + RESET)
    print(RED + "║      " + message.center(36) + "    ║" + RESET)
    print(RED + "║   " + suggestion.center(40) + "  ║" + RESET)
    print(RED + "║                                              ║" + RESET)
    print(RED + "╚══════════════════════════════════════════════╝" + RESET)


def show_route(result, origin, destination, unit_label):

    print("\n")
    print(GREEN + "╔═══════════════════ ROUTE ══════════════════════╗" + RESET)

    print(
        GREEN + "║" + RESET +
        " From     : " + origin
    )

    print(
        GREEN + "║" + RESET +
        " To       : " + destination
    )

    print(
        GREEN + "║" + RESET +
        " Route    : " + result["route_type"].title()
    )

    print(
        GREEN + "║" + RESET +
        " Distance : {:.2f} {}".format(
            result["distance"],
            unit_label
        )
    )

    print(
        GREEN + "║" + RESET +
        " Duration : " + result["travel_time"]
    )

    print(GREEN + "╚════════════════════════════════════════════════╝" + RESET)

    print("\n" + BLUE + "DIRECTIONS" + RESET)
    print("────────────────────────────────────────────────")

    for number, step in enumerate(result["directions"], 1):

        arrow = get_direction_arrow(step["turn_type"])

        distance = step["distance"]

        if unit_label == "miles":
            distance_unit = "mi"
        else:
            distance_unit = "km"

        print(
            "{:02d}  {}  {} ({:.2f} {})".format(
                number,
                arrow,
                step["narrative"],
                distance,
                distance_unit
            )
        )

    print("────────────────────────────────────────────────")


def ask_continue():

    while True:
        print("\n" + CYAN + "WHAT WOULD YOU LIKE TO DO?" + RESET)
        print("┌────────────────────────────────────┐")
        print("│ [1] Search another route           │")
        print("│ [2] Exit                           │")
        print("└────────────────────────────────────┘")

        choice = input("Select an option [1-2]: ").strip()

        if choice == "1":
            return True

        if choice == "2":
            return False

        print(RED + "Invalid choice. Please enter 1 or 2." + RESET)


while True:

    print_header()

    print("\n" + YELLOW + "ENTER LOCATIONS" + RESET)

    origin = input("Starting Location: ").strip()

    if origin.lower() in ["quit", "q"]:
        print("\nGoodbye!")
        break

    if not origin:
        show_route_error("Starting location cannot be empty.")
        continue

    destination = input("Destination: ").strip()

    if destination.lower() in ["quit", "q"]:
        print("\nGoodbye!")
        break

    if not destination:
        show_route_error("Destination cannot be empty.")
        continue

    unit, unit_label = select_unit()

    route_type = select_route_type()

    print("\n" + CYAN + "SEARCHING FOR ROUTE..." + RESET)
    print("From: " + origin)
    print("To  : " + destination)

    result = get_route(
        origin,
        destination,
        unit,
        route_type
    )

    if result["success"]:

        print(
            GREEN +
            "✓ Route found successfully!" +
            RESET
        )

        show_route(
            result,
            origin,
            destination,
            unit_label
        )

    else:

        show_route_error(result["error"])

    if not ask_continue():
        print("\nGoodbye!")
        break