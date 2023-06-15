def fact(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n+1):
        # fact = fact*i
        fact *= i
    return fact

def main():
    n = int(input('calculate factorial of:'))
    print(fact(n))

if __name__ == '__main__':
    main()