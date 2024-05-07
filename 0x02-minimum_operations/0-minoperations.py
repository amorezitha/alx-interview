#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    minimumOperations = 2
    totalOperations = 0
    while n > 1:
        while n % minimumOperations == 0:
            totalOperations += minimumOperations
            n /= minimumOperations
        minimumOperations += 1
    return totalOperations

