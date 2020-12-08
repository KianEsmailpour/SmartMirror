def print_days():
    days = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    #print(days)
    for day in days:
        print(f"| {day}\t",end = '')



def pringArray(a):
    for i in a:
        print(i)

def findMax(a):
    max = a[0]
    for i in a:
        if(i>max):
            max = i
    return max

def findMin(a):
    min = a[0]
    for i in a:
        if(i<min):
            min = i
    return min
def count( b):
    return b.__len__()
    count = 0
    for v in b:
        count+=1
    return count

print("hello wotrld!")

def printLine(width,baseChar=' ',firstChar='│',endChar='│'):
    print(firstChar,end="")
    for i in range(width):
        print(baseChar,end="")
    print(endChar)

def printTable(width,hight):
    printLine(width,'─','┌','┐')
    for j in range(hight):
        printLine(width)
    printLine(width,'─','└','┘')


printTable(20,5)
#print_days()
# a=[7,2,3,1,16,7,1,23,20]

# pringArray(a)
# max = findMax(a)
# print(f"max = {max}")
# min = findMin(a)
# print(f"min = {min}")
# c = count(a)
# print(f"count = {a.__len__()}")