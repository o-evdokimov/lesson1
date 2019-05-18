#!/usr/local/bin/python3

import sys
import unicodedata

v=''

#while (v<1 or v>10):
v=input('Введите число от 1 до 10:')

if v.isdigit() is False: sys.exit(0)
if (int(v)<1 or int(v)>10): 
    print('неверный диапазон 1..10')
    sys.exit(0)    
else: 
    v2 = int(v)   
    v2+=10

print(f'v={v2}')
