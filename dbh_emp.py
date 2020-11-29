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

    def save(self, employee):
        """ This function is for insert a security officer into database. parameter is employee type."""
        cur = self.conn.cursor()
        query = "insert into security_officer (id, name, username, email, password, org_id) values (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (employee.get_id(), employee.get_name(), employee.get_username(), employee.get_email(), employee.get_password(), employee.get_org_id()))
        self.conn.commit()

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

    def login(self, username, password):
        self.cur.execute("select username from security_officer where username=%s and binary password=%s",(username,password))

        if self.cur.fetchone() is not None:
            return True
        else:
            return False




test = EmployeeDBHelper()
em = Employee("Shuvo Rahaman", "shrahaman", "shuvo@hawkeye.com", "qwert", 3, id=2456)
print(test.login("shrahaMan", 'Qwert'))