#!/usr/bin/python3
"""module contains function that returns a list of integers."""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's
    triangle of n."""
    if n <= 0:
        return []
    r = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(r[i-1][j-1] + r[i-1][j])
        row.append(1)
        r.append(row)
    return r
