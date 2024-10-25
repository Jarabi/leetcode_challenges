#!/usr/bin/python3

def main(nums, target):
    """
    Two Sum

    Return indices of the two numbers in `nums` such they add up to `target`
    """
    simple_result = simple(nums, target)
    optimal_result = optimal(nums, target)

    return simple_result, optimal_result


def simple(nums, target):
    """
    Time complexity: O(N^2)

    - Use of nested loops
    """
    indices = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                indices += [i, j]
    return indices

def optimal(nums, target):
    """
    Time complexity: O(N)

    - Using a hashmap (dictionary): O(1)
    - Iterating through list once: O(N)
    """
    indices_map = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in indices_map:
            return [indices_map[diff], index]

        indices_map[value] = index


if __name__ == "__main__":
    lst1 = [2,7,11,15]
    target1 = 9

    lst2 = [3,2,4]
    target2 = 6

    lst3 = [3,3]
    target3 = 6

    simple, optimal = main(lst2, target2)

    print("Simple:",simple)
    print("Optimal:",optimal)
