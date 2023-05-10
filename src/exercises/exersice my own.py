message = 'hello python world'
print(message)

message = 'hello pyhton carsh coure world'
print(message)

name= "ada lovelace"
print(name.title())

name= "ada lovelace"
print(name.upper())
name="ada lovelace"
print(name.lower())

first_name = "ada"
last_name = 'lovelace'
full_name = first_name + " " + last_name
message = ("hello", full_name.title() + "!")
print(message)

print(f"python")

print("\tpython")

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

print(5+3)
print(2*4)

bikes = ['trek', 'redline', 'giant']
print(bikes)

first_bike = bikes[0]
print(first_bike)

bikes = bikes[1]
print(bikes)

square = []
for x in range(1, 11):
    square.append(x**2)
    print(square)


square = []
for x in range(2, 7):
    square.append(x**2)
    print(square)

square = [x**2 for x in range(1, 11)]
print(square)

square = [x*2 for x in range(1, 5)]
print(square)

runners = ['sam', 'bob', 'ada', 'bea']
first_two = runners[:2]
print(first_two)

last_three = runners[3:]
print(last_three)

copy_of_runners = runners
print(copy_of_runners)

copy_of_bikes = bikes[:]
print(copy_of_bikes)

dimensions = (1920, 1080)
print(dimensions)

if age >= 18:
    print("You can vote!")

if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15
    print(age)

alien = {'color': 'green', 'points': 5}
print("The allen's color is " + alien['color'])

alien['x_position'] = 0
print(alien)

fav_numbers = {eric}





# value = 1
# while value <= 9:
#     print(value)
#     value += 2
#
# # msg = ''
# # while msg != 'quit':
# #     msg = input(f"what's your message? ")
# #     print(msg)
#
#
# # msg = ''
# # while msg != 'take':
# #     msg = input(f"take what?")
# #     print(msg)
#
#
# value = 1
# while value <= 9:
#     print(value)
#     value += 1
#
# def greet_user():
#     """Display a simple greeting"""
#     print("Hello!")
#
# greet_user()
#
# def greet_user():
#     """Display angry greeting"""
#     print("insert the reality")
#
# greet_user()
#
# def greet_user(username):
#     """Display personalized greeting"""
#     print("hello, " + username + "!")
# greet_user('Jesse')
#
# def make_pizza(topping ='turkey bacon'):
#     """Make a single topping pizza."""
#     print("have a " + topping + " pizza!")
# make_pizza()
# make_pizza('pepperoni')
#
# def adding_numbers(x, y):
#     """Multiply two numbers and return the sum"""
#     return x * y
#
# sum = adding_numbers(3, 5)
# print(sum)
#
#
# def subtract_numbers(x, y):
#     return x / y
# sum = subtract_numbers(15, 3)
# print(sum)
#
# def minus_numbers(x, y):
#     return x - y
# sum = minus_numbers(17, 3)
# print(sum)
#
# user = ['val', 'bob', 'mia', 'ron', 'ned']
# first_user = user[0]
# print(first_user)
#
# second_user = user[1]
# print(second_user)
#
# newest_user = user[-1]
# print(newest_user)
#
# user[0] = 'valerie'
# user[-2] = 'ronald'
#
# first_user = user[0]
# print(first_user)
#
# middle_user = user[3]
# print(middle_user)
#
#
#
#
