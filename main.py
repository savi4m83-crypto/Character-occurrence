# Write a program to check how many times a character is repeated in a word?


word=str(input("Enter your word"))
character=str(input("enter your character"))
count=0
for i in word:
    if (i==character):
        count=count+1
print(count)