from geopy.distance import geodesic
import math

MAX_RANGE = 500      
MPG = 10             

def optimize_fuel_dp(route_coords, fuel_df):
    route_points = []
    total_distance = 0.0
    route_points.append((route_coords[0], 0.0))

    for i in range(1, len(route_coords)):
        d = geodesic(route_coords[i-1], route_coords[i]).miles
        total_distance += d
        route_points.append((route_coords[i], total_distance))

    stations = []
    for _, row in fuel_df.iterrows():
        closest = min(route_points, key=lambda p: geodesic(p[0], (row.lat, row.lng)).miles)
        stations.append({
            "distance": closest[1],
            "lat": row.lat,
            "lng": row.lng,
            "price": row.price
        })

    nodes = [{
        "distance": 0.0,
        "price": min(s["price"] for s in stations),
        "type": "start"
    }] + stations + [{
        "distance": total_distance,
        "price": 0,
        "type": "end"
    }]

    nodes.sort(key=lambda x: x["distance"])

    n = len(nodes)
    dp = [math.inf] * n
    prev = [-1] * n
    dp[0] = 0

    for i in range(n):
        for j in range(i+1, n):
            dist = nodes[j]["distance"] - nodes[i]["distance"]
            if dist > MAX_RANGE:
                break

            fuel_needed = dist / MPG
            cost = fuel_needed * nodes[i]["price"]

            if dp[i] + cost < dp[j]:
                dp[j] = dp[i] + cost
                prev[j] = i

    path = []
    idx = n - 1
    while idx > 0:
        if nodes[idx].get("type") != "end":
            path.append(nodes[idx])
        idx = prev[idx]

    return list(reversed(path)), round(dp[-1], 2)
