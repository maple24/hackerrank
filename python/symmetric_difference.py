'''
The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
'''

a = "1 2 3 4 5 6 7 8 9"
b = "10 1 2 3 11 21 55 6 8"
a = set(a.split())
b = set(b.split())
print(a.symmetric_difference(b))