#!/usr/bin/python3

def main(nums):
    """
    Missing number: Check for missing numbers in `nums`

    Args:
        nums (list): An integer list.

    Returns:
        int: Missing number in `nums`

    Raises:
        ValueError: If `nums` is not a list.
    """
    if not isinstance(nums, list):
        raise ValueError("Must be a list.")

    simple_result = simple(nums)
    optimal_result = optimal(nums)

    return simple_result, optimal_result

def simple(nums):
    """
    Time complexity: O(N), due to the use of `in` keyword which results in an O(1) for each element making it
    slower for large lists.
    """
    for item in range(len(nums) + 1):
        if item not in nums:
            return item

def optimal(nums):
    """
    Time complexity: O(N)

    Notes:
        - len() = O(1)
        - range object creation = O(1)
        - sum() = O(N)
        * +1 used in range(n) because n will be excluded otherwise
    """
    return sum(range(len(nums) + 1)) - sum(nums)


if __name__ == "__main__":
    _list = [3,0,1]
    _list1 = [0, 1]
    _list2 = [9,6,4,2,3,5,7,0,1]

    simple, optimal = main(_list1)
    print("Simple result",simple)
    print("Optimal result", optimal)