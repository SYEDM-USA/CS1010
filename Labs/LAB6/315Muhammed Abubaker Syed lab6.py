#  ************************************************
#  CS1010  Lab 6
#  Name :  315 Muhammed Abubaker Syed
#  Purpose: The program will zoo read data
#  and divide the animals up into two categories.
#  The code will yield the average weight of each category
#  along with the heaviest and lightest overall animals.
#  *************************************************
#begin

infile = open("zoo.txt", "r")
def main():
    jumbosum = 0
    midsum = 0
    largerfid = 0
    largename = ""
    largeweight = -500
    jumbocnt = 0
    smallrfid = 0
    smallname = ""
    smallweight = 500
    midcnt = 0


    line = infile.readline()
    while line != "":
        rfid = int(line)
        name = (infile.readline()).rstrip("\n")
        weight = int(infile.readline())
        if weight >= 200:
            jumbosum += weight
            jumbocnt += 1
        else:
            midsum += weight
            midcnt += 1
        if weight > largeweight:
            largerfid = rfid
            largename = name
            largeweight = weight
        if weight < smallweight:
            smallrfid = rfid
            smallname = name
            smallweight = weight
        line = infile.readline()

    jumboavg = jumbosum / jumbocnt
    midavg = midsum / midcnt

    print("------------------------------")
    print("Largest RFID  : ",largerfid)
    print("Largest name  : ",largename )
    print("Largest Weight: ",largeweight )
    print("------------------------------")
    print("Smallest RFID  : ",smallrfid )
    print("Smallest name  : ",smallname )
    print("Smallest Weight: ",smallweight )
    print("------------------------------")
    print("Jumbo-Jungle Average: ", format(jumboavg, "3.2f"))
    print("Mid-Meadows Average: ", format(midavg, "3.2f"))

main()
input()
#end

