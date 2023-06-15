def rm_list(li, rm):
    # use remove function
    licopy = li
    for i in licopy:
        if i in rm:
            licopy.remove(i)

    return licopy


def pop_list(li, rm):
    # use pop function
    licopy = li
    for i in licopy:
        if i in rm:
            licopy.pop(licopy.index(i))
    return li


def main():
    li = [3,5,7,9,11,13]
    rm = [7,11]
    print('using remove function, the output is', rm_list(li, rm))
    print('using pop function, the output is', pop_list(li.copy(), rm))


if __name__ == "__main__":
    main()