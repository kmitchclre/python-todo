from random import randint
# age = input("How old are you?")
# age = int(age)

# if age >= 21:
#     print("you can drink")
# elif age == 20:
#     print("Come back in a year")
# else:
#     print("You're too young kid")


# first_name = input("What is your first name?")
# last_name = input("What is your last name?")
# char_length = len(first_name) + len(last_name)


# if char_length == 12:
#     print(f"{first_name} {last_name} is exactly the average")
# elif char_length < 12:
#     print(f"{first_name} {last_name} is shorter than the average")
# else:
#     print("Longer than average")


# total_length = 140;
# tweet = input("enter your tweet:")
# length = len(tweet)

# if length < total_length:
#     print(f"That {length} char tweet will work!")
# elif length > 140:
#     print(f"Your {length} char tweet is {length - total_length} too long.")

# height = int(input("enter your height in inches"))
# weight = int(input("enter your weight in lbs:"))
# bmi = (weight * 703) / (height * height)
# bmi = round(bmi, 1)

# if bmi < 16.0:
#     print(f"Your {bmi} makes you Severely Underweight")
# elif bmi >= 16.0 and bmi <= 18.4:
#     print(f"Your {bmi} makes you Underweight")
# elif bmi >= 18.5 and bmi <= 24.9:
#     print(f"Your {bmi} makes you Severely Normal")
# elif bmi >= 25.0 and bmi <= 29.9:
#     print(f"Your {bmi} makes you Overweight")
# elif bmi >= 30.00 and bmi <= 34.9:
#     print(f"Your {bmi} makes you Moderately Obese")
# elif bmi >= 35.0 and bmi <= 39.9:
#     print(f"Your {bmi} makes you Severely Obese") 
# else:
#     print(f"Your {bmi} makes you Morbidly Obese")


# age = int(input("What is your age?"))

# if age < 5 or age > 65:
#     print("You get in for free")
# else:
#     print("you gotta pay")

# answer = input("Please say hi")

# while answer != "hi":
#     answer = input("Rude. Say hi...")

# print("Helllo :)")





# first_dice = random.randint(1,6)
# second_dice = random.randint(1,6)


# while first_dice != 1 or second_dice != 1:
#     first_dice = random.randint(1,6)
#     second_dice = random.randint(1,6)
#     print("Keep rollin")

# print(f"Finally reached {first_dice} and {second_dice} ")


# for num in range(10,1,-1):
#     print(num)


# for num in range(99,0,-1):
#     print(f"{num} bottles of beer on the wall")
#     print(f"{num} bottles of beer.")
#     if num == 1:
#         print("Take one down, pass it around, no more bottles of beer on the wall")
#     else:
#         print(f"Take one down, pass it around, {num - 1} bottles of beer on the wall")
#     print("*********************")





# def reverse(nums):

#     start_index = 0

#     end_index = len(nums)-1

#     while end_index > start_index:
#         nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
#         start_index = start_index + 1
#         end_index = end_index - 1



# n = [1,2,3,4]
# reverse(n)
# print(n)



# def is_palindrome(str):
#     original_str = str
#     reversed_str = str

#     if original_str == reversed_str:
#         return True
#     return False




# def pallindrome_python(s):
#     if s == s[::-1]:
#         return True
        
#     return False

# print(pallindrome_python('madam'))






# def reversed_integer(n):
#         reversed = 0
#         remainder = 0

#         while n > 0:
#             remainder = n % 10
#             reversed = reversed*10 + remainder
#             n = n //10
#         return reversed


# if __name__ == '__main__':
#     print(reversed_integer(1234 ))



# dice = int(input("How many dice are we rolling? "))
# sides = int(input("how many sides on the die?"))

# while True:
#     result = "|"
#     for die in range(dice):
#         rand = (randint(1, sides))
#         result += f"{rand}"
#     print(result)
#     reply = input("Roll again? type q to quit: ")
#     if reply == "q":
#         break




# print("Welcome To The Game!")
# print("********************")
# num_left = 13
# player1_name = input("Enter player 1's name: ")
# player2_name = input("Enter player 2's name: ")

# while True:
#     print("| " * num_left)
#     print(f"There are {num_left} toothpicks left")
#     p1_choice = int(input(f"{player1_name}, how many toothpicks do you take? "))
#     num_left -= p1_choice
#     if num_left <= 0:
#         print(f"{player1_name} wins the game!")
#         break

#     print("| " * num_left)
#     print(f"There are {num_left} toothpicks left")
#     p2_choice = int(input(f"{player2_name}, how many toothpicks do you take? "))
#     num_left -= p2_choice
#     if num_left <= 0:
#         print(f"{player2_name} wins the game!")
#         break

# print("GAME OVER!")


# def isEven(num):
#     if num % 2 == 0:
#         return True
#     elif num % 2 == 1:
#         return False

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     return False



# def slugify(string):
#     return string.lower().strip().replace(' ', '-')



# def count_vowel(word):
#     count = 0
#     for char in word:
#         if char in "aeiou":
#             count += 1
#     return count

# print(count_vowel("Hello world"))

header = "TO DO LIST"



print(header)

todos = []
while True:
    for todo in range(len(todos)):
        print(f"{todo + 1}) {todos[todo]}")
    print("**********************")
    print("Enter a command. Type 'h' for help: ")
    command = input(' ')

    if command == 'q':
        print("Today you completed 5 todos: ")
        for todo in todos:
            print(f"* {todo}")
        break
    
    elif command.isnumeric():
        idx = int(command)
        todos.pop(idx-1)

    elif command == 'h':
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("To add a todo to the list, type it and hit enter")
        print("To complete a todo enter its number")

    else:
        todos.append(command)

    


