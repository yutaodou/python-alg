from __future__ import annotations
from typing import DefaultDict, List, Optional
from dataclasses import dataclass, field


@dataclass
class Vertex:
    name: str
    edges: List[Edge] = field(default_factory=list)


@dataclass
class Edge:
    start: Vertex
    end: Vertex
    weight: float = 0


class Graph:
    def __init__(self) -> None:
        self.vertices = []

    def vertex(self, name: str) -> Vertex:
        vertex = next((v for v in self.vertices if v.name == name), None)
        if vertex is None:
            vertex = Vertex(name)
            self.vertices.append(vertex)
        return vertex

    def add_edge(self, start: str, end: str, weight: float = 0):
        start_v = self.vertex(start)
        end_v = self.vertex(end)
        start_v.edges.append(Edge(start_v, end_v, weight))


cities = Graph()
cities.add_edge("Seattle", "Chicago")
cities.add_edge("Seattle", "San Francisco")
cities.add_edge("San Fancisco", "Riverside")
cities.add_edge("San Fancisco", "Los Angeles")
cities.add_edge("Los Angeles", "Riverside")
cities.add_edge("Los Angeles", "Phoenix")
cities.add_edge("Riverside", "Phoenix")
cities.add_edge("Riverside", "Chicago")
cities.add_edge("Phoenix", "Dallas")
cities.add_edge("Phoenix", "Houston")
cities.add_edge("Dallas", "Chicago")
cities.add_edge("Dallas", "Atlanta")
cities.add_edge("Dallas", "Houston")
cities.add_edge("Houston", "Atlanta")
cities.add_edge("Houston", "Miami")
cities.add_edge("Atlanta", "Chicago")
cities.add_edge("Atlanta", "Washington")
cities.add_edge("Atlanta", "Miami")
cities.add_edge("Miami", "Washington")
cities.add_edge("Chicago", "Detroit")
cities.add_edge("Detroit", "Boston")
cities.add_edge("Detroit", "Washington")
cities.add_edge("Detroit", "New York")
cities.add_edge("Boston", "New York")
cities.add_edge("New York", "Philadelphia")
cities.add_edge("Philadelphia", "Washington")
