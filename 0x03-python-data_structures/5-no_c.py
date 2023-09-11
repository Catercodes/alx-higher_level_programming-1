#!/usr/bin/env python3
def no_c(my_string):
    new_list = ""
    for i in my_string:
         if i != 'c' and i != 'C':
             my_string.append(i)
    return ''.join(new_list[i])
