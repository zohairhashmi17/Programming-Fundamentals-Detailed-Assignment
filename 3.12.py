print('zohair hashmi - 18b-127-cs - Section A')
print('Practice Problem - 3.12')

def negatives(number):
    neg_num = []
    for i in number:
        if i<0:
             neg_num.append(i)
    return neg_num

x = negatives([2,3,-4,5,-9])
print(x)
        
