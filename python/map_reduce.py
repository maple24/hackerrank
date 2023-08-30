import functools


# Python program to  illustrate sum of two numbers.
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
 
# Note that the initializer, when not None, is used as the first value instead of the first value from iterable , and after the whole iterable.
tup = (2,1,0,2,2,0,0,2)
print(reduce(lambda x, y: x+y, tup,6))


# initializing list
lis = [1, 3, 5, 6, 2]
 
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))


def multiplyNumbers(givenNumbers):
   return givenNumbers*3

givenNumbers = map(multiplyNumbers, [1, 3, 5, 2, 6, 10])
print(list(givenNumbers))

def getNumbers(givenNumbers):
    if givenNumbers > 5:
        return givenNumbers

givenNumbers = filter(getNumbers, [1, 3, 5, 2, 6, 10])
print(list(givenNumbers))

# function that returns the sum of all list items
def addNumbers(x, y):
    print(x, y)
    return x+y
# input list
inputList = [12]
# Print the sum of the list items using reduce() function
print("The sum of all list items:")
print(reduce(addNumbers, inputList))