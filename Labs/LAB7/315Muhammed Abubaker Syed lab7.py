#  ************************************************
#  CS1010  Lab 7
#  Name :  315 Muhammed Abubaker Syed
#  Name :  347 Khalifah AlIbrahim
#  Purpose: Process City Data. Thi sprogram will read
#  data from a file and find the avg budget, highest
#  budget and the cities that have gone over budget
#  *************************************************
#begin
MaxCities = 100

def main():
#1 Create the lists here
#???????????????????
    cities     = [""]  * MaxCities
    revenue    = [0]  * MaxCities
    budget    = [0]   * MaxCities
    NumCities = 0
    hipos = -1
    avg = 0

    NumCities = fillList(cities, budget, revenue)
    printList(cities, budget, revenue, NumCities)


    #-------------------------------------------------------------------------------------
    #2
    #Call the function getavgbudget, use avg (What do you need to send it)
    #???????????????????????????
    avg = getavgbudget(budget,NumCities)
    #-------------------------------------------------------------------------------------
    #3
    #Call the function findhibudget, use hipos (What do you need to send it)
    #???????????????????????????
    hipos = findhibudget(budget, cities, NumCities)

    #4
    #Call the function showshortfalls (What do you need to send it)
    #???????????????????????????
    shortfall = showshortfalls(revenue,budget,cities,NumCities)

#--------------------------------------------------------------------------------
# This function will read the data from the file until the fil is empty
def fillList(cities, budget, revenue):

    infile = open("citydata.txt", "r")
    NumCities = 0
    line = infile.readline()
    while line != "" and NumCities < MaxCities:
        cities[NumCities] = line.rstrip("\n")
        budget[NumCities] = int(infile.readline())
        revenue[NumCities] = int(infile.readline())

        NumCities = NumCities + 1
        line = infile.readline()

    infile.close()
    return  NumCities

#-------------------------------------------------------------------------------
# This function will print the city data
def printList(cities, budget, revenue, NumCities):

    print("Cities".ljust(20), "Budget".ljust(10), "Revenue".ljust(10))
    print("------".ljust(20), "------".ljust(10), "-------".ljust(10))

    for k in range(NumCities):
        print(cities[k].ljust(20), str(budget[k]).ljust(10),str(revenue[k]).ljust(10))

    print(" ") #blank line

#--------------------------------------------------------------------------------
#5 write the getavgbudget
#??????????????????????????
def getavgbudget(budget,NumCities):

        #Calculate the average miles
    sum = 0
    for k in range(NumCities):
        sum += budget[k]
    avg = sum / NumCities

    print("")
    print("")
    print("The average budget is $", format(avg, "7.0f"))
    return avg


#--------------------------------------------------------------------------------
#6 write the findhibudget
#??????????????????????????
def findhibudget(budget, cities, NumCities):

    hibudget = -500
    hipos = -1

    for k in range(NumCities):
        if (budget[k] > hibudget):
            hibudget = budget[k]
            hipos = k
    print("")
    print("")
    print(cities[hipos], "has the highest budget with", format (budget[hipos],"7.0f"))
    return hipos

#--------------------------------------------------------------------------------
#7 write the showshortfalls (hint create a variable called over)
# I have supplied the output header code, use it to create your print statement
# to print the cities that match the criteria
#??????????????????????????
def showshortfalls(revenue,budget,cities,NumCities):
    print("")
    print("")
    print("The cities with a budget shortfall are:")
    print()#space
    print("Cities".ljust(20), "Over".ljust(10))
    print("------".ljust(20), "----".ljust(10))
    for k in range(NumCities):
        if (budget[k] > revenue[k]):
            over = budget[k] - revenue[k]
            overstr = str(over)
            print(cities[k].ljust(20), overstr.ljust(10))

    #???????????????????????????????



main()
input()
#end

