def powersort(lst):
    """
    Sorts the list of integers first by the sum of their digits (ascending),
    then by their original value (ascending) if digit sums are equal.
    """
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))
    return sorted(lst, key=lambda x: (digit_sum(x), x))


