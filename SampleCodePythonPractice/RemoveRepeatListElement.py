# def rm_list(li, rm):
#     # use remove function
#     licopy = li
#     for item in licopy:
#         if item in rm:
#             licopy.remove(item)
#
#     return licopy
#
#
# def pop_list(li, rm):
#     # use pop function
#     licopy = li
#     for item in licopy:
#         if item in rm:
#             licopy.pop(licopy.index(item))
#     return li
#
#
# def main():
#     li = [3,5,7,9,11,13]
#     rm = [7,11]
#     print('using remove function, the output is', rm_list(li, rm))
#     print('using pop function, the output is', pop_list(li.copy(), rm))
#
#
# if __name__ == "__main__":
#     main()


def setlist(li):
    licopy = li
    return list(set(licopy))


def forloop(li):
    uli = []
    for i in li:
        if i not in uli:
            uli.append(i)
    return uli


def main():
    li = [10, 20, 30, 10, 30, 10]
    print('use set function result is ', setlist(li))
    print('use forloop function result is ', forloop(li))


if __name__ == "__main__":
    main()
