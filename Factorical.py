# factorical of a number
def factorial(a):
 
  if a <0:
    print("no factorial of a number")
  elif a==1:
    print("1")
  else:
        fact = 1
        for i in range(1, a + 1):
            fact *= i
        print (fact)
a=int(input("enter a number "))  
factorial(a)