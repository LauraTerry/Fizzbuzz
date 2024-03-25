num = int (input ("Fizz, Buzz, or Fizzbuzz? Enter a whole number:"))
if num % (3 * 5) == 0:
	print("Fizzbuzz")
elif num % 5 == 0:
	print("Buzz")
elif num % 3 == 0:
	print("Fizz")
else:
	print (num)
