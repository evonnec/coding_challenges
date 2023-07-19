# Python program to find minimum difference between any pair in an unsorted array   
# Returns minimum difference between any pair


class Solution:
    def minimumAbsDifference(arr: List[int]) -> int):
        prev, diff = -1, 10**9
        for a in arr:
            if prev != -1:
                diff = min(diff, abs(a - prev))
            prev = a
        return diff

 
    def findMinDiff(arr):     
        # Sort array in non-decreasing order 
        arr = sorted(arr) 
    
        # Initialize difference as upper bound 
        diff = 10**20
    
        # Find the min diff by comparing adjacent 
        # pairs in sorted array 
        for i in range(len(arr) - 1): 
            if arr[ i + 1 ] - arr[i] < diff: 
                diff = arr[i + 1] - arr[i] 
    
        # Return min diff 
        return diff 
        
"""
Write a function:

def solution(S)

that, given a string S, returns the index (counting from 0) of a character such 
that the part of the string to the left of that character is a reversal of the part 
of the string to its right. The function should return −1 if no such index exists.
Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.

For example, given a string:

"racecar"

the function should return 3, because the substring to the left of the character "e" 
at index 3 is "rac", and the one to the right is "car".

Given a string:

"x"

the function should return 0, because both substrings are empty.

Write an efficient algorithm for the following assumptions:

the length of string S is within the range [0..2,000,000].
"""

def solution1(S: str) -> int:
    if len(S) % 2 == 0:
        return -1
        
    s_in_order = [item for item in S]
    reversed_s = [item for item in reversed(S)]

    if s_in_order == reversed_s:
        return (len(s_in_order) - 1) // 2
    else:
        return -1
    
"""
https://app.codility.com/demo/results/trainingPZHNZK-2AF/
O(length(S)) time complexity
Analysis summary
The solution obtained perfect score.
100% test coverage
"""

"""
Next Task:
Task description
A non-empty array A consisting of N integers is given. The unique number is the 
number that occurs exactly once in array A.

For example, the following array A:

  A[0] = 4
  A[1] = 10
  A[2] = 5
  A[3] = 4
  A[4] = 2
  A[5] = 10
contains two unique numbers (5 and 2).

You should find the first unique number in A. In other words, find the unique 
number with the lowest position in A.

For above example, 5 is in second position (because A[2] = 5) and 2 is in 
fourth position (because A[4] = 2). So, the first unique number is 5.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the first unique 
number in A. The function should return −1 if there are no unique numbers in A.

For example, given:

  A[0] = 1
  A[1] = 4
  A[2] = 3
  A[3] = 3
  A[4] = 1
  A[5] = 2
the function should return 4. There are two unique numbers (4 and 2 occur exactly once). 
The first one is 4 in position 1 and the second one is 2 in position 5. 
The function should return 4 bacause it is unique number with the lowest position.

Given array A such that:

  A[0] = 6
  A[1] = 4
  A[2] = 4
  A[3] = 6
the function should return −1. There is no unique number in A (4 and 6 occur more than once).

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000
"""

from typing import List
from collections import Counter

def solution2(A: List[int]) -> int:
    a_counter = Counter()
    for i in A:
        a_counter[i] += 1

    test = set(k for k, v in a_counter.items() if v == 1)
    
    if not test:
        return - 1

    for i in A:
        if i in test:
            return i
        
"""
https://app.codility.com/demo/results/trainingX7WJF3-KF5/
Detected time complexity:
O(N * log(N))
Analysis summary
The solution obtained perfect score.
100% test coverage: Task Score, Correctness, Performance
"""

"""
Mext Task:
Task description
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive 
integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

from typing import List

def solution3(A: List[int]) -> int:
    result = 1
    set_A = set(A)
    while True:
        if result not in set_A:
            return result
        result += 1
        
"""
https://app.codility.com/demo/results/trainingZ7P6RF-RAB/
Analysis summary
The solution obtained perfect score.
Analysis
Detected time complexity:
O(N) or O(N * log(N))
100% test coverage: Task Score, Correctness, Performance
"""
    