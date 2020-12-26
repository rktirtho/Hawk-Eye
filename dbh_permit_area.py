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



