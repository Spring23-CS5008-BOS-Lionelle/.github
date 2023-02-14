"""
Example file solving the pascal triangle using python.
Author: Albert Lionelle
Semester: Spring 2023
"""
from enum import Enum
from typing import List
from functools import lru_cache


class PascalType(Enum):
    DP = 2
    RECURSIVE = 1
    ITERATIVE = 0


@lru_cache(maxsize=None)
def pascal_dp(n: int, i: int) -> int:
    """
    Solves the pascal triangle using simple recrusion and built
    in memoization
    Args:
        n: the nth row
        i: the item in the row

    Returns:
        the addition of n-1, i + n-1, i-1
    """
    if n == i or i == 0:
        return 1
    return pascal_dp(n - 1, i) + pascal_dp(n - 1, i - 1)


def pascal_r(n: int, i: int) -> int:
    """
    Solves the pascal triangle using simple recursion
    Args:
        n: the nth row
        i: the item in the row

    Returns:
        the addition of n-1, i + n-1, i-1
    """
    if n == i or i == 0:
        return 1
    return pascal_r(n - 1, i) + pascal_r(n - 1, i - 1)


def scalar(coef: int, i: int, j: int) -> int:
    """
    calculates the scalar for the iterative version of pascals triangle
    Args:
        coef: the coef that is slowly increasing
        i: the ith location (row)
        j: the jth location (column)

    Returns:
        the coef of the binomial at that i/j location
    """
    if i == 0 or j == 0:
        return 1
    return int(coef * (i-j+1) / j)


def get_pascal_triangle(n: int, print_it: bool = False, version: PascalType = PascalType.RECURSIVE) -> List[int]:
    """
    Generates the nth row in the pascal triangle based on the
    method requested

    Args:
        n: the row to generate
        print_it:  print out all rows as being generated
        version:  the type/method of generation

    Returns:
        the nth row of the pascal triangle
    """
    row: list = []
    coef: int = 0
    for i in range(0, n):
        for j in range(0, i+1):
            if version == PascalType.RECURSIVE:
                tmp = pascal_r(i, j)
            elif version == PascalType.ITERATIVE:
                coef = scalar(coef, i, j)
                tmp = coef
            elif version == PascalType.DP:
                tmp = pascal_dp(i, j)
            if print_it:
                print(tmp, end=' ')
            if i+1 == n:
                row.append(tmp)
        if print_it:
            print()
    return row


def main():
    print(get_pascal_triangle(3000, False, PascalType.DP)[-2])


if __name__ == "__main__":
    main()

