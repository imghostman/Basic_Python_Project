import random as r

num = r.randrange(100)
guess = 5
while guess >= 0:
    your_guess = int(input("enter your guess: "))


    def check(x):
        if your_guess == x:
            print("you win")

        elif your_guess > x:
            print("You are very close,Keep trying lower")

        else:
            print("You are very close,Keep trying higher")
    if guess > 1:
        check(num)
    elif guess == 1:
        check(num)
        print('This is your last chance, Make the most of it')
    else:
        print("You lost")
    guess -= 1
