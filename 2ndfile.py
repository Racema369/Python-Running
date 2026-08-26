students={}

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("Press 1 ADD STUDENT")
    print("Press 2 FIND STUDENT")
    print("Press 3 CALCULATE GRADE")
    print("Press 4 UPDATE MARKS")
    print("Press 5 DELETE STUDENTS")
    print("Press 6 DISPLAY ALL STUDENTS")
    print("Press 7 EXIT")

    response=int(input("Enter the choice: "))

    def add_student():
        try:
            id=int(input("Enter student ID: "))
            name=input("Enter the student name: ")
            age=int(input("Enter the student age: "))
            if age<0:
                print("Age cannot be less than 0")
                return

            marks=float(input("Enter the student marks: "))
            if marks<0 or marks>100:
                print("Marks must be between 0 and 100")
                return
        except ValueError:
            print("Invalid Input!, Please enter number where required")
        else:
            students[id]={
                
                    "name":name,
                    "age":age,
                    "marks":marks
                }
               
            print("Student added successfully!!!")
        finally:
            print("Add operation completed")

    def find_student():
        try:
            id=int(input("Enter student ID to find student: "))
            if id not in students:
                print("Student ID does not exists")
                return
            student=students[id]
            print("\n STUDENT INFORMATION")
            print("ID: ",id)
            print("Name: ",student["name"])
            print("Age: ",student['age'])
            print("Marks: ",student["marks"])
            print("Grade: ",calculate_grade(student["marks"]))
        except ValueError:
            print("Invalid Input. Student ID must be number")
        finally:
            print("Find Operation is complete!!!")

    def calculate_grade(marks):
        if marks>=90:
            return "A"
        if marks>=80:
            return "B"
        if marks>=70:
            return "C"
        if marks>=60:
            return "D"
        else:
            return "F"

    def update_marks():
        try:
            id=int(input("Enter Student ID to update: "))
            if id not in students:
                print("Student ID does not exists")
                return

            new_marks=float(input("Enter the new marks: "))
            if new_marks<0 or new_marks>100:
                print("Marks must be between 0 and 100")
                return
            students[id]["marks"]=new_marks
            print("Student Marks is successfully updated!!!")
        except ValueError:
            print("Invalid Input. Marks should be in numbers")
        finally:
            print("Update operation is completed")

    def delete_students():
        try:
            id=int(input("Enter Student ID to delete student: "))
            if id not in students:
                print("Student ID does not exists")
                return
            del students[id]

            print("Student is successfully deleted")
        except ValueError:
            print("Invalid Input. Student ID must be number")
        finally:
            print("Delete Operation is completed")

    def display_all_students():
        if not students:
            print("No Students found!!!\n")
            return

        print("\n....ALL STUDENTS.....")
        for id,info in students.items():
            grade=calculate_grade(info["marks"])
            print("ID: ",id)
            print("Name: ",info["name"])
            print("Age: ",info["age"])
            print("Marks: ",info["marks"])
            print("Grade: ",grade)
            print("...................................")



    if response == 1:
        add_student()
    elif response == 2:
        find_student()

    elif response == 3:
        marks=float(input("Enter the marks: "))
        if marks<0 or marks>100:
            print("Marks must be between 0 and 100")
        else:
            print("Grade: ",calculate_grade(marks))

    elif response == 4:
        update_marks()
    elif response == 5:
        delete_students()
    elif response == 6:
        display_all_students()
    elif response ==7 :
        print("Thank you for using Student Management System")
        break
    else:
        print("Invalid menu option!!!. Please choose option between 1 to 7")

