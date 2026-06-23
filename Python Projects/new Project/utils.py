from Connection import DBConnect
class accountHolder:
  def addAccount():
    conn = DBConnect.getConnection()

    cur = conn.cursor()
    conn.commit()
    cur.close()
    conn.close()