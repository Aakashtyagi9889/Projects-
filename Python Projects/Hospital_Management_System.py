"""
Hotel Mangement System

Entity
- Patient           ( pid, pname , page , pgender , pcontact , problem )
- Doctor            ( did , dname , dspecility , active / inactive )    
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

# A method To View All Patient
def viewAllPatient():
    file = open("Patient.bin" , "rb")
    try:
        while True:
            data = pickle.load(file)
            for pid , info  in data.items():
                print("\n\t\t Patient ID = ", pid)
                print("\t Patient Name : ", info[0])
                print("\t Patient Age : ", info[1])
                print("\t Patient Gender : ", info[2])
                print("\t Patient Mobile No. : ", info[3])
                print("\t Patient Disease : ", info[4])
                print("\t------------------------------------")
    except:
        print("Here is your All Patient")
    file.close()

# A method To Get Patient Information
def getAllPatients():
    file = open("Patient.bin" , "rb")
    pat = dict()
    try:
        while True:
            pat.update(pickle.load(file))  # ye yaha ku hua samaj nahi aa raha hai 
    except:
        pass
    file.close()
    return pat

# A method To Update Patient's Information 
def updatePatient():
    pid = input("\n\tPatient ID To Update Info : ")
    pat = getAllPatients()
    res = pat.get(pid , False)      # ye kaise hua ye to bus  id lata hai isne to puri list print krdi 
    print(res)
    if res:
        print("\t Patient Name : ", res[0])
        print("\t Patient age : ", res[1])
        print("\t Patient Gender : ", res[2])
        print("\t Old Patient Contact : ", res[3])
        cont = input("\nEnter New Contact : ")
        print("\t Old Patient Problem : ", res[4])
        prob = input("\nEnter New Problem if Any : ")
        pat.update({pid: [res[0],res[1],res[2] , cont , prob]}) # ye dictionary ka update method hai kya 
        print(pat.get(pid))
        file = open("Patient.bin" , "wb")
        for pid,info in pat.items():
            pickle.dump({pid:info}, file)
        print("\n\tPatient Update Successfully ")
    else:
        print("\n\t No Patient Found on this ID ")


# A method To Delete a Patient
def deletePatient():
    pid = input("\n\tEnter Patient ID To Delete : ")  
    pat = getAllPatients()
    res = pat.get(pid , False)
    if res:
        print("\tPatient Name " , res[0])
        print("\tPatient Age " , res[1])
        print("\tPatient Gender " , res[2])
        print("\tPatient Contact " , res[3])
        print("\tPatient Problem " , res[4])
        ch  =  input("\n\tDo You Want to Delete (Y/N) : ")
        if ch in  "Yy":
            pat.pop(pid)
            file = open("Patient.bin" , "wb")
            for pid, info in pat.items():
                pickle.dump({pid:info}, file)
            file.close()
            print("\tPatient Deleted Succesfully ")
        else:
            print("Patient Information Not Deleted")
    else:
        print("\n\tPatient Not Found ")



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
    elif ch==2:
        viewAllPatient()
        input("\n\t\tPress Enter To Continue ...   ")
    elif ch==3:
        updatePatient()
        input("\n\t\tPress Enter To Continue ...   ")
    elif ch==4:
        deletePatient()
        input("\n\t\tPress Enter To Continue ...   ")

















