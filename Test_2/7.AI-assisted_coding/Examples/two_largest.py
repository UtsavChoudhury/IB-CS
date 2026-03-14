def two_largest(numbers):
    """
    Returns the two largest numbers in a list.
    
    Args:
        numbers: A list of numbers
        
    Returns:
        A tuple containing the two largest numbers (largest, second_largest)
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least 2 numbers")
    
    largest = max(numbers[0], numbers[1])
    second_largest = min(numbers[0], numbers[1])
    
    for num in numbers[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    
    return (largest, second_largest)