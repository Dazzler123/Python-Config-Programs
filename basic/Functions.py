
# returning from functions - hashtag generator
s = input()
def hashtagGen(text):
    # your code goes here
    s1 = text.replace(" ", "")
    return "#" + s1

print(hashtagGen(s))


# random module - dice number generator
import random
random.seed(int(input())) # initialize random & take user input

#generate the random values for every dice
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print(dice1)
print(dice2)