"""
Hotel Mangement System

Entity
- Patient
- Doctor
- Appointment

1. Add Patient Information
2. View All Patient
3. Update Pateint Information
4. Delete Patient 
5. Add Doctor Information
6. View All Doctors Information
7. Active / Inactive Doctor
8. Book An Appointment
9. View All Apointments 
0. Exit
====================================================================================================
"""
#Importing Required Libraries
import pickle





# A Method  To Add Patient Information
def addPatient():
    pid = input("\nEnter Patient ID : ")
    pname = input("Enter Patient Name : ")
    page = input("Enter Patient Age : ")
    pgender = input("Enter Patient Gender : " )
    pmob = input("Enter Patient Mobile No : ")
    pdisease = input("Explain Disease / Problem : ")
    data = {pid : [pname , page , pgender , pmob , pdisease ]}
    file = open("patient.bin" , "ab" )
    pickle.dump(data , file)
    file.close
    print("\n\t\tPatient Added Succesfully ")





#Dashboard
while True:
    print("\n \t \t \t Hospital Management System")
    print("""
        1. Add Patient Information
        2. View All Patient
        3. Update Pateint Information
        4. Delete Patient 
        5. Add Doctor Information
        6. View All Doctors Information
        7. Active / Inactive Doctor
        8. Book An Appointment
        9. View All Apointments 
        0. Exit """)

    ch = int(input("\n\tEnter Your Choice : "))
    if ch == 0:
        print("\n\t\tBye Bye Admin! :)")
        break
    elif ch==1:
        addPatient()
        input("\n\t\tPress Enter To Continue ...   ")

















