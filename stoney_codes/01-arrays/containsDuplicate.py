#!/usr/bin/python3

def main(nums):
    """
    Checks if `nums` list has duplicates.

    Args:
        nums (list): An integer list.

    Returns:
        bool: True if duplicate exists, else False

    Raises:
        ValueError: If `nums` is not a list.
    """
    if not isinstance(nums, list):
        raise ValueError("Must be a list.")

    if len(nums) < 2:
        return False

    simple_result = simple(nums)
    optimal_result = optimal(nums)

    return simple_result, optimal_result

def simple(nums):
    """Time complexity: O(N^2)"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def optimal(nums):
    """
    Time complexity: O(N)

    Notes:
    - Sets are implemented as hash tables; lookup/insert/delete time complexity of O(1)
    """
    return False if len(set(nums)) == len(nums) else True


if __name__ == "__main__":
    _list = [1, 2, 3, 9, 4, 3]
    simple, optimal = main(_list)
    print("Simple solution:", simple)
    print("Optimal solution:", optimal)
