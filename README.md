# optimal-fuel-routing

## Overview
This Django-based application exposes an API that computes and visualizes long-distance road trips across the United States. The system determines the most efficient driving route, identifies cost-effective refueling stops along the way, and calculates the total fuel cost for the journey.

## Key Features
- Generates an optimal driving route between a given start and destination using a free mapping and routing service.
- Selects the most economical fuel stops along the route based on available fuel price data.
- Estimates the total fuel expenditure for the trip using:
  - Vehicle range of 500 miles per full tank
  - Fuel efficiency of 10 miles per gallon
- Leverages a predefined fuel price dataset to accurately compute refueling costs throughout the journey.

## How It Works

1. **Input**  
   Users provide a start and destination location within the USA.

2. **Route Calculation**  
   The API computes the optimal driving route using a free mapping and routing service.

3. **Fuel Stop Optimization**  
   - The calculated route is divided into segments of up to **500 miles**, matching the vehicle’s maximum range per tank.
   - For each segment, the system selects the most cost-effective refueling stop based on available fuel price data.

4. **Output**  
   - A visual map displaying the full route with refueling stops clearly marked.
   - A JSON response containing the total fuel cost and additional trip details.

## Prerequisites
- Python 3.11
- Install dependencies listed in `requirements.txt`.
   ```bash
    pip install -r requirements.txt
   ```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Willie-theBeastMutua/optimal-fuel-routing.git
   cd optimal-fuel-routing
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   cd backend
   ```
4. Import fuel station data:
   ```bash
   python manage.py import_stations

5. Run the API server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints
### 1. **Calculate Route and Fuel Stops**
   **Endpoint**: `/api/route/`
   
   **Method**: POST
   
   **Request Body**:
   ```json
   {
       "start": "New York, NY, USA",
       "end": "Los Angeles, CA, USA"
   }
   ```
   
   **Response**:
   ```json
   {
    "route_coordinates": ["Coordinates between start and end location"],
    "map_url": "URL-to-route-map",
    "fuel_stops": ["Fuel stops along the route"],
    "total_cost": 123.45,
    "total_distance": 500.0
}
   ```

## Fuel Price Dataset
- The API uses a provided dataset containing fuel prices across various locations in the USA.  
  Ensure the dataset is placed at the following location before running the server:

  ```text
  optimal-fuel-routing/backend/fuel-prices-for-be-assessment.csv
```

## Technologies Used
- **Backend**: Django
- **Mapping API**: Free map and routing API (e.g., OpenRouteService, MapQuest, or similar)


