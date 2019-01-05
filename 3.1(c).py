print('zohair hashmi - 18b-127-cs - Section A')
print('Practice Problem - 3.1(c)')

a = eval(input('enter a number:'))
b = eval(input('enter a number:'))
hits = a+b
shield = a-b
if hits>10 and shield==0:
    print('you are dead')
else:
    print('You are alive')

