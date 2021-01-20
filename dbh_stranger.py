import mysql
from mysql.connector import (connection)
from cl_stranger import Stranger

class StrangerDbHelper:

    def get_conn(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='12345678',
            host='127.0.0.1',
            database='hawk_eye'
        )
        return self.conn

    def add(self, id, image_id):
        conn = self.get_conn()
        cur = conn.cursor()
        quary = "insert into stranger(id, image) value (%s,%s)"
        cur.execute(quary,(id, image_id))
        print("add function execute")
        conn.commit()
        conn.close()

    def get_all_strangers(self):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from stranger")
        data = cur.fetchall()
        strangers = list()
        for item in data:
            stn = Stranger(item[0], item[1],item[3])
            strangers.append(item)
        return strangers

    def get_stranger_by_image_id(self, id):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from stranger where image=%s", (id,))
        data = cur.fetchone()
        snanger = Stranger(data[0], data[1],data[3])
        print(data)

        return snanger


# test = StrangerDbHelper()
# test.add(2, "test")
# data = test.get_all_stranger_by_image_id("st3")
# print(data.get_image())
#
# for i in data:
#     print(i)
