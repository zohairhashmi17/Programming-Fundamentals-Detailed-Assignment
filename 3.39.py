print('zohair hashmi - 18b-127-cs - Section A')
print('Practice Problem - 3.39')

def collision(x1,y1,r1,x2,y2,r2):
    import math
    c_diff = ((x2-x1)**2+(y2-y1)**2)
    if c_diff <= (r1+r2)**2:
        return True
    else:
        return False

x1 = collision(0,1,2,3,2,2)
print(x1)
x2 = collision(2,5,2,1,0,2)
print(x2)
    
