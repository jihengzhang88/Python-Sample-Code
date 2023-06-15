def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def forloop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def main():
    n = int(input('calculate fibonacci number:'))
    print('using recursive function, the result is', fib(n))
    print('using forloop function, the result is', forloop(n))

if __name__ == '__main__':
    main()