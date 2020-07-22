#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      JenJab
#
# Created:     03/11/2018
# Copyright:   (c) JenJab 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
MaxCars = 100

def main():
    owners     = [""]  * MaxCars
    cartype    = [""]  * MaxCars
    mileage    = [0]   * MaxCars
    color      = [""]  * MaxCars
    passengers = [0]   * MaxCars
    NumCars = 0
    hipos = -1
    avg = 0
    avgHonda = 0


    NumCars = fillList(owners, cartype, mileage, color, passengers)
    printList(owners, cartype, mileage, color, passengers, NumCars)
    hipos = gethimiles(mileage, NumCars)
    showOwners(owners, cartype, "Honda", NumCars)
    showOwners(owners, cartype, "Chevy", NumCars)
    avg = GetAverage(mileage, NumCars)
    avgHonda = GetAverageHonda(cartype, mileage, NumCars)
    print (owners[hipos], "owns a", cartype[hipos],
                "with the highest mileage of", mileage[hipos])
    print(" ") #blank line
    print("The average is ", format(avg, ".2f"))
    print("The average  Hondais ", format(avgHonda, ".2f"))


#--------------------------------------------------------------------------------
def fillList(owners, cartype, mileage, color, passengers):

    infile = open("fleet.txt", "r")
    NumCars = 0
    line = infile.readline()
    while line != "" and NumCars < MaxCars:
        owners[NumCars] = line.rstrip("\n")
        cartype[NumCars] = (infile.readline()).rstrip("\n")
        mileage[NumCars] = int(infile.readline())
        color[NumCars] = (infile.readline()).rstrip("\n")
        passengers[NumCars] = int(infile.readline())

        NumCars = NumCars + 1
        line = infile.readline()

    infile.close()
    return  NumCars

#-------------------------------------------------------------------------------

def printList(owners, cartype, mileage, color, passengers, NumCars):

    print("Owner".ljust(20), "Car".ljust(10), "Miles".ljust(10),
                "Color".ljust(10), "Passengers".ljust(10))

    print("-----".ljust(20), "---".ljust(10), "-----".ljust(10)
                , "-----".ljust(10), "----------".ljust(10))

    for k in range(NumCars):
        print(owners[k].ljust(20), cartype[k].ljust(10),str(mileage[k]).ljust(10),
                    color[k].ljust(10), str(passengers[k]).ljust(10))

    print(" ") #blank line

#--------------------------------------------------------------------------------

def gethimiles(mileage, NumCars):

    hilemiles = -500
    hipos = -1

    for k in range(NumCars):
        if (mileage[k] > hilemiles):
            hilemiles = mileage[k]
            hipos = k

    return hipos
#--------------------------------------------------------------------------------
def showOwners(owners, cartype, mycar, NumCars):

    print(" ") #blank line
    print("The ", mycar,  " are:")
    print("-----------------")
    for k in range(NumCars):
        if cartype[k] == mycar:
            print(owners[k])

    print(" ") #blank line
#--------------------------------------------------------------------------------

def GetAverage(mileage, NumCars):

        #Calculate the average miles
    sum = 0
    for k in range(NumCars):
        sum += mileage[k]

    #The average is the sum divided by NumCars
    avg = sum / NumCars
    return avg

#--------------------------------------------------------------------------------

def GetAverageHonda(cartype, mileage, NumCars):

    #Calculate the average miles
    cntHonda = 0
    sum = 0
    for k in range(NumCars):
        if cartype[k] == "Honda":
            cntHonda += 1
            sum += mileage[k]

    #The average is the sum divided by NumCars
    avg = sum / cntHonda
    return avg

main()

input()
#end

