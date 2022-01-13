"""Enumerate function:returns item and its index"""
a = (1, 2, 3, 33, 45, 67, 78, 6.5)
for position, item_name in enumerate(a):
    print(position, ':', item_name)
for i in enumerate(a):
    print(i)
"""asci - """
from string import ascii_letters
for i in ascii_letters:
    print(i, ord(i), chr(ord(i)))
