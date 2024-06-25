import math

User_name = input(f"Welcome to GC Mini Golf! What is your name? ")
print(f"Hi, {User_name}! ")

number_holes = input("Would you like to play 3 holes or 6 holes today? ")
if number_holes == "3":
    score_one = int(input("How many putts for hole 1 (par is 3)? "))
    tso = score_one - 3
    score_two = int(input("How many putts for hole 2 (par is 3)? "))
    tst = score_two - 3
    score_three = int(input("How many putts for hole 3 (par is 3)? "))
    tsh = score_three - 3
    calc_par = tso + tst + tsh
    if calc_par < 0:
        print(f"Great job, {User_name}! Your total par was: {calc_par}")
    elif calc_par == 0:
        print(f"Good game, {User_name}. Your total par was: 0")
    elif calc_par > 0:
        print(f"Nice try, {User_name}... Your total par was: +{calc_par}")


if number_holes == "6":
    sso = int(input("How many putts for hole 1 (par is 3)? "))
    stso = sso - 3
    sst = int(input("How many putts for hole 2 (par is 3)? "))
    stst = sst - 3
    ssth = int(input("How many putts for hole 3 (par is 3)? "))
    stsh = ssth - 3
    ssf = int(input("How many putts for hole 4 (par is 3)? "))
    stsf = ssf - 3
    ssv = int(input("How many putts for hole 5 (par is 3)? "))
    stsv = ssv - 3
    ssx = int(input("How many putts for hole 6 (par is 3)? "))
    stsx = ssx - 3
    calc_par = stso + stst + stsh + stsf + stsv + stsx
    if calc_par < 0:
        print(f"Great job, {User_name}! Your total par was: {calc_par}")
    elif calc_par == 0:
        print(f"Good game, {User_name}. Your total par was: 0")
    elif calc_par > 0:
        print(f"Nice try, {User_name}... Your total par was: +{calc_par}")

else:
    print(f"Sorry {User_name}, {number_holes} is not a valid choice.")

