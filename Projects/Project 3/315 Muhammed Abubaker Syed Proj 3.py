#  ************************************************
#  CS1010  Proj 3
#  Name :  315 Muhammed Abubaker Syed
#  Purpose: The Holiday Travel Agency is putting
#  together some travel packages for vacations, and
#  they would like a program that will help them
#  calculate the cost of a customer’s trip.
#  *************************************************

# begin
# leave these as global constant initialized values
#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG

hotelrateflorida = 70
hotelratetexas = 60
hotelratecancum = 100
hotelratebahamas = 95
airfareflorida = 175.98
airfaretexas = 225.98
airfarecancum = 474.98
airfarebahamas = 355.98
#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG


#==================================================================
#======================== Start of the main function ==============
def main():
#input
    cityCode = input("Enter the letter code\nF - Florida\nT - Texas\nC - Cancum\nB - Bahamas")
    numDays = int(input("Enter the number of days of stay: "))
    weeksreservation = int(input("Enter the number of weeks in advance the reservation was done: "))



    cityStr = getcityStr(cityCode)
    hotelrate = gethotelrate(cityStr)
    hotelCost = gethotelCost(hotelrate, numDays)
    airfare = getAirFarecost(cityStr)
    longDisc = getLongDisc(cityStr, numDays, airfare, hotelrate)
    earlyDisc = getEarlyDisc (weeksreservation, hotelrate, numDays)
    finalCost = getfinalCost(hotelCost, airfare, longDisc, earlyDisc)
    printReceipt= getprintReceipt(cityStr, numDays, weeksreservation, hotelCost, airfare, longDisc, earlyDisc, finalCost)
#-------------------------------------------------------

#-------------------------------------------------------
# getcityStr is simply an addition to make the
# input process more fluid and easy.
#-------------------------------------------------------
def getcityStr(cityCode):
    if cityCode == "F" or cityCode == "f":
        cityStr = "Florida"
    elif cityCode == "T" or cityCode == "t":
        cityStr = "Texas"
    elif cityCode == "C" or cityCode == "c":
        cityStr = "Cancum"
    elif cityCode == "B" or cityCode == "b":
        cityStr = "Bahamas"
    return cityStr

#-------------------------------------------------------


#-------------------------------------------------------
# gethotelrate is the rate of the hotal perday which
# could be done using the global values.
#-------------------------------------------------------
def gethotelrate(cityStr):
    if cityStr == "Florida":
        hotelrate = hotelrateflorida
    elif cityStr == "Texas":
        hotelrate = hotelratetexas
    elif cityStr == "Cancum":
        hotelrate = hotelratecancum
    elif cityStr == "Bahamas":
        hotelrate = hotelratebahamas
    return hotelrate

#-------------------------------------------------------

#-------------------------------------------------------
# gethotelCost is the total cost of the hotelrate and no
# of days of stay.
#-------------------------------------------------------
def gethotelCost(hotelrate, numDays):
    hotelCost = hotelrate * numDays
    return hotelCost

#-------------------------------------------------------


#-------------------------------------------------------
# getAirFarecost is the fare which could be simply be
# done using the global values.
#-------------------------------------------------------
def getAirFarecost(cityStr):
    if cityStr == "Florida":
        airfare = airfareflorida
    elif cityStr == "Texas":
        airfare = airfaretexas
    elif cityStr == "Cancum":
        airfare = airfarecancum
    elif cityStr == "Bahamas":
        airfare = airfarebahamas
    return airfare

#-------------------------------------------------------

#-------------------------------------------------------
# getLongDisc will formulate the long discount that was
# given because of values (cityStr, numDays, airfare, hotelrate)
#-------------------------------------------------------
def getLongDisc(cityStr, numDays, airfare, hotelrate):
    if numDays > 7:
        if cityStr == "Florida" or cityStr == "Texas":
            longDisc = hotelrate
        else:
            airfare = airfare * 0.5
            longDisc = airfare
    else:
        longDisc = 0
    return longDisc

#-------------------------------------------------------


#-------------------------------------------------------
# getEarlyDisc will formulate the early disc that was
# given because of values (weeksreservation, hotelrate, numDays)
#-------------------------------------------------------
def getEarlyDisc (weeksreservation, hotelrate, numDays):
    if weeksreservation >= 10:
        earlyDisc = 0.1
    elif weeksreservation >=7:
        earlyDisc = 0.08
    elif weeksreservation >= 5:
        earlyDisc = 0.05
    else:
        earlyDisc = 0
    earlyDisc = hotelrate*numDays*earlyDisc
    return earlyDisc

#-------------------------------------------------------

#-------------------------------------------------------
# getfinalCost will do the calculation of the total cost
# using the values (hotelCost, airfare, longDisc, earlyDisc)
#-------------------------------------------------------
def getfinalCost(hotelCost, airfare, longDisc, earlyDisc):
    finalCost = hotelCost + airfare -(longDisc + earlyDisc)
    return finalCost

#-------------------------------------------------------

#-------------------------------------------------------
# getprintReceipt will print the receipt using all the values
# (cityStr, numDays, weeksreservation, hotelCost, airfare, longDisc, earlyDisc, finalCost).
# hint: this function will not have a return statement
#-------------------------------------------------------
def getprintReceipt(cityStr, numDays, weeksreservation, hotelCost, airfare, longDisc, earlyDisc, finalCost):
    print ("====== Holiday Travel Agency ======")
    print ("Destination :", cityStr)
    print ("Days Stayed :", numDays)
    print ("Weeks Before:", weeksreservation)
    print ("---------------------------------")
    print ("Hotel Cost        $", format(hotelCost, "7.2f"))
    print ("Air Fare          $", format(airfare, "7.2f"))
    print ("Long Stayed Disc  $", format(-longDisc, "7.2f"))
    print ("Early Disc        $", format(-earlyDisc, "7.2f"))
    print ("Final Cost        $", format(finalCost, "7.2f"))
    print ("=================================")

#-------------------------------------------------------
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

main()
input()
# end




