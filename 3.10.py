print('zohair hashmi - 18b-127-cs - Section A')
print('Practice Problem - 3.10')

s = input('enter a word:')
def noVowel(s):
    for x in s:
        if (x == "a" or x == "e"  or x == "i" or x == "o"  or x == "u" or x == "A" or x == "E" or x == "I" or x == "O" or x == "U"):
            return("False")
        else:
            return("True")
print(noVowel(s))
            

    
