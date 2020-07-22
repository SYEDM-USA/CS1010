#  ************************************************
#  CS1010  lAB 5
#  Name :  315 Muhammed Abubaker Syed
#  Purpose: Write a complete Python program with a
#  main function that inputs a user’s height, weight
#  and age as floats.  Then compute clothing sizes
#  according to the formulas, display the results.
#  *************************************************

# begin
# leave these as global constant initialized values
#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG

#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG

#==================================================================
#======================== Start of the main function ==============
# initialize

def main():
    height = int(input("Enter your height: "))
    weight = int(input("Enter your weight: "))
    age = int(input("Enter your age: "))
    hatsize = gethatsize(height, weight)
    sweatersize = getsweatersize(height, weight, age)
    waistsize = getwaistsize(weight, age)
    printsize(hatsize, sweatersize, waistsize)

#-------------------------------------------------------
# convert this into a function called gethatsize
#-------------------------------------------------------
def gethatsize(height, weight):
    hatsize = weight/height * 2.9
    return hatsize

#-------------------------------------------------------


#-------------------------------------------------------
# convert this into a function called getsweatersize
#-------------------------------------------------------

def getsweatersize(height, weight, age):
    sweatersize = (height*weight/301)+(1/8*(age // 10))
    return sweatersize

#-------------------------------------------------------


#-------------------------------------------------------
# convert this into a function called getwaistsizesize
#-------------------------------------------------------

def getwaistsize(weight, age):
    waistsize = (weight/5.7)+(0.1*(age//2))
    return waistsize

#-------------------------------------------------------


#-------------------------------------------------------
# convert this into a function called printsize
#-------------------------------------------------------
def printsize(hatsize, sweatersize, waistsize):
    print("Hat Size     :", format(hatsize, ".2f"))
    print("Sweater Size :", format(sweatersize, ".2f"))
    print("Pant Size    :", format(waistsize, ".2f"))

#-------------------------------------------------------


#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

main()
input()
#end