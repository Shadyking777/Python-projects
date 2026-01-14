arrayData = [10, 5, 6, 7, 12, 1]

def Insertionsort():
    arraysize = 6

    for pointer in range(1, arraysize):
        #hum ek temp variable banate hein take value lost na ho
        Valuetoinsert = arrayData[pointer]
        #this is the correct position that you are trying to find
        holeposition = pointer

        while holeposition > 0 and arrayData[holeposition - 1] > Valuetoinsert:

            #if you are in loop then you should insert and keep on finding correct holeposition
            #shifting values to the right
            arrayData[holeposition] = arrayData[holeposition - 1]
            holeposition = holeposition - 1

        
        arrayData[holeposition] = Valuetoinsert


Insertionsort()
print(arrayData)
