"""
Bank Mangement System
account_holder(accno, aname , aemail, amob , agender ,aadd , abalance  , atype active_status)
transaction(accno , credit , debit , balance , time_stamps)

1. Add New Account Holder
2. View Account Holder
3. Update Account Holder Information
4. Deposite Ammount
5. Withdraw Ammount
6. Freeze An Account
7. Transaction History
0. Exit
"""



# IMPORTING REQUIRED LIBRARIES
from utils import accountHolder






#  Dashboard

while True:
  print('''
      1. Add New Account Holder
      2. View Account Holder
      3. Update Account Holder Information
      4. Deposite Ammount / Withdraw Ammount
      5. Freeze An Account
      6. Transaction History
      0. Exit
  ''')
  ch = int(input("\tSelect Option : "))
  if  ch ==0:
      print("THANK YOU FOR USING OUR BANK MANAGEMENT SYSTEM! ")
      break
  elif ch==1:
    accountHolder.addAccount()
    input("\n Press Enter to Continue...")
  elif ch==2:
    accountHolder.view_accounts()
    input("\n Press Enter to Continue...")
  elif ch==3:
    accountHolder.update_account()  
    input("\n Press Enter to Continue...")
  elif ch==4:
    accountHolder.deposit_amount()
    input("\n Press Enter to Continue...")