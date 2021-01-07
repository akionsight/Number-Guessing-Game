import random
num = random.randint(1,20)

def play(num):
    guess = int(input("enter guess:- "))
    if guess == num:
        print("correct guess 😀😀")
        break
    if guess < num:
        print("too low, guess higher")
    if guess > num:
        print("too high, guess lower")

while True:
    play(num)
