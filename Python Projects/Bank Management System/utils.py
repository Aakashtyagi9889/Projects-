from Connection import DBConnect
class accountHolder:
  def addAccount():
    conn = DBConnect.getConnection()
    cur = conn.cursor()
    
    name = input("Enter Account Holder Name : ")
    email = input("Enter Email ID : ")
    mob = input("Enter Mobile Number : ")
    gender = input("Enter A/c Holder Gender : ")
    address = input("Enter A/c Holder Address : ")
    print("Select A/c Type : ")
    type = input("1.Saving A/c \n2.Current A/c\nEnter Choice : ")
    type = 'Saving' if type == '1' else 'Current'
    print(type) 
    balance  = input("Enter Opening Balance : ")
    sql = "insert into account_holder(aname , aemail , amob ,agender, aadd, atype , abalance)value(%s,%s,%s,%s,%s,%s,%s)"
    data = (name,email,mob,gender,address,type,balance)
    cur.execute(sql,data)
    if cur.rowcount>0:
      print("\n\tNew Account Holder Added to the Database!")
    else:
      print("\n\tFailed to Add A New Account")
    conn.commit()
    cur.close()
    conn.close()

  def view_accounts():
    conn = DBConnect.getConnection()
    cur = conn.cursor()
    sql = "SELECT * FROM account_holder"
    cur.execute(sql)
    data = cur.fetchall()
    print("\n\tAccno\t\tName\t\tType\t\tBalance\t\tStatus")
    print("\t" + '-' *70)
    for acc in data:
      print(f"\t{acc[0]}\t{acc[1]:<15}\t{acc[6]:<15}\t{acc[7]}\t{"Active " if acc[8]==1 else "Inactive"}")

    ch = int(input("\n\tEnter AccountNo For Complete Information or 0 to Exit : "))
    if ch != 0:     # 0 to exit work nahi kar raha
      sql = "Select * from account_holder where acc_no=" + str(ch) # ye line samaj nahi aai yha comma mai ku nai dia 
      cur.execute(sql)
      data = cur.fetchone()
      print("\n\tA/c Number : ",data[0])
      print("\tA/c Holder Name : " , data[1])
      print("\tA/c Holder Email : " , data[2])
      print("\tA/c Holder MobileNo : " , data[3])
      print("\tA/c Holder Gender : " , data[4])
      print("\tA/c Holder Address : " , data[5])
      print("\tA/c Holder Type : " , data[6])
      print("\tA/c Holder Balance : " , data[7])
      print("\tActive status  : " , "Active " if data[8]==1 else "Inactive")
      print("\t---------------------------------------------------")
      
      

    cur.close()
    conn.close()

      