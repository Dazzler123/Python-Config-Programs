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


# File I/O ---> Text file reading program
file = open("filename.txt")
n = int(input())

#your code goes here
resul = file.readlines()
print(resul[n])
file.close()
# //////////////////////////////////////////////////////////

# File I/O ---> Text file writing program
names = ["John", "Oscar", "Jacob"]
file = open("names.txt", "w+")
#write down the names into the file
file.write(names[0])
file.write(names[1])
file.write(names[2])
file.close()

file= open("names.txt", "r")
#output the content of file in console
print(file.readline())
file.close()
# //////////////////////////////////////////////////////////