import random
for i in range(10):
    num1,num2 = random.randint(1,100),random.randint(1,100)
    answer = num1 + num2
    question = int(input(f'what is :\n\n{num1} + {num2}?\n'))
    if question == answer:
        print('Correct !!')
    else:
        print('InCorrect')
   