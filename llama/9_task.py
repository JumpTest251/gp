from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest = min(numbers)
    largest = max(numbers)
  
    # find the closest pair of numbers to each other
    diff_smallest = [abs(x - smallest) for x in numbers]
    diff_largest = [abs(x - largest) for x in numbers]
    closest_pair = [(smallest, largest)] if min(diff_smallest + diff_largest) == 0 else [(numbers[i], numbers[j]) for i, j in enumerate(numbers) if abs(numbers[i] - numbers[j]) == min(diff_smallest + diff_largest)]
  
    return closest_pair