import random
from game_data import data
from art import*
import os

# Global Variables 
valA = random.choice(data)
valB = random.choice(data)

if valA == valB:
  valB = random.choice(data)

score = 0
lose = False
  
def Main():
  # Game Loop
  
  while lose == False:
    cls()
    game_logic()
  
  # Game End
  cls()
  print(logo)
  print(f'\nSorry, that\'s wrong. Final score: {score}' )
  
def gen_rand():
  # Generate random choice
  global valA
  global valB
  valA = valB
  valB = random.choice(data)
  
  if valA == valB:
    valB = random.choice(data)
  

# Format value data into printable format

def format_accounts(account):
  valA_name = account['name']
  valA_descr = account['description']
  valA_country = account['country']

  output = f'{valA_name}, {valA_descr}, from {valA_country}'
  return output

# Game Start
def game_logic():
  global valA
  global valB
  global lose
  global score

  print(logo)

  if score != 0: 
    print(f'\nYou\'re right! Current score: {score}')
  else:
    pass

  print(f'\nCompare A: {format_accounts(valA)}.')

  # Display Vs.

  print(vs)

  print(f'\nAgainst B: {format_accounts(valB)}')

  # Ask User for input
  
  while True:
    user_input = input('\nWho has more followers on Instagram? Type "A" or "B": ').upper()

    if user_input == 'A' or 'B':
      break
    else:
      print('\nInvalid input. Try again')
      continue

  # Check if user_input is correct

  countA = int(valA['follower_count'])
  countB = int(valB['follower_count'])

  if countA > countB and user_input == 'A':
    score += 1
    gen_rand()
  elif countB > countA and user_input == 'B':
    score += 1
    gen_rand()
  else:
    lose = True

# Clear Screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

Main()