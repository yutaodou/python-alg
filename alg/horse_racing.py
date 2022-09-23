from typing import List


def race(horses: List[int], king_horses: List[int]):
    my_sorted_by_power = sorted(horses)

    my_paired = set()
    pairs = []

    def find_pair_for(king_horse: List[int]) -> int:
        # return winning horse with least horse power if can win
        for my in my_sorted_by_power:
            if my > king_horse and my not in my_paired:
                return my

        # return horses with smallest possible horses if not possible to win
        for my in my_sorted_by_power:
            if my not in my_paired:
                return my

        return None

    for king_horse in king_horses:
        my_pair = find_pair_for(king_horse)
        my_paired.add(my_pair)
        pairs.append([my_pair, king_horse])

    return pairs


horse_pairs = race([12, 24, 8, 32], [13, 25, 32, 11])
for pair in horse_pairs:
    print(f"{pair[0]} -> {pair[1]}")
