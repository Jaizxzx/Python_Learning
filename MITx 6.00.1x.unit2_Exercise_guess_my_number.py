low = 0
high = 100
print("Please think of a number between 0 and 100!")
while True:
    guess = (low + high) // 2
    print("Is your secret number " + str(guess) + "?")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if x == "h":
        high = guess
    elif x == "l":
        low = guess
    elif x == "c":
        print("Game over. Your secret number was: ", guess)
        break
    else:
        print("Sorry, I did not understand your input")