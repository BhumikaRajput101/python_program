## Simple calculator

def add(num1 , num2):
    return num1+num2

def subs(num1,num2):
    return num1-num2

def multi(num1 , num2):
    return num1*num2

def divide(num1,num2):
    if num2==0:
        return "Can not be divided by zero"
         
    else : 
        return num1/num2
    
def get_started():
           
       print("1. Addition")
       print("2. Subtraction")
       print("3. Multiplication")
       print("4. Division")
    

       try:
        ch = int(input("Enter your choice: "))
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
       except ValueError:
           print("❌ Please enter valid numbers.")
           return

       if ch==1:
            print("Result:", add(num1, num2))
       elif ch== 2:
            print("Result:", subs(num1, num2))
       elif ch==3:
            print("Result:", multi(num1, num2))
       elif ch==4:
           print("Result:", divide(num1, num2))
       else:
           print("Invalid Choice reset the program")
    
print("Welcome to  the Simple Calculator ")
while True:
    choice =input("If you want to do some calculation \n Enter y/n :")
    if choice=='y':
        get_started()
    else: 
        break
print("Thank you ")