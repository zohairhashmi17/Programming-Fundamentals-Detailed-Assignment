print('zohair hashmi - 18b-127-cs - Section A')
print('Practice Problem - 3.25')

userlist = []
for x in range(3):
    a = input('name' + str(x+1) + ':')
    userlist.append(a)
for x in range(3):
    if userlist[x][:1] in ('A','a','B','b','c','C','c','D','d','e','E','f','F','G','g','h','H','i','I','J','j','K','k','L','l','M','m'):
        print(userlist[x])
