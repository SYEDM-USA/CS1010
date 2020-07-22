#  ************************************************
#  CS1010 1003  am  Lab 1
#  Name: Muhammed Abubaker Syed
#  Class Code: 315
#  Purpose: The program will ask a user for a
#  name, hours worked and wage. It will use the input
#  to calculate and output the gross pay, taxes and
#  net pay.
#  *************************************************

#begin

#Initialize
TAXRATE = 0.12
MED_DEDUCT = 20

#INPUT
name = input("Enter Name")
hrs = int(input("Enter # of hours"))
WAGE = int(input("Enter Wage"))

#Process
grossPay = (hrs * WAGE)
tax = grossPay * TAXRATE
netPay = grossPay - (MED_DEDUCT + tax)

#Output
print("Name = ", name)
print("Gross = $" , format(grossPay, ".2f"))
print("Tax   = $" ,format(tax, ".2f"))
print("Netpay = $" , format(netPay, ".2f"))

#end
