#!/usr/bin/python3
"""Find a peak element in a list of unsorted integers using binary search"""


def find_peak(list_of_integers):
    """
    Find a peak element in a list of unsorted integers using binary search.

    Parameters:
    - list_of_integers (list): A list of unsorted integers.

    Returns:
    - int or None: The peak element found in the list, or None if the list is empty.

    Algorithm:
    This function uses a binary search algorithm to efficiently find a peak element
    in the given list of integers. A peak element is defined as an element that is
    greater than its neighboring elements (if they exist). The function operates on
    the assumption that there may be more than one peak in the list.

    1. Check if the input list is empty. If it is, return None to indicate an empty list.
    2. Initialize the search range with 'low' as the first index and 'high' as the last index.
    3. Perform binary search to iteratively narrow down the search range until a peak is found.
    4. Calculate the midpoint 'mid' of the current search range.
    5. Compare the element at 'mid' with the element at 'mid + 1' to determine the direction of the search:
       - If 'list_of_integers[mid] > list_of_integers[mid + 1]', update 'high' to 'mid'.
       - If not, update 'low' to 'mid + 1'.
    6. Repeat steps 4 and 5 until 'low' and 'high' converge to a peak.
    7. Return the peak element found in the list.

    Example Usage:
    >>> find_peak([1, 2, 4, 6, 3])
    6
    >>> find_peak([4, 2, 1, 2, 3, 1])
    4

    Note: This function has a time complexity of O(log(n)), making it efficient for large lists.

    """
    # Check if the list is empty
    if not list_of_integers:
        return None

    # Initialize the search range
    low = 0
    high = len(list_of_integers) - 1

    # Perform binary search to find the peak
    while low < high:
        # Calculate the midpoint of the current search range
        mid = (low + high) // 2

        # Check if the element at the midpoint is greater than the next element
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If it is, update the high end of the search range
            high = mid
        else:
            # If it's not, update the low end of the search range
            low = mid + 1

    # The loop terminates when low and high converge to a peak
    # Return the peak element
    return list_of_integers[low]

