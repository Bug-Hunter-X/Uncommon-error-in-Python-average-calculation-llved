# Uncommon Error in Python Average Calculation

This repository demonstrates a potential error in a Python function designed to calculate the average of a list of numbers.  The function correctly handles empty lists, but it's susceptible to errors if the input list contains non-numeric data.

## Bug Description:

The `calculate_average` function fails gracefully with an empty list, returning 0. However, if the input list contains any non-numeric elements (strings, booleans, etc.), it will raise a `TypeError` during the `sum()` operation. This is an uncommon error because the empty list case is often explicitly handled, but the non-numeric data case might be overlooked. 

## Solution:

The provided solution includes comprehensive input validation to prevent this error. It checks for empty lists and also ensures that all elements in the list are numeric before performing the calculation.