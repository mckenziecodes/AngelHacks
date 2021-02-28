import random 
from random import randint
def guessing_game():  
  lower = int(input("Enter a lower bound: "))
  upper = int(input("Enter an upper bound: "))
  if upper <= lower:
    raise Exception("Impossible. Run the program again.")
  actual = randint(lower, upper)

  
  user_num = int(input("Enter a number within this range: "))
  number_guesses = []

  while user_num != actual: 
    if user_num < actual:
      print("Too low! Try again.")
      number_guesses.append(user_num)
      user_num = int(input("Enter another number: "))

    if user_num > actual: 
      print("Too high! Try again.")
      number_guesses.append(user_num)
      user_num = int(input("Enter another number: "))

  if user_num == actual:
    print("Great job! You guessed it!")
    number_guesses.append(user_num)
    print("It took you ", len(number_guesses), " times to guess correctly. Your guesses were:\n", number_guesses)  

  
