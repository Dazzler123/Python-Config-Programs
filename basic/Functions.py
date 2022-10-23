
# returning from functions - hashtag generator
s = input()
def hashtagGen(text):
    # your code goes here
    s1 = text.replace(" ", "")
    return "#" + s1

print(hashtagGen(s))