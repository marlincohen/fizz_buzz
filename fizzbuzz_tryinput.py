try:
	my_input = raw_input("Enter the upper end of the range for Fizzbuzz ")
	input_int = int(my_input)

	for n in range (0,input_int):
		if n % 5 == 0 and n % 3 == 0:
			print "fizzbuzz"
		elif n % 3 == 0:
			print "fizz"
		elif n % 5 == 0:
			print "buzz"
		else:
			print n
except ValueError:
	print "Enter numerical value, please!"
	my_input = raw_input("Enter the upper end of the range for Fizzbuzz ")
	input_int = int(my_input)

	for n in range (0,input_int):
		if n % 5 == 0 and n % 3 == 0:
			print "fizzbuzz"
		elif n % 3 == 0:
			print "fizz"
		elif n % 5 == 0:
			print "buzz"
		else:
			print n
