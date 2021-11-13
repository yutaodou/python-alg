from abc import ABC, abstractmethod
from typing import Dict, Generic, List, NamedTuple, Set, Type, TypeVar

V = TypeVar("V")
D = TypeVar("D")


class Constraint(Generic[V, D], ABC):
    @abstractmethod
    def satisfied(self, variable: V, assignments: Dict[V, D]) -> bool:
        pass


class CSP(Generic[V, D]):
    def __init__(
        self,
        variables: List[V],
        domains: Dict[V, List[D]],
        constraint: Constraint,
    ) -> None:
        self.variables = variables
        self.domains = domains
        self.constraint = constraint

    def satisfied(self, assignments: Dict[V, D]) -> bool:
        for k, _ in assignments.items():
            if not self.constraint.satisfied(k, assignments):
                return False

        return True

    def backtracking_search(self, assignments: Dict[V, D]) -> Dict[V, D]:
        if len(self.variables) == len(assignments):
            return assignments

        unassigned = [v for v in self.variables if v not in assignments]

        next_attempt = unassigned[0]
        for d in self.domains[next_attempt]:
            attempt = assignments.copy()
            attempt[next_attempt] = d
            if self.satisfied(attempt):
                attempt = self.backtracking_search(attempt)
                if attempt:
                    return attempt

        return dict()


class Position(NamedTuple):
    x: int
    y: int


class QueenConstraint(Constraint):
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols

    def satisfied(self, variable: int, assignments: Dict[int, Position]) -> bool:
        if variable not in assignments:
            return True

        current = assignments[variable]
        territory = self.territory(current)

        others = list(
            position for idx, position in assignments.items() if idx != variable
        )
        collisions = [p for p in others if p in territory]
        return len(collisions) == 0

    def territory(self, position: Position) -> Set[Position]:
        positions = set()
        for x in range(self.cols):
            positions.add(Position(x, position.y))

        for y in range(self.rows):
            positions.add(Position(position.x, y))

        x, y = position.x - 1, position.y - 1
        while x >= 0 and y >= 0:
            positions.add(Position(x, y))
            x -= 1
            y -= 1

        x, y = position.x, position.y
        while x < self.cols - 1 and y < self.rows - 1:
            positions.add(Position(x + 1, y + 1))
            x += 1
            y += 1

        return positions


# const = QueenConstraint(8, 8)
# print(const.territory(Position(0, 0)))


def print_solution(rows: int, cols: int, solution: Dict[int, Position]):
    flipped = {v: k for k, v in solution.items()}
    for row in range(rows):
        for col in range(cols):
            end = "\n" if col + 1 == cols else ""
            queen = flipped.get(Position(row, col))
            if queen is not None:
                print(f"{queen}", end=end)
            else:
                print("-", end=end)


if __name__ == "__main__":
    rows, cols = 8, 8
    variables = list(range(8))
    positions = [Position(x, y) for x in range(rows) for y in range(cols)]

    domains = dict((v, positions) for v in variables)

    csp = CSP(variables, domains, QueenConstraint(rows, cols))

    solution = csp.backtracking_search({})
    if solution:
        print_solution(rows, cols, solution)
    else:
        print("no solution")
