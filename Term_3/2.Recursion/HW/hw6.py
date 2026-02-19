def is_palindrome(lst):
    if not lst or len(lst) == 1:
        return True
    if lst[0] == lst[-1]:
        return is_palindrome(lst[1: len(lst) - 1])
    else:
        return False
    