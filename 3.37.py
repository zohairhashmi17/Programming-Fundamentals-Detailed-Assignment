print('zohair hashmi - 18b-127-cs - Section A')
print('Practice Problem - 3.37')

def points(x1,y1,x2,y2):
    
    import math
    distance = math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))
    if x1==x2:
        print('the slope is infinity' + ' ' + 'and the distance is',distance)
    else:
        slope = ((y2 - y1)/(x2 - x1))
        print('the slope is',slope, 'and the distance is',distance)
coordinates1 = points(0,1,0,0)
coordinates2 = points(0,2,4,4)
print(coordinates1)
print(coordinates2)
