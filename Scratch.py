import math

User_name = input(f"Welcome to GC Mini Golf! What is your name? ")
print(f"Hi, {User_name}! ")

number_holes = input("Would you like to play 3 holes or 6 holes today? ")
if number_holes == "3":
    hole_list = ["hole 1", "hole 2", "hole 3"]

    current_hole = 1
    for x in hole_list:
        while current_hole <= 4:
            score = int(input("How many putts for hole " + str(current_hole) + str('(par is 3)? ')))
            current_hole += 1
            if current_hole == 4:
                print(f"Good game {User_name}! Your total score was: ")
            break

if number_holes == "6":
    hole_list = ["hole 1", "hole 2", "hole 3", "hole 4", "hole 5", "hole 6"]

    current_hole = 1
    for x in hole_list:
        while current_hole <= 7:
            score = int(input("How many putts for hole " + str(current_hole) + str('(par is 3)? ')))
            current_hole += 1
            if current_hole == 7:
                print(f"Good game {User_name}! Your total score was: ")
            break