from collections import deque
from typing import List

from .graph import Graph, Vertex, cities


def dfs(cities: Graph, start: str, end: str) -> List[Vertex]:
    queue = [start]
    visited = []

    while queue:
        city_name = queue.pop()
        city = cities.vertex(city_name)
        visited.append(city)
        if city.name == end:
            return visited

        for edge in city.edges:
            if edge.end.name not in visited:
                queue.append(edge.end.name)

    return []


if __name__ == "__main__":
    path = dfs(cities, "Boston", "Washington")
    if path:
        print(path)
    else:
        print("No path found")
