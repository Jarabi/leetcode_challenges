#!/usr/bin/python3

def solution(points):
    """
    Minimum time to visit all points

    Return the minimum time in seconds to visit all the points in the order given by `points`.

    Args:
        points (list): List of integer arrays.
    """
    result = 0
    x1, y1 = points.pop()

    while points:
        x2, y2 = points.pop()
        result += max(abs(y2 - y1), abs(x2 - x1))
        x1, y1 = x2, y2
    return result


if __name__ == "__main__":
    pts = [[1,1],[3,4],[-1,0]]

    print(solution(pts))
