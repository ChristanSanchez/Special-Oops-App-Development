from backend.mapquest_service import get_route


print("=== MAPQUEST BACKEND TEST ===")


# Test 1: Valid route
print("\nTest 1: Valid Route")

result = get_route(
    "Quezon City",
    "Manila",
    "k",
    "fastest"
)

if result["success"]:
    print("PASS")
    print("Distance:", result["distance"])
    print("Travel Time:", result["travel_time"])
else:
    print("FAIL:", result["error"])


# Test 2: Empty location
print("\nTest 2: Empty Origin")

result = get_route(
    "",
    "Manila",
    "k",
    "fastest"
)

if not result["success"]:
    print("PASS:", result["error"])
else:
    print("FAIL")


# Test 3: Shortest route
print("\nTest 3: Shortest Route")

result = get_route(
    "Manila",
    "Quezon City",
    "k",
    "shortest"
)

if result["success"]:
    print("PASS")
    print("Distance:", result["distance"])
    print("Travel Time:", result["travel_time"])
else:
    print("FAIL:", result["error"])