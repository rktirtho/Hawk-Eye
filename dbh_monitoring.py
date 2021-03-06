import mysql
from mysql.connector import (connection)
from cl_monitoring import Monitoring, StrangerMonitoring
from cl_monitoring import Access
from cl_stranger import Stranger
from dbh_stranger import StrangerDbHelper
from dbh_person_reg import AuthorizedDbHelper

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
            values.append(per)
        return values



    def get_unauth_access(self):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute(
            "select DISTINCT permitted.id, permitted.name, permitted.org_id, permitted.image_id,  permitted.regestered_time ,monitoring.is_permitted from permitted inner join monitoring on permitted.id = monitoring.person_id and monitoring.is_permitted=0")
        for data in cur:
            per = Access(data[0], data[1], data[2], data[3], data[4])
            values.append(per)
        return values

    # def get_today(self):
    #     values = list()
    #     conn = self.get_conn()
    #     cur = conn.cursor()
    #     cur.execute(
    #         "select DISTINCT permitted.id, permitted.name, permitted.org_id, permitted.image_id,  permitted.regestered_time ,monitoring.is_permitted from permitted inner join monitoring on permitted.id = monitoring.person_id and monitoring.is_permitted=0  and DATE(`time`) = CURDATE()")
    #     for data in cur:
    #         per = Access(data[0], data[1], data[2], data[3], data[4])
    #         values.append(per)
    #     return values

    def get_yesterday(self):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT distinct person_id FROM monitoring where DATE(`time`) = CURDATE()-1")
        print(cur)
        for id in cur:
            auth_db = AuthorizedDbHelper()
            person = auth_db.find_one(id[0])
            values.append(person)
        return values

    def get_today(self):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT distinct person_id FROM monitoring where DATE(`time`) = CURDATE()")
        print(cur)
        for id in cur:
            auth_db = AuthorizedDbHelper()
            person = auth_db.find_one(id[0])
            values.append(person)
        return values

    def get_all(self):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT distinct person_id FROM monitoring")
        print(cur)
        for id in cur:
            auth_db = AuthorizedDbHelper()
            person = auth_db.find_one(id[0])
            values.append(person)
        return values

    def get_access_by_id(self, id):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from monitoring where person_id=%s order by time desc;", (id,))
        print(cur)
        for id in cur:
            mon = Monitoring(id[0],id[1],id[3],id[4], id[2])
            values.append(mon)
        return values

    def get_today_access_by_id(self, id):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from monitoring where person_id=%s and DATE(`time`) = CURDATE() order by time desc;", (id,))
        print(cur)
        for id in cur:
            mon = Monitoring(id[0],id[1],id[3],id[4], id[2])
            values.append(mon)
        return values

    def get_yesterday_access_by_id(self, id):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from monitoring where person_id=%s and DATE(`time`) = CURDATE()-1 order by time desc;", (id,))
        print(cur)
        for id in cur:
            mon = Monitoring(id[0],id[1],id[3],id[4], id[2])
            values.append(mon)
        return values

    def get_auth_access_by_id(self, id):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from monitoring where person_id=%s and is_permitted=1 order by time desc;", (id,))
        print(cur)
        for id in cur:
            mon = Monitoring(id[0],id[1],id[3],id[4], id[2])
            values.append(mon)
        return values

    def get_unauth_access_by_id(self, id):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from monitoring where person_id=%s and is_permitted=0 order by time desc;", (id,))
        print(cur)
        for id in cur:
            mon = Monitoring(id[0],id[1],id[3],id[4], id[2])
            values.append(mon)
        return values

    def count_today_employee(self):
        con = self.get_conn()
        cur = con.cursor()
        cur.execute("SELECT count(distinct person_id) FROM monitoring where area= '1st Floor' and  DATE(`time`) = CURDATE()")
        return cur.fetchone()




# m = MonitoringDbHelper()
# m.add(3001, "5th Floor", 1)
# values = m.get_auth_access_by_id(4001)
# for i in values:
#     print(i.get_time())

class StrangerMonitoringDatabaseHelper:
    def get_conn(self):

        self.conn = mysql.connector.connect(
            user='root',
            password='12345678',
            host='127.0.0.1',
            database='hawk_eye'
        )
        return self.conn

    def add(self, st_id, area):
        conn = self.get_conn()
        cur = conn.cursor()
        query = "insert into stranger_monitor ( st_id, area) values (%s, %s)"
        cur.execute(query, (st_id, area))
        conn.commit()
        conn.close()

    def get_all(self):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        st_db_helper = StrangerDbHelper()
        cur.execute("SELECT distinct st_id FROM stranger_monitor")
        print(cur)
        for id in cur:
            person = st_db_helper.get_stranger_by_id(id[0])
            values.append(person)
        return values

    def count_today_strangers(self):
        con = self.get_conn()
        cur = con.cursor()
        cur.execute("SELECT count(distinct st_id) FROM stranger_monitor where area= '1st Floor' and  DATE(`time`) = CURDATE()")
        data = cur.fetchone()
        return data

    # def get_all(self):
    #     monitors = list()
    #     conn = self.get_conn()
    #     cur = conn.cursor()
    #     cur.execute("select * from StrangerDatabaseHelper")
    #     data = cur.fetchall()
    #     print(data)
    #     for i in data:
    #         mon = Stranger(i[0], i[1],i[3],i[4],i[2])
    #         monitors.append(mon)
    #     conn.close()
    #     return monitors
    #
    # def get_one(self, id):
    #     conn = self.get_conn()
    #     cur = conn.cursor()
    #     cur.execute("select * from monitoring where id=%s", (id,))
    #     data = cur.fetchone()
    #     conn.close()
    #     return data

    def get_access_by_id(self, id):
        values = list()
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("select * from stranger_monitor where st_id=%s order by time desc;", (id,))
        print(cur)
        for id in cur:
            mon = StrangerMonitoring(id[0],id[1],id[2], id[3])
            print(id)
            values.append(mon)
        return values


# m =StrangerMonitoringDatabaseHelper()
# m.add(3001, "5th Floor", 1)
# values = m.get_all()
# for i in values:
#     print(i.get_image())


