from rest_framework.views import APIView
from rest_framework.response import Response

from .services.routing_service import get_route
from .services.fuel_prices import load_fuel_prices
from .services.fuel_optimizer_dp import optimize_fuel_dp

class RouteAPIView(APIView):
    def post(self, request):
        start = request.data["start"]
        end = request.data["end"]

        route = get_route(start, end)
        geometry = route["features"][0]["geometry"]

        coords = [(c[1], c[0]) for c in geometry["coordinates"]]

        fuel_df = load_fuel_prices()
        stops, cost = optimize_fuel_dp(coords, fuel_df)

        return Response({
            "distance_miles": round(
                route["features"][0]["properties"]["summary"]["distance"] / 1609.34, 2
            ),
            "route": geometry,
            "fuel_stops": stops,
            "total_fuel_cost": cost
        })
