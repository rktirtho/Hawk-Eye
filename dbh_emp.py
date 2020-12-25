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

    def save(self, id, name, email):
        """ This function is for insert a security officer into database. parameter is employee type."""
        cur = self.conn.cursor()
        query = "insert into security_officer (id, name,  email,  org_id) values (%s, %s, %s, %s)"
        cur.execute(query, (id, name,  email, 1))
        self.conn.commit()

    def update_account(self, id, username, password):
        cur = self.conn.cursor()
        cur.execute("update security_officer set username=%s, password=%s where id = %s",(username,password,id))
        self.conn.commit()

    def find_all(self):
        my_list = list()
        self.cur.execute("select * from security_officer")
        for data in self.cur:
            print(data)
            # (self, name, username, email, password, org_id, join_date, id=None, last_excess=None)
            emp = Employee(data[1], data[2], data[3],data[4], data[5], data[0], data[6])
            my_list.append(emp)
        return my_list

    def login(self, username, password):
        self.cur.execute("select username from security_officer where username=%s and binary password=%s",(username,password,id))

        if self.cur.fetchone() is not None:
            return True
        else:
            return False




test = EmployeeDBHelper()
# em = Employee("Shuvo Rahaman", "shrahaman", "shuvo@hawkeye.com", "qwert", 3, id=2456)
test.update_account(1234,"lina","3455")