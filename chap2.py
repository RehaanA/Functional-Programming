def proj2_1_a():
	print("This is a temperature conversion program!")
	celsius = eval(input("What is the temperature in Celsius?"))
	fahrenheit = 9/5(celsius) + 32
	print("The temperatures are: ", fahrenheit)

def proj2_1_b():
	print("This is a temperature conversion program!")
	c1, c2, c3, c4 = eval(input("Please input 4 temperatures in celsius separated by commas: "))
	clist = list([c1 ,c2, c3, c4])
	for celsius in clist:
		fahrenheit = 9/5 * celsius + 32
		print(celsius,' celsius equal ',fahrenheit,' fahrenheit.')

#Problem 1c
def proj2_1_c():
	print("This is a celsius and fahrenheit chart")
	celsius = 0
	for i in range(11):
		fahrenheit = 9/5 * celsius + 32
		print("|",celsius, "celsius | ", fahrenheit,"fahrenheit |")

def proj2_2():
	print("This is a program that takes the average of any 5 numbers!")
	a, b, c, d, e = eval(input("Type in your 5 scores separated by commas: "))
	average = (a+b+c+d+e)/5
	print("Your average is ", average)

def proj2_3():
	principle = eval(input("Enter your first principle: "))
	interestRate = eval(input("Enter your interest rate as a decimal"))
	time = eval(input("How many years?: "))
	for year in range(time):
		principle *= (1+interestRate)
		print('Year:', year + 1, '=', principle)

def proj2_4():
	print("This is a centimeter to meter conversion program!")
	c1, c2, c3 = eval(input("Type 3 measurements in centimeters with commas: "))
	clist = list([c1, c2, c3])
	for centimeters in clist:
		meter = centimeters/100
		print(centimeters,' centimeters equal ', meter,' meters.')
proj2_4()
