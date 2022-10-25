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
resul = file.readlines()
print(resul[1])
print(resul[2])
print(resul[3])
file.close()
# //////////////////////////////////////////////////////////