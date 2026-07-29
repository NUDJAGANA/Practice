secret_word = "Star Wars"
to_print = ""
guessed_letters = []
for char in secret_word:
    if char == " ":
        to_print += "/"
    else:
        to_print += "_"

print(to_print)

user_name = input("Guess a letter: ")
guessed_letters.append(user_guess)

for char in secret_word:
    if char is guessed_letters:
        to_print += char
    else:
         if char == " ":
           to_print += "/"
         else:
           to_print += "_"

print("\n" + to_print)


