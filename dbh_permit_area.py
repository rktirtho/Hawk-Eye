import mysql
from mysql.connector import (connection)
from cl_permit_area import PermitArea

class PermitAreaDbHelper:
    def __init__(self):
        print("Object Created")

    def get_conn(self):

        self.conn = mysql.connector.connect(
            user='root',
            password='12345678',
            host='127.0.0.1',
            database='hawk_eye'
        )
        return self.conn

    def add(self, person_id, area):
        conn = self.get_conn()
        cur = conn.cursor()
        query = "insert into permit_area (person_id, area) values (%s, %s)"
        cur.execute(query, (person_id, area))
        conn.commit()
        conn.close()

    def getAreaById(self, id):
        conn = self.get_conn()
        cur = conn.cursor()
        floors = list()
        cur.execute("select area from permit_area where person_id=%s",(id,))
        for i in cur.fetchall():
            floors.append(i[0])
        return floors



test = PermitAreaDbHelper()
data = test.getAreaById(3001)
for i in data:
    print(i)