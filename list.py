#!/usr/local/bin/python3

_lst = [3,5,7,9,10.5]
_str = 'Python'

print (f'\nlist={_lst}\n')

_lst.append(_str)

print (f'len_of_list = {len(_lst)}\n')

print (f'first = {_lst[0]}\n')
print (f'last = {_lst[-1]}\n')
print (f'2..4 = {_lst[2:5]}\n')

_lst.remove(_str)

print (f'list = {_lst}\n')