secret=34
lives=5

while lives>0:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess == secret:
        print("Congratulations! You've guessed the correct number.")
        break
    else:
        lives = lives - 1

        if guess > secret:
            diff= guess - secret
        else:
            diff= secret - guess
        
        if diff <= 3:
            print("You are very hot")
        elif diff >= 10:
            print("You are cold")
        elif diff <= 20:
            print("You are warm" )
        elif diff >=20:
            print("You are very hot")
        elif diff >=10:
            print("You are warm")
        elif diff >=5:
            print("You are warm")
        elif diff >=30:
            print("You are very hot")
        else:
            print("........")
for i in range(lives):
    print("You have", lives, "lives left.")
if lives == 0:
    print("Game over! You've run out of lives. The secret number was", secret)


    
