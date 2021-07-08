#!/usr/bin/env python3

# reverse a number

def reverse_num(num):
    list_num = [char for char in str(num)]
    reverse_num = []
    for _ in range(0, len(list_num)):
        reverse_num.append(list_num.pop())
    new_num = "".join(reverse_num)
    return int(new_num)

print(reverse_num(1234))

assert reverse_num(1234) == 4321

def reverse_num_recurse(num):
    list_num = [char for char in str(num)]
    reverse_num = []
    def _recurse_num(num_list):
        if not num_list:
            return
        else:
            reverse_num.append(num_list.pop())
            _recurse_num(num_list)
    _recurse_num(list_num)
    new_num = "".join(reverse_num)
    return int(new_num)

print(reverse_num_recurse(1234))

assert reverse_num_recurse(1234) == 4321