def all_even():
    n = 0
    while True:
        yield n
        n += 2
res = all_even()
print(next(res))
print(next(res))
print(next(res))
print(next(res))

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

res = PowTwoGen(3)
print(next(res))
print(next(res))
print(next(res))