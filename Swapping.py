#Swap two numbers without using a third variable.
a = int(input("Enter 1st Number:"))
b = int(input("Enter 2nd Number:"))
print("Number before Swapping:",a,b)
a = a + b
b = a - b
a = a - b

print("Number after Swapping:",a,b)
