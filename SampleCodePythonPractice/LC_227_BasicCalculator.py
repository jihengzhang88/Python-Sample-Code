def calculate(s):
    pending_res = res = num = 0
    pending_op = "+"

    for char in s + "+":
        if char.isdigit():
            num = 10*num + int(char)

        elif char in {"+", "-", "*", "/"}:
            if pending_op == "+":
                pending_res += num
            elif pending_op == "_":
                pending_res -= num
            elif pending_op == "*":
                pending_res *= num
            else:
                pending_res = int(pending_res/num)

            if char in {"+", "-"}:
                res += pending_res
                pending_res = 0

            pending_op = char
            num = 0

    return res


if __name__ == "__main__":
    test1 = "3+2*2"
    print(calculate(test1))
    test2 = " 3/2 "
    print(calculate(test2))
    test3 = " 3+5 /2 "
    print(calculate(test3))
