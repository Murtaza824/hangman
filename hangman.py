import random

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

usedLetters = []
print("Hangman")
print()
counter = 0

wordChosen = random.choice(listOfWords)

while True:
  counter += 1
  print()
  letter = input("Choose a letter: ").strip().lower()g
  print(wordChosen)

  if counter == 6:
    print("You ran out of lives")
    break

  if letter in usedLetters:
    print("You've tried that before")
  else:
    usedLetters.append(letter)

  allLetters = True
  if letter in wordChosen:
    print("You found a letter")
    print()
  else:
    print("Nope, not in there.")
    print()
  
  for i in wordChosen:
    if i in usedLetters:
      print(i, end = "")
    else:
      print("_", end= "" )
      allLetters = False
  print()
  
  if allLetters == True:
    print(f"You won with {6-counter} lives left!")
    break
