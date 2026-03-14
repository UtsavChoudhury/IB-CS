def fun(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The GCD of the two numbers.
    """
    while b != 0:
        a, b = b, a % b
    return a
