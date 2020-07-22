#  ************************************************
#  CS1010  Proj 1
#  Name :  315 Muhammed Abubaker Syed
#  Purpose: The program will ask a user for a date
#  and the program will identify it between two solutions
#  the magic number or NOT a magic number.
#  *************************************************

# initialize

# input section

month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
fourdigit = int(input("Enter the year: "))

# calculation
shortyear = fourdigit - (round(fourdigit, -2))

if month == 1:
    strmonth = "January"
elif month == 2:
    strmonth = "Febraury"
elif month == 3:
    strmonth = "March"
elif month == 4:
    strmonth = "April"
elif month == 5:
    strmonth = "May"
elif month == 6:
    strmonth = "June"
elif month == 7:
    strmonth = "July"
elif month == 8:
    strmonth = "August"
elif month == 9:
    strmonth = "September"
elif month == 10:
    strmonth = "October"
elif month == 11:
    strmonth = "November"
else:
    strmonth = "December"


# output section

if shortyear < 0:
    shortyear = 100 + shortyear
    if shortyear == fourdigit % (fourdigit - month * day):

        print("%(s)s %(d)s , %(f)s is a magic date!" % {'s': strmonth, 'd': day, "f": fourdigit})
    else:
     print("%(s)s %(d)s , %(f)s is NOT a magic date!" % {'s': strmonth, 'd': day, "f": fourdigit})

elif shortyear == fourdigit % (fourdigit - month * day):
        print("%(s)s %(d)s , %(f)s is a magic date!" % {'s': strmonth, 'd': day, "f": fourdigit})

else:
     print("%(s)s %(d)s , %(f)s is NOT a magic date!" % {'s': strmonth, 'd': day, "f": fourdigit})


input()