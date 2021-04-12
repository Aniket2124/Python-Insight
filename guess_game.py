'''
from random import randint
# randint(a,b)= a<=n,=b
randval = randint(0, 100)
while(True):
    guess = int(input("please enter your Guess: "))
    if guess == randval:
        break
    elif guess <= randval:
        print("Your guess was too low ")
    else:
        print("Too High")
print(" You guess correctly with: ", guess)
'''
from random import random


randval = random()
print(randval)

upper = 1.0
lower = 0.0
guess = 0.5


while(True):
    # guess = (upper + lower)/2
    if guess == randval:
        break
    elif guess < randval:
        lower = guess
    else:
        upper = guess
    guess = (upper + lower)/2


print(guess)
