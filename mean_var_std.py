import numpy as np
from mean_var_std import calculate

# Test cases
input_lists = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8],  # Example list from the prompt
    [1, 2, 3, 4, 5, 6, 7, 8, 9],  # Another list for testing
    [10, 20, 30, 40, 50, 60, 70, 80, 90]  # Yet another list for testing
]

# Iterate over input lists and test the calculate function
for idx, lst in enumerate(input_lists):
    print(f"Test Case {idx + 1}:")
    try:
        result = calculate(lst)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print()
