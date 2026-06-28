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
    print("\n\tAccno\t\tName\t\tAccType\t\tBalance\t\tStatus")
    print("\t" + '-' *70)
    for acc in data:
      print(f"\t{acc[0]}\t{acc[1]:<15}\t{acc[6]:<15}\t{acc[7]}\t{"Active " if acc[8]==1 else "Inactive"}")

    ch = int(input("\n\tEnter AccountNo For Complete Information or 0 to Exit : "))
    if ch != 0:     # 0 to exit work nahi kar raha
      sql = "Select * from account_holder where acc_no=" + str(ch) # ye line samaj nahi aai yha comma mai ku nai dia 
      cur.execute(sql)
      data = cur.fetchone()
      if cur.rowcount>0:
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
      else:
        print("\tA/c Not Found!")
    cur.close()
    conn.close()


  def update_account():
    conn = DBConnect.getConnection()
    cur = conn.cursor()
    sql = "SELECT * FROM account_holder"
    cur.execute(sql)
    data = cur.fetchall()
    print("\n\tAccno\t\tName\t\t\tEmail\t\t\t\tMobile")
    print("\t" + '-' *90)
    for acc in data:
      print(f"\t{acc[0]}\t{acc[1]:<20}\t{acc[2]:<30}\t{acc[3]}")

    ch = int(input("\n\tEnter AccountNo To Update or 0 to Exit : "))
    if ch != 0:
      sql = "Select * from account_holder where acc_no=" + str(ch) # ye line samaj nahi aai yha comma mai ku nai dia 
      cur.execute(sql)
      data = cur.fetchone()
      if cur.rowcount>0:
        print("\n\tA/c Number : ",data[0])
        print("\tA/c Holder Name : " , data[1])
        print("\tA/c Holder Old Email : " , data[2])
        email = input("Enter New Email Id : ")
        print("\tA/c Holder Old MobileNo : " , data[3])
        mob=input("Enter New Mobile Number : ")
        print("\tA/c Holder Gender : " , data[4])
        print("\tA/c Holder Address : " , data[5])
        print("\tA/c Holder Type : " , data[6])
        print("\tA/c Holder Balance : " , data[7])
        print("\tActive status  : " , "Active " if data[8]==1 else "Inactive")
        print("\t---------------------------------------------------")
        sql = f"Update account_holder set aemail = '{email}' , amob = '{mob}' where acc_no = {ch}"
        cur.execute(sql)
        if cur.rowcount>0:
          print("\n Email and Mobile Updated!")
        else:
          print("\n Failed To Update! ")
      else:
        print("\tA/c Not Found!") 
    conn.commit() 
    cur.close()
    conn.close()

  def deposit_amount():
    conn = DBConnect.getConnection()
    cur = conn.cursor()
    sql = "SELECT * FROM account_holder"
    cur.execute(sql)
    data = cur.fetchall()
    print("\n\tAccno\t\tName\t\tAccType\t\tBalance\t\tStatus")
    print("\t" + '-' *70)
    for acc in data:
      print(f"\t{acc[0]}\t{acc[1]:<15}\t{acc[6]:<15}\t{acc[7]}\t{"Active " if acc[8]==1 else "Inactive"}")

    ch = int(input("\n\tEnter AccountNo To Deposit/Withdrawl Amount or 0 to Exit : "))
    if ch != 0:
      sql = "select * from account_holder where acc_no = " +str(ch)
      cur.execute(sql)
      data = cur.fetchone()
      if cur.rowcount>0:
        c =int(input("\n\t1. Deposit\n\t2. Withdrawl\n\t0. Exit\n\tEnter Choice : "))
        if c!=0:
          if c ==1:
            amt = int(input("\n\tEnter Amount To Deposit : "))
            if amt>0:
              sql = f"update account_holder set abalance = abalance + {amt} where acc_no = " + str(ch)  
              cur.execute(sql) 
              print(f"\n\t{amt} Rupee Deposit Succesfully!")
            else:
              print("\n\tAmount Should Be Above 1 Rupee\n\t Transaction Cancelled!")

          elif c==2:
            amt = int(input("\n\tEnter Amount To Withdrawl : "))
            if amt>0:
              sql = f"update account_holder set abalance = abalance -   {amt} where acc_no = " + str(ch)
              cur.execute(sql) 
              print(f"\n\t{amt} Rupee Withdrawl Succesfully!")
            else:
              print("\n\tAmount Should Be Above 1 Rupee\n\t Transaction Cancelled!")
          else:
            print("\n\tWrong Entered!")
        else:
          print("\n\tTransaction Cancelled!")
      else:
        print("\tA/c Not Found!")

    conn.commit()
    cur.close()
    conn.close()
    accountHolder.view_accounts() 
