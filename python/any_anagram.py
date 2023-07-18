#!/usr/bin/env python3

#  /*
#    * Given a list of words, group them into anagrams and output one word from each of the anagram groups 
# that contains at least 2 words.
#    * Any of the words in the group can be used (not necessarily the first word) and the order of the output does not matter.
#    * For example:
#    *   given ["tsar", "rat", "tar", "star", "tars", "cheese", "cat"]
#    *   output might be ["tsar", "tar"]
#    */

from collections import defaultdict
from typing import List

words = ["tsar", "rat", "tar", "star", "tars", "cheese", "cat"]

def make_anagram(word_list: List[str]) -> List[str]:
    visited_words = defaultdict(list)

    for i in word_list:
        char_list = sorted([char for char in i])
        word_key = "".join(char_list)
        visited_words[word_key].append(i)
    
    count_more_than_one = [visited_words[key][0] for key in visited_words if len(visited_words[key]) > 1]

    return count_more_than_one

print(make_anagram(words))
assert make_anagram(words) == ["tsar", "rat"]