def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    product = 1
    for num in nums:
        if num % 2 == 0: # <-- this checks if the number is even it can be evenly divided by 2, which means the remainder of this division is 0.
            product *= num
    return product