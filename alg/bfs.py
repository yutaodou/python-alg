# breadth first search
from typing import List, Dict
from .graph import cities, Graph, Vertex, Edge


def bfs(graph: Graph, start: str, end: str) -> List[Vertex]:
    visited = []
    queue = [start]

    while queue:
        name = queue.pop()
        city = graph.vertex(name)
        visited.append(name)

        for edge in city.edges:
            next_stop = edge.end.name
            print(f"next: {next_stop}")
            if next_stop == end:
                visited.append(next_stop)
                return visited

            if next_stop not in visited:
                queue.insert(0, next_stop)

    return []


if __name__ == "__main__":
    path = bfs(cities, "Boston", "Washington")
    print(path)
