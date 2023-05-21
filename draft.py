name=input("Hey there!Enter your name:")
print(f"Vanakkam {name} ,lets begin the game!")
word="Scarlet"
chances=10
guesses=""#characters users have guessed so far


while chances>0:
    won=True
    for i in word:
        if i in guesses:
            print(i,end=" ")
        else:
            won=False
            print("_",end=" ")
    if won:
        print(f"\nYay {name} you've won!")
        break 
#take input guess from the user
guess=input("\nEnter a character: ")
guesses+=guess

if guess not in word:
    chances=chances-1
    print("\nYour guess is wrong")
    print(f"\nYou only have {chances} left ")
    
    if chances==0:
        print("lost")
        break
