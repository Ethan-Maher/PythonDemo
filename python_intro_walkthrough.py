# -----------------------------------------------
# SECTION 1: VARIABLES - Storing and using values
# -----------------------------------------------

# name = "Oscar"
# age = 13
# height_in_cm = 160.5
# likes_pizza = True

# print("Name:", name)
# print("Age:", age)
# print("Height (cm):", height_in_cm)
# print("Likes pizza?", likes_pizza)


# -----------------------------------------------
# SECTION 2: INPUT - Getting info from the user
# -----------------------------------------------

# user_name = input("What's your name? ")
# print("Nice to meet you,", user_name)


# -----------------------------------------------
# SECTION 3: BASIC TYPES - int, float, str, bool
# -----------------------------------------------

# age = int(input("How old are you? "))
# gpa = float(input("What’s your GPA? "))
# is_student = True  # Just a simple True/False value

# print("Age:", age)
# print("GPA:", gpa)
# print("Student:", is_student)


# -----------------------------------------------
# SECTION 4: CONDITIONALS - If, else, elif
# -----------------------------------------------

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You're an adult.")
# elif age >= 13:
#     print("You're a teenager.")
# else:
#     print("You're a kid.")


# -----------------------------------------------
# SECTION 5: LOOPS - For loops
# -----------------------------------------------

# print("Counting from 1 to 10:")
# for i in range(1, 11):
#     print(i)


# -----------------------------------------------
# SECTION 6: LOOPS - While loops
# -----------------------------------------------

# counter = 0
# while counter < 5:
#     print("Looping:", counter)
#     counter += 1


# -----------------------------------------------
# SECTION 7: FUNCTIONS - Reusable code
# -----------------------------------------------

# def greet(name):
#     print("Hello", name + "!")

# greet("Alex")
# greet("Taylor")


# -----------------------------------------------
# SECTION 8: MINI PROJECT - Number guessing game
# -----------------------------------------------

# import random
# secret = random.randint(1, 10)
# guess = int(input("Guess a number between 1 and 10: "))
# if guess == secret:
#     print("You got it!")
# else:
#     print("Nope, it was", secret)


# -----------------------------------------------
# SECTION 9: LISTS - Storing multiple values
# -----------------------------------------------

# colors = ["red", "blue", "green"]
# print("First color:", colors[0])
# colors.append("yellow")
# print("All colors:", colors)


# -----------------------------------------------
# SECTION 10: LOOPS + LISTS
# -----------------------------------------------

# names = ["Oscar", "Bob", "Charlie"]
# for name in names:
#     print("Hi", name)


# -----------------------------------------------
# SECTION 11: CHALLENGE - FizzBuzz
# -----------------------------------------------

# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
