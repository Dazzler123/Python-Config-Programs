# Exception handling ---> Bank card PIN number checker
pin = input()
try:
	#your code goes here
	int(pin)
	print("PIN code is created")
except ValueError:
	#and here
	print("Please enter a number")
# //////////////////////////////////////////////////////////


# Exception handling ---> Coffee machine
coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]
choice = int(input())
try:
	# your code goes here
	print(coffee[choice])
except:
	# and here
	print("Invalid number")
finally:
	# and finally here
	print("Have a good day")
# //////////////////////////////////////////////////////////