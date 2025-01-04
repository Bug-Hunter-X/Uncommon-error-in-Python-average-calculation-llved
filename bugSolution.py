def calculate_average(numbers):
    if not numbers:
        return 0
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers.")
    return sum(numbers) / len(numbers)