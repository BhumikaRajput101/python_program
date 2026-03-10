#Custom Exception
class dobexception(Exception):
    pass

year = int(input ("Enter your birth year"))
age=2026-year
try :

 if age <= 30 and age>= 20:
    print("This is VALID so you can apply for the exam ")
 else: 
    raise dobexception()
except dobexception :

    print("sorry your age should be  between 20 and 30")
