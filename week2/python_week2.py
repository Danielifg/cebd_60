"""
1. The function picks a number between 0 and 200.
	 Then you should input different values until you guess the hidden number correctly.
	 The function would return “way upper”,“upper”, “lower”, “way lower”, “close”, ”bingo”.
	 It’s your choice to pick the ranges you want to use for responses. The success measure
	 is how intuitive the communication is between the user and the function.
"""
import random

def guessNum(numRange):
	secret = random.choice(list(range(numRange))); guess=''
	while secret != guess:
			guess  = int(input('Guess a number from 0 to 200? : '))
			diff   = int((secret-guess) if secret>guess else (guess-secret))
			label  = 'upper' if secret>guess else 'lower'
			if secret==guess: print('bingo!!')
			elif diff <= 10:  print('close',label)
			elif diff < 100:  print(label)
			elif diff >= 100: print('way', label)

guessNum(200)

"""
2. Now do the reverse and you guide the program to get close 
   to (and eventually guess)your number in mind.
"""
def guessNumInMind(numRange):
	guess = random.choice(list(range(numRange)));
	end = guess; start = 0; guessing = '';
	print('\n OK! Think a number from 0 to 200 ')
	input('Ready ? press enter...')
	print('Is it ',guess)
	bingo = input('(y/n)? : ')
	if bingo == 'y': print('Bingo !!!')
	else:
		while bingo != 'y':
			answer = input('Let me guess (upper/lower)? : '); lucky = guessing if guessing else guess;
			if answer=='upper'  :	guessing = random.choice(list(range(lucky,numRange)))
			elif answer=='lower':	guessing = random.choice(list(range(0,lucky)))
			print('Is it',guessing)
			bingo = input('(y/n) ? : ')
			if bingo == 'y':
				 print('Bingo !!!')
				 break

guessNumInMind(200)

"""
3. Now improve your code by limiting the guesses and let the function to 
	 guide you after the second guess that as long as the reply 
	 is not way up/low. Try to compare two functions 
	 over one chosennumber and count the guesses,
"""
def limitGuess(numRange):
	secret = random.choice(list(range(numRange))); count = 0; limit = 5;
	while count <= limit:
		if count == limit: 
			print('Sorry, lost!')
			break
		guess = int(input("Try a number: ")); count+=1;
		if guess == secret: 
			print("You won!")
			break

limitGuess(200)

"""
4. Again do reverse and make the communication more interesting.
"""
def guessNumInMind(numRange):
	guess = random.choice(list(range(numRange)));
	end = guess; start = 0; guessing = ''; counter=0; limit=5;
	print('\n OK! Think a number from 0 to 200 this time I\'ll get it within 5 times')
	input('Ready ? press enter...')
	print('Is it ',guess)
	bingo = input('(y/n)? : ')
	if bingo == 'y': print('Bingo !!!')
	else:
		while bingo != 'y':			
			answer = input('Let me guess (upper/lower)? : '); 
			lucky = guessing if guessing else guess; 
			if answer=='upper'  :	guessing = random.choice(list(range(lucky,numRange)))
			elif answer=='lower':	guessing = random.choice(list(range(0,lucky)))
			print('Is it',guessing)
			bingo = input('(y/n) ? : '); counter +=1;
			if counter >= limit:
				print('Hmm OK,I guess I\'ll call Alexa or Mr. Watson next time!')
				print('you win...')
				break
			if bingo == 'y':
				 print('Bingo !!!')
				 break

guessNumInMind(200)