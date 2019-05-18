#!/usr/local/bin/python3

def get_sum(one, two, delimeter= '&'):
    return '{}{}{}'.format(str(one),delimeter,str(two))

    
lp = get_sum('Learn','python', delimeter='+').upper()

print (lp)