# Guess the number

''' Your program ask the user to guess a number and keep it in their head.
It then asks the user to input a range that would dictate the maximum and minum range
your program should guess from. If your program guesses too high or too low, the user
should be able to input "too high" or "too low" to notify you to fix your guess or you're right.
'''

'''
import random
*enter a number
enter_lowerBound  = ('')
enter_UpperBound = ('')

randomNumber = random.randit(lowerBound, upperBound)
if entry > UpperBound print("TOO HIGH")
If entry <  LowerBound print("too low")
if entry == range(1, 1000) and entry != randomNumber
	print('close to the answer! Please try again')
	***make program wait 5 secs before announcing***
	print('The number is ', randomNumber)
else:
	print('You guessed right!')
'''

#import random to generate random number
import random
#import time time to pause in program
import time
 
 #create a while loop 
while True:
	#enter the ranges of the guesses lower bound of range and upper bound of range
    lowerBound = int(input('Enter a lower bound: '))
    upperBound = int(input('Enter an upper bound: '))
    
    #enter the number your guess
    guess = int(input('Guess a number: '))
    #generate random number via ramdom module
    randomNumber = random.randrange(lowerBound, upperBound + 1)
    #conditions
    if guess > upperBound:
        print('Your guess is too high.')
        #pause code for 3 secs
        time.sleep(2)
        print('The magic number is ', randomNumber)
    elif guess < lowerBound:
        print('Your guess is too low')
        time.sleep(2)
        print('The magic number is ', randomNumber)
    elif guess == randomNumber:
        print("Nice one! You guessed right.")

        #check if number is within range but not equal to randomNumber
    elif (guess > randomNumber or guess < randomNumber) and guess != randomNumber:
        print("You're close!")
        time.sleep(2)
        print("The magic number is ", randomNumber)
    time.sleep(2)
    retry = input("Do you want to try again? yes(y) or no(n)")
    if retry == 'y':
        continue
    else:
        break
