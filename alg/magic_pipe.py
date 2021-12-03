from typing import Counter, List
from itertools import count


def magic_pipe(n: int, names: List[str]) -> str:
    def size(names: List[str], loop: int) -> int:
        if loop == 0:
            return len(names)

        return len(names) * pow(2, loop) + size(names, loop - 1)

    for loop in count():
        queue_size = size(names, loop)
        if queue_size == n:
            return names[-1]
        elif queue_size > n:
            fully_loopped = size(names, loop - 1)
            reminders = n - fully_loopped
            for idx in range(len(names)):
                if (idx + 1) * pow(2, loop) >= reminders:
                    return names[idx]

    return ""


print(magic_pipe(7, ["A", "B", "C", "D"]))
