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

    def add(self, person_id, area, isPermitted):
        conn = self.get_conn()
        cur = conn.cursor()
        query = "insert into monitoring ( person_id, area, isPermitted) values (%s, %s, %s)"
        cur.execute(query, (person_id, area, isPermitted))
        conn.commit()
        conn.close()

    def get_all(self):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from monitoring")
        data = cur.fetchall()
        conn.close()
        return data

    def get_one(self, id):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from monitoring where id=%s", (id,))
        data = cur.fetchone()
        conn.close()
        return data




mon = Monitoring()

all = mon.get_one(2)

print(all)

