#!/usr/bin/python3

def solution(matrix):
    """
    Spiral Matrix

    Given an `m x n` matrix, return all elements of the `matrix` in spiral order.

    Args:
        matrix (list): A 2D list.

    Complexity: O(N)
    """
    result = []

    while matrix:
        # 1. Get the first row of matrix
        result += matrix.pop(0)

        # 2. Get the last item of all rows in order
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        # 3. Add reverse of the last row
        if matrix:
            result += matrix.pop()[::-1]

        # 4. Append the first element of all rows in reverse
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop())
    return result


if __name__ == "__main__":
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    m2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    print(solution(m2))
