#Chapter 2 Problem 1a
def proj2_1_a():
	print("This is a temperature conversion program!")
	celsius = eval(input("What is the temperature in Celsius?"))
	fahrenheit = 9/5(celsius) + 32
	print("The temperatures are: ", fahrenheit)

#Chapter 2 Problem 1b
def proj2_1_b():
	print("This is a temperature conversion program!")
	c1, c2, c3, c4 = eval(input("Please input 4 temperatures in celsius separated by commas: "))
	clist = list([c1 ,c2, c3, c4])
	for celsius in clist:
		fahrenheit = 9/5 * celsius + 32
		print(celsius,' celsius equal ',fahrenheit,' fahrenheit.')

#Chapter 2 Problem 1c
def proj2_1_c():
	print("This is a celsius and fahrenheit temperature chart")
	celsius = 0
	for i in range(10):
		celsius += 5
		fahrenheit = 9/5 * celsius + 32
		print("|",celsius, "degrees celsius | ", fahrenheit,"degrees fahrenheit |")

#Chapter 2 Problem 2
def proj2_2():
	print("This is a program that takes the average of any 5 numbers!")
	a, b, c, d, e = eval(input("Type in your 5 scores separated by commas: "))
	average = (a + b + c + d + e) / 5
	print("Your average is ", average)

#Chapter 2 Problem 3
def proj2_3():
	principle = eval(input("Enter your first principle: "))
	interestRate = eval(input("Enter your interest rate as a decimal"))
	time = eval(input("How many years?: "))
	for year in range(time):
		principle *= (1 + interestRate)
		print('Year:', year + 1, '=', principle)

#Chapter 2 Problem 4
def proj2_4():
	print("This is a centimeter to meter conversion program!")
	cm1, cm2, cm3 = eval(input("Type 3 measurements in centimeters with commas: "))
	cmlist = list([cm1, cm2, cm3])
	for centimeters in cmlist:
		meter = centimeters/100
		print(centimeters,' centimeters equal ', meter,' meters.')
proj2_4()
