import os

def student():
    name=input ('Enter student name :')
    roll=input ("Enter roll number:")
    marks=input("Enter marks:")
    my_file=open('student.txt','a')
    my_file.write(f"{name},{roll},{marks}\n")

def modify_student():
    roll_number = input("Enter roll number to modify: ")
    new_marks = input("Enter new marks: ")

    if not os.path.exists("student.txt"):
        print("No records found.\n")
        return

    with open("student.txt", "r") as file:
        data = file.readlines()

    found = False

    with open("student.txt", "w") as file:
        for line in data:
            parts = line.strip().split(",")

            if len(parts) != 3:
                file.write(line)
                continue

            name, roll, marks = parts

            if roll == roll_number:
                file.write(f"{name},{roll},{new_marks}\n")
                found = True
            else:
                file.write(line)

    if found:
        print("Record Modified Successfully!\n")
    else:
        print("Roll number not found!\n")

    
        

def Information():
    with open("student.txt", "r") as file:
        records = file.readlines()

    print("\nStudent Records:")
    print("-----------------")
    for record in records:
        name, roll, marks = record.strip().split(",")
        print(f"Name: {name}, Roll: {roll}, Marks: {marks}")
    print()

def main():
    while True:
    
        print('### Student Management System ###')
        print("Enter your choice :")
        print("1. Save New Information,")
        print("2.Modify The Record.")
        print("3.View The Information of Students.")
        print("4.Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue

        if choice==1:
          student()
        elif choice ==2:
          modify_student()
        elif choice == 3: 
            Information()
        elif choice== 4:
            print("Thank you!!!")
            break
        else: 
             print("Wrong choice! Enter your choice again.")
    
main()