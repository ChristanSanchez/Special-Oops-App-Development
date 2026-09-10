from backend.mapquest_service import get_route


origin = input("Enter starting location: ")
destination = input("Enter destination: ")

print("\nChoose unit:")
print("1 - Miles")
print("2 - Kilometers")

unit_choice = input("Enter choice: ")

if unit_choice == "2":
    unit = "k"
    unit_label = "kilometers"
else:
    unit = "m"
    unit_label = "miles"


print("\nChoose route type:")
print("1 - Fastest")
print("2 - Shortest")

route_choice = input("Enter choice: ")

if route_choice == "2":
    route_type = "shortest"
else:
    route_type = "fastest"


result = get_route(origin, destination, unit, route_type)


if result["success"]:
    print("\n--- ROUTE INFORMATION ---")
    print("Route Type:", result["route_type"].title())
    print("Distance:", result["distance"], unit_label)
    print("Travel Time:", result["travel_time"])

    print("\nDirections:")

    for step in result["directions"]:
        print("-", step)

else:
    print("\nError:", result["error"])