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
    file = open("Patient.bin" , "ab" )
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

# A method To Add A Doctors's Information
def addDoctor():
    did = input("\n\tEnter New Doctor ID : ")
    dname = input("\tEnter Doctor Name : ")
    dspec =  input("\tEnter Doctor Speciality : ")
    active = 1
    data = {did:[ dname , dspec , active ]}
    file = open("doctor.bin" , "ab")          
    pickle.dump(data, file )
    print(f"\n\t\tDoctor {dname} Added Succesfully!")
    file.close()
    file = open("appointment.bin" , "ab")
    data = {did:{"1PM":0,"2PM":0,"3PM":0,"4PM":0}}
    pickle.dump(data,file)
    file.close()


# A method To Get All Doctors's Information 
def getAllDoctors():
    doc = dict()
    file = open("doctor.bin" , "rb")
    try:
        while True :
            doc.update(pickle.load(file))
    except:
        pass
    file.close()
    return doc




# A method To View All Doctors's Information 
def viewAllDoctors():
    doc = getAllDoctors()
    for did ,info in doc.items():
        print("\n\tDoctor ID : " , did)
        print("\tDoctor Name : " , info[0])
        print("\tDoctor Speciality : " , info[1])
        print("\tDoctor Active : " ,"Active" if info[2]==1 else "Inactive")
        print("\t****************************************************")
        
# A method To Get All Appointments 
def getAllAppointments():
    app = dict()
    file = open("appointment.bin" , "rb")
    try:
        while True :
            app.update(pickle.load(file))
    except:
        pass
    file.close()
    return app


# A method To Mark Active/Inactive To A Doctor
def activeDoctor():
    did = input("\n\tEnter Doctor Id To mark A/In : ")
    doc = getAllDoctors()
    d = doc.get(did , False)
    if d:
        print(f"\n\tDoctor {d[0]} is " , "Active" if d[2]==1 else "InActive")
        if d[2]==1:
            ch = input("\tDo You Want To Mark Inactive (Y/n)")
            if ch in "Yy":
                d[2] = 0
                print(f"\tDoctor {d[0]} is InActive Now!")
            else:
                print(f"\n\tDoctor {d[0]} is still " , "Active" if d[2]==1 else "InActive")
        else:
            ch = input("\tDo You Want To Mark Active (Y/n)")
            if ch in "Yy":
                d[2] = 1
                print(f"\tDoctor {d[0]} is Active Now!")
            else:
                print(f"\tDoctor {d[0]} is still " , "Active" if d[2]==1 else "InActive")
        doc.update({did:d})  # ye line samaj nahi aai
        #print(doc)
        file = open("doctor.bin" , "wb")
        for did , info in doc.items():
            pickle.dump({did:info},file)
        file.close()
    else:
        print("\n\tDoctor Not Found")

#A Method to book An Appointment
def bookAnAppointment():
    pid = input("\n\tEnter Patient Id : ")
    pat = getAllPatients().get(pid,False)
    if pat:
        print("\n\tPatient Name : " , pat[0] )
        print("\tPatient Age : " , pat[1] )
        print("\tPatient Disease : " , pat[4] )
        did = input("\n\tEnter Doctor ID : ")
        doc = getAllDoctors().get(did,False)
        if doc:
            if doc[2]==1:
                print("\tDoctor Name : " , doc[0])
                print("\tDoctor Speciality : " , doc[1])
                doc = getAllAppointments() # ye samaj nahi aaya
                print(doc)
                app = doc.get(did)  # ye samaj nahi aaya
                print(app)
                print("\tAll Slots")
                i = 1
                li = []
                for k,v in app.items():
                    print(f"\t{i}.",k , "\tAvailable" if v==0 else "\tBooked")
                    i+=1
                    li.append(k)
                ch = int(input("\n\tSelect Your Slot(1-4) : ")) 
                if app.get(li[ch-1])==0:
                    app[li[ch-1]]=1
                    print("\n\tAppointment Booked!")
                else:
                    print("\n\tSlot Already Booked!")
                doc.update({did:app}) # ye samaj nahi aaya
                file = open("appointment.bin" , "wb")  # ye samaj nahi aaya
                for k,v in doc.items():
                    pickle.dump({k:v}, file)# ye samaj nahi aaya
                file.close()
                
                    

                
            else:
                print("\tDoctor is Inactive! Not Avilable Right Now !")
        else:
            print("\n\tDoctor Not Found! : ")
    else:
        print("\n\tPatient Not Found!")



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
    elif ch==5:
        addDoctor()
        input("\n\t\tPress Enter To Continue ...   ")
    elif ch==6:
        viewAllDoctors()
        input("\n\t\tPress Enter To Continue ...   ")
    elif ch==7:
        activeDoctor()
        input("\n\t\tPress Enter To Continue ...   ")
    elif ch==8:
        bookAnAppointment()
        input("\n\t\tPress Enter To Continue ...   ")
        
        
            

















