# '''two sum'''
# # n1 = 1
# # n2 = 2
#
# def two_sum(n1, n2):
#     return n1 + n2
#
#
# def main(): n1 = float( input('first number:'))  # ctrl+D copy current line, default input is string,
# need to define it as float or int n2 = float(input('second number:')) print('n1 + n2 =', two_sum(n1, n2))
#
#
# if __name__ == "__main__":
#     main()


# def twoSum(nums, target):
#     res = []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#              if nums[i] + nums[j] == target:
#                 res.append(i)
#                 res.append(j)
#     return res

def two_sum_dict(nums, target):
    dict = {}
    for index, value in enumerate(nums):
        if value in dict:
            return [dict[value], index]
        else:
            dict[target - value] = index


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_dict(nums, target))


if __name__ == '__main__':
    main()
