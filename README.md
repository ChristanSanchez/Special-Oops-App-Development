# Special Ops App Development - MapQuest Route Application

A Python application that uses the MapQuest Directions API to retrieve and display route information between two locations.

This project enhances the original MapQuest REST API activity by adding route options, validation, testing, and a backend structure that can later be connected to a graphical frontend.

---

## Team Instructions

### For Frontend Developer

Use this backend function:

from backend.mapquest_service import get_route

Call it like this:

result = get_route(origin, destination, unit, route_type)

Inputs:
- origin = starting location
- destination = destination location
- unit = "m" for miles or "k" for kilometers
- route_type = "fastest" or "shortest"

Handled na ng backend ang:
- MapQuest API request
- Distance
- Travel time
- Step-by-step directions
- Input validation
- Basic API and route error handling

So sa frontend side, focus lang sa UI and kung paano idi-display yung results.

---

### For Tester

Run the application using:

python main.py

Run the backend tests using:

python -m tests.test_mapquest

Please test:
- Valid origin and destination
- Empty origin
- Empty destination
- Miles option
- Kilometers option
- Fastest route
- Shortest route
- Invalid or unknown location
- API or connection error

Expected behavior:
- Kapag valid ang route, dapat lalabas ang distance, travel time, route type, and directions.
- Kapag invalid ang input or may error, dapat may mag-display ng proper error message instead na mag-crash yung program.

---

### Future Backlog

Possible features for future development:

- Avoid toll roads
- Avoid highways
- Alternative route suggestions
- Estimated fuel cost
- Recent searched locations
- Favorite locations
- Improved graphical user interface

Hindi pa kasama ang mga ito sa current version. Pwede natin silang i-prioritize sa future sprints depending sa available time and project requirements.

---

Pwede niyo i-remove itong Team Instructions section kapag nabasa and nagets niyo na  frontend developer and tester.
