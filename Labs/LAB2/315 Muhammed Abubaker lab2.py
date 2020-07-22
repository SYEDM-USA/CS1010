#  ************************************************
#  CS1010  Lab 2
#  Name :  315 MUHAMMED ABUBAKER
#  Purpose: The program will ask a user for
#  the amount of apples and oranges purchased by
#  the pound and produce a receipt for the purchase.
#  *************************************************
#begin

#initialize
APPLES=1.25
ORANGES=1.75
SALESTAX=0.07

#input section
numApples = int(input("Enter # of Apples"))
numOranges = int(input("Enter # of Oranges"))

#Calculation
apples = numApples*APPLES
oranges = numOranges*ORANGES
Subtotal = (apples + oranges)
Tax = Subtotal*SALESTAX
Cost = Subtotal+Tax

#Output Section
print("THE BG Fruit Receipt")
print("Apples=", format(apples,".2f"))
print("Oranges=", format(oranges,".2f"))
print("Subtotal=", format(Subtotal,".2f"))
print("Tax=", format(Tax,".2f"))
print("Cost", format(Cost,".2f"))

input()
#end


