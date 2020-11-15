from mysql.connector import (connection)
# from object_model import Employee
import mysql
from cl_employee import Employee


class EmployeeDBHelper:
    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='12345678',
            host='127.0.0.1',
            database='hawk_eye'
        )
        self.cur = self.conn.cursor()

    # def connection(self):
    #     conn =
    #     return conn
    #

    def update_account(self, id, username, password):
        cur = self.conn.cursor()
        cur.execute("show tables")
        for tab in cur:
            print(tab)

    def find_all(self):
        my_list = list()
        self.cur.execute("select * from security_officer")
        for data in self.cur:
            print(data)
            # (self, name, username, email, password, org_id, join_date, id=None, last_excess=None)
            emp = Employee(data[1], data[2], data[3],data[4], data[5], data[0], data[6])
            my_list.append(emp)
        return my_list

