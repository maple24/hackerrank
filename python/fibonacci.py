cube = lambda x: x ** 3

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_se = [0, 1]
    if n ==0 :
        return []
    elif n == 1:
        return [0]
    else:
        while len(fib_se) < n:
            fib_se.append(fib_se[-1] + fib_se[-2])
        return fib_se

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))