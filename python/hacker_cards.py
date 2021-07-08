#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Complete the 'hackerCards' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY collection --> Leanne's collection
#  2. INTEGER d --> Mike's budget
# Input: collection size, collection elements, last field is d which is Mike's budget
# hacker cards 1 to infinity. the cards correspond to the prices

### challenge done using for loop and while loop. both passed the 13 tests. 
### it was stated that function with "while" will pass tests and the function with "for" will not. 
### that was untrue.

def hackerCards(collection, d):
    # Write your code here
    # return array of integer cost of cards aka cards in asc 
    # collection = [4, 6, 12, 8] (leanne's collection)
    # d = 14 (mike's budget)
    # result should be 1, 2, 3, 5 = 11 
    # collect the ints not in the collection up to the sum d
    
    remaining_budget = d
    result = []
    collection_set = set(collection)
    
    for current_card in range(1, d + 1):
        if current_card not in collection_set and current_card <= remaining_budget:
            remaining_budget -= current_card
            result.append(current_card)
        elif current_card > remaining_budget:
            break
                
    return result


def hackerCards(collection, d):
    # Write your code here
    # return array of integer cost of cards aka cards in asc 
    # collection = [4, 6, 12, 8] (leanne's collection)
    # d = 14 (mike's budget)
    # result should be 1, 2, 3, 5 = 11 
    # collect the ints not in the collection up to the sum d
    
    remaining_budget = d
    result = []
    collection_set = set(collection)
    current_card = 1
    while True:
        if current_card not in collection_set and current_card <= remaining_budget:
            remaining_budget -= current_card
            result.append(current_card)
        elif current_card > remaining_budget:
            return result
        current_card += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    collection_count = int(input().strip())

    collection = []

    for _ in range(collection_count):
        collection_item = int(input().strip())
        collection.append(collection_item)

    d = int(input().strip())

    result = hackerCards(collection, d)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# if you want it shorter you can do:

# within_budget = current_card <= remaining_budget
# owned_by_leanne = current_card in collection_set
# if within_budget and not owned_by_leanne:
#    ...