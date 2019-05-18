#!/usr/local/bin/python3

_dict = {'city': 'Moscow', 'temp':'20'}

print(f'{_dict["city"]}')

t_int=int(_dict["temp"])
t_int-=5
_dict["temp"] = str(t_int)

print(f'dict = {_dict}')

if _dict.get("country",'Россия'):
    print('none country')

_dict["date"] = '27.05.2019'

print(f'dict = {_dict}')

print(f'len_dict = {len(_dict)}')