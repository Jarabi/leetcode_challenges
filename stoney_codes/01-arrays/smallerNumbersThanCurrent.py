#!/usr/bin/python3

def main(nums):
    """
    How Many Numbers Are Smaller Than the Current

    For each item in `nums` find out how many numbers in the list are smaller than it.

    Args:
        nums (list): List of integers.
    """
    simple_result = simple(nums)
    optimal_result = optimal(nums)

    return simple_result, optimal_result


def simple(nums):
    """
    Time complexity: O(N^2)

    - Use of nested loops
    """
    result = []

    for i in range(len(nums)):
        smaller_than_count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                smaller_than_count += 1

        result.append(smaller_than_count)
    return result

def optimal(nums):
    """
    Time complexity: O(NlogN)

    - Using sorted(): O(NlogN)
    - Using a hashmap (dictionary): O(1)
    - Iterating through list once: O(N)
    """
    temp = sorted(nums)
    indices_map = {}
    result = []

    for index, value in enumerate(temp):
        if value not in indices_map:
            indices_map[value] = index

    for idx in nums:
        result.append(indices_map[idx])

    return result


if __name__ == "__main__":
    lst = [8,1,2,2,3]
    lst1 = [6,5,4,8]
    lst2 = [7,7,7,7]

    simple, optimal = main(lst)

    print("Simple:",simple)
    print("Optimal:",optimal)
