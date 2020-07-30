# -*- coding: utf-8 -*-
"""
Programming Management

- Introduction to Assertions
- Fixing and debugging some code examples.
"""

# ASSERTIONS - a way to do DEFENSIVE PROGRAMMING

numbers = [1.5, 2.3, 0.7, -0.001, 4.4]

total = 0.0
for num in numbers:
    assert num > 0.0, 'Data should only contain positive values'
    total += num
print('total is', total)



# example of an assertion in a function
def calc_bulk_density(mass, volume):
    '''Return dry bulk density = poweder mass / powder volume.'''
    assert volume > 0, 'Problem with volume data'
    assert mass > 0, 'Problem with mass data'
    return mass / volume



calc_bulk_density(210, 0)






## HELP ME WITH THIS CODE:
    
def sort_for_middle(a,b,c):
    '''Return the middle value of three
     Assumes that the values can actually be compared
     Usage: sort_for_middle(a,b,c).  input three values
     '''
    values = [a,b,c]
    values.sort()
    return values[0]

help(sort_for_middle)

sort_for_middle(4,3,2)






### CLEAN UP THIS CODE.

# Read this program and try to predict what it does
# Run it: how accurate was your prediction?
# Refactor the program to make it more readable.

n = 10
s = 'et cetera et cetera'
print(s)

i = 0
while i < n :
    #print('at', j)
    new = ''
    for j in range(len(s)):
        left = j-1
        right = (j+1)%len(s)
        if s[left]==s[right]: 
            new += "-"
        else: 
            new += "*"
    s=''.join(new)
    print(s)
    i += 1  # shortcut  i = i + 1





















