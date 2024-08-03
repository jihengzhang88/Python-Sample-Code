# weight = float(input("Weight: "))
# unit = input("(K)g or (L)bs: ")
#
# if unit.upper() == "K":  # unit == "K" or unit == "k":
#     converted = weight / 0.45
#     print("Weight in lbs: " + str(converted))
# else:
#     converted = weight * 0.45
#     print(f"Weight in kg: {converted}")
#
# # numbers = [1, 2, 3, 4, 5]
# # numbers.insert()

# while True:
#     customer_input = input("> ").lower()
#     if customer_input == 'help':
#         print('''start - to start the car
# stop - to stop the car
# quit - to exit''')
#     elif customer_input == 'start':
#         print('Car started...Ready to go!')
#     elif customer_input == 'stop':
#         print('Car stopped.')
#     elif customer_input == 'quit':
#         break
#     else:
#         print("I don't understand that...")

# numbers = [5, 2, 5, 2, 2]
# for item in numbers:
#         print('X' * item)

# numbers = [5, 2, 5, 2, 2]
# # for item in numbers:
# #         print('X' * item)
#
# for item in numbers:
#     output = ""
#     for i in range(item):
#         output += "X"
#     print(output)

# number_translate = {
#         "1": "One",
#         "2": "Two",
#         "3": "Three",
#         "4": "Four",
#         "5": "Five",
#         "6": "Six",
#         "7": "Seven",
#         "8": "Eight",
#         "9": "Nine",
#         "0": "Zero"
#     }
#
# phone = input("Phone: ")
# output = ""
#
# for phone_number in phone:
#     output += number_translate.get(phone_number, "!") + " "
#
# print(output)

# class Point: #(class define new type, use pascal name convention and cap every letter vs. variables use all lower
# case and _) def __init__(self, x, y): # use constructors to initialize the class self.x = x self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# # point1 = Point() # create object as the instance of class
# # point1.x = 10 # create attributes to the object
# # point1.y = 20
# # print(point1.x)
# # point1.draw()
#
#
# point2 = Point(10, 20)
# print(point2.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi this is {self.name} talking")
#
#
# john = Person("john smith")
# john.talk()


# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):  # Dog inherited from Mammal
#     def bark(self):
#         print("bark")
#
#
# class Cat(Mammal):
#     pass  # if we have not extra def in class Dog, use pass statement cause python don't like empty class
#
#
# dog1 = Dog()
# dog1.bark()


# """
# use module to better organize your code, in the module, define your functions. when you need the functions, there are 2 ways to use them
#
# import module_name              #when use this, you have all the functions in the module
# module_name.function_name()     #this is how you use it
#
# from module_name import function_name   #when use this, you only have the functions you listed
# function_name()                         #this is how you use it
# """
# from util import find_max
# numbers = [10, 3, 6, 2]
# print(find_max(numbers))


# import ecommerce.shipping
# ecommerce.shipping.calc_tax()
# ecommerce.shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping, calc_tax
# calc_shipping()
# calc_tax()

# from ecommerce.shipping import calc_shipping
# calc_shipping()

