import mysql
from mysql.connector import (connection)

class Monitoring():
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

    def add(self):
        conn = self.get_conn()
        cur = conn.cursor()
        query = "insert into monitoning ( person_id, area, isPermitted) values (%s, %s, %s)"
        cur.execute(query, (1, "Level 5", True))
        conn.commit()
        conn.close()

    def get_all(self):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from monitoning")
        data = cur.fetchall()
        conn.close()
        return data




mon = Monitoring()
mon.add()
all = mon.get_all()

for i in all:
    print(i)

