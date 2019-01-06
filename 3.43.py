print('zohair hashmi - 18b-127-cs - Section A')
print('Practice Problem - 3.43')

def hit(x1,y1,r,x2,y2):
    import math
    c_diff = math.sqrt((x2 - x1)**2) + ((y2 - y1)**2)
    if c_diff <= (r**2):
        return True
    else:
        return False

x1 = hit(0, 0, 3, 3, 0)
print(x1)
x2 = hit(0, 0, 3, 4, 0)
print(x2)
