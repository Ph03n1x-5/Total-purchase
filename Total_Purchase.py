def toFixed(value, digits):
    return "%.*f" % (digits, value)
def checkfloatdata() :
    while True :
        try :
            floatdatatype = float(input())
        except ValueError :
            print("Entered wrong data type - Re-enter positive numerical value")
            continue
        else :

            if floatdatatype < 0 :
                print("Entered 0 or a negative value - Re-enter positive numerical value")
                continue
            else :

                break
    return floatdatatype


filename = "Total_purchases_CDT_Output.txt"
outFile = open(filename, "w")

print("What is the cost of the fist item?")
cost1 = checkfloatdata()
print("What is the cost of the second item?")
cost2 = checkfloatdata()
print("What is the cost of the third item?")
cost3 = checkfloatdata()
print("What is the cost of the fouth item?")
cost4 = checkfloatdata()
print("What is the cost of the fifth item?")
cost5 = checkfloatdata()
print("What is the current tax? (example 0.04, 0.07, etc.)")
tax = checkfloatdata()

# Final output statements
outFile.write("===================================================================\n")
outFile.write("TOTAL PURCHASE RECEIPT / INFORMATION\n")
outFile.write("===================================================================\n")
outFile.write("PRICE FOR ITEM #01: $" + str(cost1)+ "\n")
outFile.write("PRICE FOR ITEM #02: $" + str(cost2)+ "\n")
outFile.write("PRICE FOR ITEM #03: $" + str(cost3)+ "\n")
outFile.write("PRICE FOR ITEM #04: $" + str(cost4)+ "\n")
outFile.write("PRICE FOR ITEM #05: $" + str(cost5)+ "\n")
outFile.write("===================================================================\n")

# Variables used to calculate the total and sales tax
subTotal = cost1 + cost2 + cost3 + cost4 + cost5
outFile.write("SUB TOTAL = $" + toFixed(subTotal,2)+ "\n")
salesTax = subTotal * tax
outFile.write("SALES TAX = $" + toFixed(salesTax,2)+ "\n")
total = subTotal + salesTax
outFile.write("TOTAL SALES = $" + toFixed(total,2)+ "\n")
outFile.close()
# END PROGRAM
