from itertools import combinations

def equal_sum_partitions(lst):
    """
    Returns all possible ways to partition the list into two non-empty subsets with equal sums.
    Each partition is represented as a tuple of two lists.
    """
    result = []
    n = len(lst)
    total = sum(lst)
    if n < 2 or total % 2 != 0:
        return result  # No possible partition

    target = total // 2
    seen = set()
    # Generate all possible non-empty subsets except the full set and empty set
    for r in range(1, n // 2 + 1):
        for indices in combinations(range(n), r):
            subset1 = [lst[i] for i in indices]
            if sum(subset1) == target:
                subset2 = [lst[i] for i in range(n) if i not in indices]
                # To avoid duplicates, use sorted tuple of subsets as key
                key = tuple(sorted(subset1)), tuple(sorted(subset2))
                if key not in seen:
                    result.append((subset1, subset2))
                    seen.add(key)
    return result