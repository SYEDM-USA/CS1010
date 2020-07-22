#  ************************************************
#  CS1010  Lab 4
#  Name :  315 Muhammed Abubaker Syed
#  Name :  347 Khalifah Alibrahim
#  Purpose: The program will ask a user for
#  the type of rental car, how many miles were driven
#  and if they are preferred customer.
#  *************************************************

# leave these as global constant initialized values
#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
WREC_PRICE = 15.00
ECON_PRICE = 25.00
COMP_PRICE = 30.00
SUV_PRICE = 60.00
PER_MILES = 0.25
PREF_DISC = 0.15
#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG

#==================================================================
#======================== Start of the main function ==============
def main():
#input
    rentalCode = input("Enter the letter code\nW - Wreck\nE - Economy\nC - Compact\nS - SUV")
    numDays = int(input("Enter the number of days rented: "))
    numMiles = int(input("Enter the number of miles driven: "))
    prefCust = input("Are you a preferred customer enter Y or N")

    rentalStr = getRentalStr(rentalCode)
    rentalCost = getRentalCost(rentalStr, numDays)
    mileCost = getMileCost(numMiles, numDays)
    prefDisc = getPrefDisc(prefCust, rentalCost, mileCost)
    finalCost = getfinalCost(rentalCost, mileCost, prefDisc)
    printReceipt= getprintReceipt(rentalStr, numDays, rentalCost, mileCost, prefDisc, finalCost)
#-------------------------------------------------------
# convert this into a function called getRentalStr
#-------------------------------------------------------
def getRentalStr(rentalCode):
    if rentalCode == "W" or rentalCode == "w":
        rentalStr = "Wreck"
    elif rentalCode == "E" or rentalCode == "e":
        rentalStr = "Economy"
    elif rentalCode == "C" or rentalCode == "c":
        rentalStr = "Compact"
    elif rentalCode == "S" or rentalCode == "s":
        rentalStr = "SUV"
    return rentalStr
#-------------------------------------------------------


#-------------------------------------------------------
# convert this into a function called getRentalCost
#-------------------------------------------------------
def getRentalCost(rentalStr, numDays):
    if rentalStr == "Wreck":
        rentalRate =  WREC_PRICE
    elif rentalStr == "Economy":
        rentalRate =  ECON_PRICE
    elif rentalStr == "Compact":
        rentalRate =  COMP_PRICE
    elif rentalStr == "SUV":
        rentalRate =  SUV_PRICE
    rentalCost = rentalRate *  numDays
    return rentalCost

#-------------------------------------------------------


#-------------------------------------------------------
# convert this into a function called getMileCost
#-------------------------------------------------------
def getMileCost(numMiles, numDays):
    excessMiles = numMiles - numDays * 100
    if excessMiles > 0:
        mileCost = excessMiles * PER_MILES
    else:
        mileCost = 0
    return mileCost

#-------------------------------------------------------


#-------------------------------------------------------
# convert this into a function called getPrefDisc
#-------------------------------------------------------
def getPrefDisc(prefCust, rentalCost, mileCost):
    if prefCust == "Y" or prefCust == "y":
        prefDisc = (rentalCost + mileCost) * PREF_DISC
    else:
        prefDisc = 0
    return prefDisc

#-------------------------------------------------------

def getfinalCost(rentalCost, mileCost, prefDisc):
    finalCost = rentalCost + mileCost - prefDisc
    return finalCost



#-------------------------------------------------------
# convert this into a function called printReceipt
# hint: this function will not have a return statement
#-------------------------------------------------------
def getprintReceipt(rentalStr, numDays, rentalCost, mileCost, prefDisc, finalCost):
    print ("======= Falcon Rentals ==========")
    print ("Rental Type:", rentalStr)
    print ("Days Rented:", numDays)
    print ("Rental Cost     $", format(rentalCost, "7.2f"))
    print ("Mileage Cost    $", format(mileCost, "7.2f"))
    print ("Preferred Disc  $", format(-prefDisc, "7.2f"))
    print ("Final Cost      $", format(finalCost, "7.2f"))
    print ("=================================")

#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

main()
input()
# end