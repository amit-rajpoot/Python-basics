import random

easy_words = ["ball","cat","dog","mon","sat"]
medium_words = ["tiger","python","cobra","anaconda","elephant"]
hard_words = ["Sesquipedalian","Obfuscate","Quixotic","Peregrination","Inscrutable"]

print("WELCOME TO THE PASSWORD GUESSING GAME---->")
print("Choose the level you want to play:easy,medium,hard---->")


level = input("Enter difficulty: ").lower()

if level == "easy":
    secert = random.choice(easy_words)

elif level == "medium":
    secert = random.choice(medium_words)

elif level == "hard":
    secert = random.choice(hard_words)

else:
    print("Invalid choice . Defaulting to easy level")
    secert = random.choice(easy_words)

attempts = 0
print("\nGuess the secert password")

while True:
    guess =  input("Enter your guess: ").lower()
    attempts += 1

    if guess == secert:
        print(f"Congratulations ^ /-\ ^ You guessed it in {attempts} attempts.")
        break

    hint = ""

    for i in range(len(secert)):
        if i < len(guess) and guess[i] == secert[i]:
            hint += guess [i]

        else:
            hint += "_"

    print("Hint: ",hint)
print("<--GAME OVER-->")