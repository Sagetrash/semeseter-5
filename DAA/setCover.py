def greedy_set_cover(universe, subsets):
    uncovered = set(universe)
    cover = []

    while uncovered:
        best_set = max(subsets, key=lambda s: len(uncovered.intersection(s)))
        newly_covered_count = len(uncovered.intersection(best_set))
        
        if newly_covered_count == 0:
            break 

        cover.append(best_set)
        uncovered.difference_update(best_set)
    return cover

U = set(range(1, 11))

S = [
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10},
    {1, 5, 9},
    {2, 6, 10},
    {3, 7},
    {4, 8}
]

result_cover = greedy_set_cover(U, S)

print(f"Universal Set: {U}")
print(f"Greedy Cover Found: {result_cover}")
print(f"Size: {len(result_cover)}")