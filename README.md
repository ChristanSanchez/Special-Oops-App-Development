# Special Ops App Development

A Python application that uses the MapQuest Directions API to retrieve and display route information between two locations.

## Current Project Features

- Enter starting location and destination
- Display route distance
- Display estimated travel time
- Display step-by-step directions
- Choose between miles and kilometers
- Choose between fastest and shortest route
- Basic input validation
- Basic API and route error handling

## Run Project
1. Open VSCode
2. Run "python -m pip install requests"
3. Run "set MAPQUEST_API_KEY=5Q3qRHQWiYluBfqES1CmPOIJbVtv0Q9j" or "$env:MAPQUEST_API_KEY=5Q3qRHQWiYluBfqES1CmPOIJbVtv0Q9j"
4. Run "python main.py"

## Project Structure

```text
Special-Oops-App-Development/
│
├── backend/
│   └── mapquest_service.py
│
├── tests/
│   └── test_mapquest.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
