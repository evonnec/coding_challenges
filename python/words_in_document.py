#!/usr/bin/env python3

# /**

# You are given a list of documents. Find all words that appear in every document.
# Here are two test cases. Each list is a list of very short documents.

# List("I am Groot", "Sam I am", "I do not like ham") gives: Set("I")
# List("I am Groot", "Sam I am") gives: Set("I", "am")

# */

# object MyApp extends App {

# val documents1 = Seq("I am Groot", "Sam I am", "I do not like ham") // test case 1
# val documents2 = Seq("I am Groot", "Sam I am") // test case 2
# val documents3 = Seq("I am I", "you and I") // test case 3

# def findCommonWords(documents: Seq[String]): Set[String] = {
# // your code here

# }
# println(findCommonWords(documents1))
# println(findCommonWords(documents2))
# println(findCommonWords(documents3))
# }

from typing import List, Set

test_case_1 = ["I am Groot", "Sam I am", "I do not like ham"]
test_case_2 = ["I am Groot", "Sam I am"]

def myapp(sentence_list: List[str]) -> Set[str]:
    setified_strings = []
    for i in sentence_list:
        temp_set = set(i.split())
        setified_strings.append(temp_set)

    track_set = set()

    for index, j in enumerate(setified_strings):
        if index == 0:
            temp_set = j
        else:
            track_set = j.intersection(temp_set)
            temp_set = track_set

    return track_set

print(myapp(test_case_1))
assert myapp(test_case_1) == {'I'}
print(myapp(test_case_2))
assert myapp(test_case_2) == {'I', 'am'}