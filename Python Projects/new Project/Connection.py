import mysql.connector 

class DBConnect:
  def getConnection():
    conn =  mysql.connector.connect(
      host = "Localhost",
      password= "aaka0505",
      username = "root",
      port = "3306",
      database = "BankManagementSystem"
    )
    return conn
