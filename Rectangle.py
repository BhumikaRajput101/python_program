# Area and Perimeter of rectangle
class Rectangle:
    def inputl ( self):
        self.length=int(input('enter lenght:'))
        self.breadth=int(input('enter breadth:'))

    def perimetre(self):
       r.inputl()
       print("perimetre of  rectangle")
       print( 2*(self.length+self.breadth))


    def area(self):
        r.inputl()
        print("Area of Rectangle")
        print(self.length*self.breadth)
        
r=Rectangle()

        
while True :
    a=input("Do you want to continue:").lower()
    if a=='yes':
        choice=(input("Enter 'p' to find Perimeter and 'a' to find area :")).lower()
        if choice=='a':
         r.area()
        elif choice=='p':
           r.perimetre()
        else: 
         print("wrong Input ")
   
    else: 
       break
    

   