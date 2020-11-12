from mysql.connector import (connection)
# from object_model import Employee

class EmployeeDBHelper:

    def __init__(self):
        self.conn = connection.MySQLConnection(user='root', password='', host='127.0.0.1', database='hawk_eye')
        print("INIT")

    # def connection(self):
    #     conn =
    #     return conn
    #
    def login(self, username, password):
        return True


    def update_account(self, id, username, password):
        cur = self.conn.cursor()
        cur.execute("show tables")
        for tab in cur:
            print(tab)


ts=EmployeeDBHelper()
ts.update_account("df", "fdf", "fd")
