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