import random

print("Welcome!!!")
title = input("Type you Title you give it to urself\n")
name = input("What is your Name?\n")
num = random.randrange(1, 999)
username = (title+name+str(num))
print(username)
