import random

number = random.randint(1,100)
right = 5
print(number)

while right > 0:
  guess = int(input("Please enter your guess: "))
  right -= 1  # right = right - 1
  if guess == number:
    print("<<<< BINGOOO!!! >>>> Are you a mindreader? Congrats!!!")
    break
  elif guess > number:
    print(f"Please enter lower !!!  Remain rights : {right}")
  elif guess < number:
    print(f"Please enter higher !!!  Remain rights : {right}")
else:
  print(f"<<<< GAME OVER >>>> Your rights are over. Number : {number}")
