import mysql
from mysql.connector import (connection)
from cl_monitoring import Monitoring
from cl_monitoring import Access

class MonitoringDbHelper:
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
        query = "insert into monitoring ( person_id, area, is_permitted) values (%s, %s, %s)"
        cur.execute(query, (person_id, area, isPermitted))
        conn.commit()
        conn.close()

    def get_all(self):
        monitors = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from monitoring")
        data = cur.fetchall()
        print(data)
        for i in data:
            mon = Monitoring(i[0], i[1],i[3],i[4],i[2])
            monitors.append(mon)
        conn.close()
        return monitors

    def get_one(self, id):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from monitoring where id=%s", (id,))
        data = cur.fetchone()
        conn.close()
        return data


    def get_auth_access(self):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select DISTINCT permitted.id, permitted.name, permitted.org_id, permitted.image_id,  permitted.regestered_time ,monitoring.is_permitted from permitted inner join monitoring on permitted.id = monitoring.person_id and monitoring.is_permitted=1")
        for data in cur:
            per = Access(data[0], data[1], data[2], data[3],data[4])
            values.append(per.get_name())
        return values





m = MonitoringDbHelper()

values = m.get_auth_access()
for i in values:
    print(i)




