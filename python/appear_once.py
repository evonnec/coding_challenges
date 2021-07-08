#!/usr/bin/env python3

# /* Given a list of integers, return a list of integers that only appear once in the list
#   Example:
#   List: [4, 6, 7, 6, 8, 10, 11, 1, 2, 4, 4, 4]
#   Solution: [7, 8, 10, 11, 1, 2]
#  */

from collections import defaultdict

# O(n)
# take each element compare against the list. 
def appear_once_list(list_of_ints: list) -> list:
    visited = defaultdict(int)
    count_is_one = []

    for i in list_of_ints:
        visited[i] += 1

    count_is_one = [j[0] for j in visited.items() if j[1] == 1]
    return count_is_one

print(appear_once_list([3, 4, 4, 6, 2, 2, 2]))
assert appear_once_list([3, 4, 4, 6, 2, 2, 2]) == [3, 6]
print(appear_once_list([4, 6, 7, 6, 8, 10, 11, 1, 2, 4, 4, 4]))
assert appear_once_list([4, 6, 7, 6, 8, 10, 11, 1, 2, 4, 4, 4]) == [7, 8, 10, 11, 1, 2]

