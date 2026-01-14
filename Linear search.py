arrayData = [1, 5, 6, 7, 8, 10, 12, 13, 19, 23]
#            0  1  2  3  4  5   6   7   8   9

def BinarySearch(number):
    upperbound = 9
    lowerbound = 0

    valuefound = False
    notinlist = False

    while valuefound == False and notinlist == False:
        midpoint = int((lowerbound + upperbound)/ 2)

        if arrayData[midpoint] == number:
            valuefound = True
            return True
        elif arrayData[midpoint] < number:   
            lowerbound = midpoint + 1
        else: 
            upperbound = midpoint - 1
        
        if lowerbound > upperbound:
            notinlist = True
            return False
        

temp = BinarySearch(10)
if temp == True:
    print("Value Found")
else:
    print("Value Not Found")
