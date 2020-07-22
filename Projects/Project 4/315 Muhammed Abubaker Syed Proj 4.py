#  ************************************************
#  CS1010  Proj 4
#  Name :  315 Muhammed Abubaker Syed
#  Purpose: You are an analyst for a sports information
#  organization who has been given a file of names,
#  racing times and ages for participants in a 1-mile race.
#  Your task is to determine results for participants
#  in various age categories (under 30, 30 to 50,
#  and over 50) who qualify for the next race.
#  *************************************************
# Begin
# The statement to read the file runners.txt
infile = open("runners.txt", "r")

def main():
# Initialisation for further use in the loop function.
    under30sumtime = 0
    under30time = 500
    under30name = ""
    under30age = 0
    under30cnt = 0
    s30to50sumtime = 0
    s30to50time = 500
    s30to50name = ""
    s30to50age = 0
    s30to50cnt = 0
    over50sumtime = 0
    over50time = 500
    over50name = ""
    over50age = 0
    over50cnt = 0
    cnt = 0
    disqualified = 0
    line = infile.readline()

# This is the function to loop the program to find the required solution.
    while line != "":
        name = (line).rstrip("\n")
        time = int(infile.readline())
        age = int(infile.readline())
        cnt += 1
# This is the section to take the qualified participants for the section ie. under 30 and total time less than 300.
        if age<30 and time <= 300:
            under30sumtime += time
            under30cnt += 1
            if time < under30time:
                under30age = age
                under30time = time
                under30name = name
# This is the section to take the qualified participants for the section ie. above 50 and total time less than 420.
        elif age >50 and time <= 420:
            over50sumtime += time
            over50cnt += 1
            if time < over50time:
                over50age = age
                over50time = time
                over50name = name
# This is the section to take the qualified participants for the section ie. under 50  and total time less than 360
        elif age >= 30 and time <= 360:
            s30to50sumtime += time
            s30to50cnt += 1
            if time < s30to50time:
                s30to50age = age
                s30to50time = time
                s30to50name = name
        line = infile.readline()

# Calculation Section
# This is the area of calculation of the average time of each section
    avgunder30time = under30sumtime / under30cnt
    avgs30to50time =s30to50sumtime / s30to50cnt
    avgover50time = over50sumtime / over50cnt
# this is the area of calculation of the number of disqulified participants
    disqualified = cnt - under30cnt -s30to50cnt -over50cnt


# Print section
# This is the section for the print.
    print("---------------UNDER 30---------------")
    print("Favourite Name  : ",under30name)
    print("Favourite Time  : ",under30time)
    print("Favourite Age   : ",under30age)
    print("Qualified       : ",under30cnt)
    print("Average Time    : ",format(avgunder30time, "4.1f"))
    print("---------------30 to 50---------------")
    print("Favourite Name  : ",s30to50name)
    print("Favourite Time  : ",s30to50time)
    print("Favourite Age   : ",s30to50age)
    print("Qualified       : ",s30to50cnt)
    print("Average Time    : ",format(avgs30to50time, "4.1f"))
    print("---------------Over 50---------------")
    print("Favourite Name  : ",over50name)
    print("Favourite Time  : ",over50time)
    print("Favourite Age   : ",over50age)
    print("Qualified       : ",over50cnt)
    print("Average Time    : ",format(avgover50time, "4.1f"))
    print("---------------Disqualified---------------")
    print("Disqualified    : ",disqualified)


main()
input()
#end

