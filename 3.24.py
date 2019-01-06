print('zohair hashmi - 18b-127-cs - Section A')
print('Practice Problem - 3.24')

userlist = []
for x in range(3):
    a = input('word' + str(x+1) + ':')
    userlist.append(a)
for x in range(3):
    if userlist[x]!='secret':
        print(userlist[x])
        
