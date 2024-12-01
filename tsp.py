
from itertools import permutations
def calculate(distance,route):
    # calculate the total distance of the route
    return sum(distance[route[i-1]][route[i]] for i in range(len(route)))



def tsp(distance):
    cities = range(len(distance))
    short_dist = 2**31
    best_route = None
    for route in permutations(cities):
        route = list(route) + [route[0]]
        if calculate(distance,route) < short_dist:
            short_dist = calculate(distance,route)
            best_route = route
    return short_dist,best_route


print(tsp([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]))

    