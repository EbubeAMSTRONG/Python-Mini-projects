
'normal version'

"""
import random

secret_number = random.randint(1,10)
guess = int(input("gues the number between 1 and 100 : "))

if guess == secret_number:
    print('Well done You guessed the correct number .')

else:
    print(f'Sorry your wrong , the correct nuber was {secret_number} Try Again')

"""

'looped version'

import random

while True:
   secret_number = random.randint(1, 10)  # Generate a new secret number for each round
   guess = int(input("Guess the number between 1 and 10: "))

   if guess == secret_number:
       print('\033[1m\033[92mWell done! You guessed the correct number!\033[0m')  # Highlight in green
       break  # Exit the loop if the guess is correct
   else:
       print(f"\033[1mSorry, you're wrong. The correct number was {secret_number}. Try again.\033[0m")  # Highlight in bold

