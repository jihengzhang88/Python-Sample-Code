'''two sum'''
# n1 = 1
# n2 = 2

def two_sum(n1, n2):
    return n1 + n2


def main():
    n1 = float(
        input('first number:'))  # ctrl+D copy current line, default input is string, need to define it as float or int
    n2 = float(input('second number:'))
    print('n1 + n2 =', two_sum(n1, n2))


if __name__ == "__main__":
    main()
