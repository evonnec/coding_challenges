#!/usr/bin/env python3

numbers_to_letters = {
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p','q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': []
}

letter_dictionary = set(['BAD', 'ACE', 'CAD'])

#dial pad
#dictionary with English words
#write a function, given a series of numbers -> return all valid words that can be created
#input 223 -> 'BAD' or 'ACE' or 'CAD' but not 'BCD' b/c it's not valid

def make_word(input_num):
    if not input_num:
        raise ValueError('Invalid Input')
    valid_word = []
    
    def take_num(i, word_so_far):
        if len(input_num) == i:
            if word_so_far in letter_dictionary:
                print(word_so_far)
        else:
            dial_num = numbers_to_letters.get(input_num[i])

            for j in dial_num:
                word_so_far = word_so_far + j
                print(word_so_far)
                take_num(i + 1, word_so_far)
                # word_so_far.pop()
                word_so_far[:-1]

    take_num(0, '')
    # if take_num(0, '') in letter_dictionary:
    #     valid_word.append(take_num(0, ''))
    return valid_word