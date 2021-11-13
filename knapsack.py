from typing import NamedTuple, List


class Item(NamedTuple):
    name: str
    weight: int
    value: int


class Solution:
    def __init__(self):
        self.items = []
        self.total = 0

    def append(self, item):
        self.items.append(item)
        self.total = sum(item.value for item in self.items)

    def __repr__(self):
        return f"total: {self.total}, items: {self.items}"


def knapsack(items: List[Item], max_capacity: int) -> Solution:
    solution = Solution()

    table = [[0 for _ in range(max_capacity + 1)] for _ in range(len(items))]

    for i, item in enumerate(items):
        for capacity in range(1, max_capacity + 1):
            previous_value = table[i - 1][capacity] if i > 0 else 0

            if capacity >= item.weight:
                free_space_value_if_take = table[i - 1][capacity - item.weight]
                table[i][capacity] = max(
                    free_space_value_if_take + item.value, previous_value
                )
            else:
                table[i][capacity] = previous_value

    for values in table:
        print(values)

    capacity = max_capacity
    for i in range(len(items) - 1, -1, -1):
        if (i > 0 and table[i][capacity] != table[i - 1][capacity]) or (
            i == 0 and table[i][capacity] > 0
        ):
            solution.append(items[i])
            capacity -= items[i].weight
    return solution


if __name__ == "__main__":
    items = [
        Item("tv", 5, 500),
        Item("candlesticks", 2, 300),
        Item("stereo", 3, 400),
        Item("laptop", 3, 1000),
        Item("food", 2, 50),
    ]
    print(knapsack(items, 8))
