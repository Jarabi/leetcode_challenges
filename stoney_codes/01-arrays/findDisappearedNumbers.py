#!/usr/bin/python3

def main(nums):
    """
    Find All Numbers Disappeared in a List

    Args:
        nums (list): List of integers

    Return:
        list: List on integers
    """
    simple_result = simple(nums)
    optimal_result = optimal(nums)

    return simple_result, optimal_result

def simple(nums):
    """
    Time complexity: O(N^2)

    - Algorithm uses a `for loop` combined with the `in keyword
    O(N) * O(N)
    """
    missing = []

    for item in range(1, len(nums) + 1):
        if item not in nums:
            missing.append(item)
    return missing

def optimal(nums):
    """
    Time complexity: O(N)

    - Employs `set` which makes membership checks faster: O(1)
    - Iteration over the range: O(N)
    O(N) * O(1)
    """
    missing = []
    set_nums = set(nums)

    for item in range(1, len(nums) + 1):
        if item not in set_nums:
            missing.append(item)
    return missing


if __name__ == "__main__":
    lst = [4,3,2,7,8,2,3,1]
    lst1 = [1,1]

    simple, optimal = main(lst)
    print("Simple:",simple)
    print("Optimal:",optimal)
