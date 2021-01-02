import mysql.connector
from cl_permitted import Permitted

class AuthorizedDbHelper:

    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='12345678',
            host='127.0.0.1',
            database='hawk_eye'
        )
        self.cur = self.conn.cursor()

    def save(self, permitted):
        cur = self.conn.cursor()
        print(permitted.get_name())
        print(permitted.get_id())
        print(permitted.get_image)
        print(permitted.get_org_id())
        # print(permitted.get)
        query = "insert into permitted(id, name, org_id, image_id) values (%s, %s, %s, %s)"
        cur.execute(query, (permitted.get_id(), permitted.get_name(), permitted.get_org_id(), permitted.get_image()))
        self.conn.commit()

    def find_all(self):
        auths = list()
        self.cur.execute("select * from permitted")
        for data in self.cur:
            auths.append(data)
        return auths

    def find_one(self, id):
        self.cur.execute("select permitted.id, permitted.name, permitted.org_id, permitted.image_id, organizations.name, permitted.regestered_time from permitted join organizations on permitted.org_id = organizations.id and permitted.id=%s", (id,))
        data = self.cur.fetchone()
        per =None
        try:
            per = Permitted(data[1], data[3], data[4], data[2],data[0])
        except:
            print("Error")
        return per

    def find_all_details(self):

        auths = list()
        query = "select permitted.id, permitted.name, permitted.org_id, permitted.image_id, organizations.name, permitted.regestered_time from permitted join organizations on permitted.org_id = organizations.id"
        self.cur.execute(query)
        for data in self.cur:
            per = Permitted(data[1], data[3], data[4], data[2],data[0])
            auths.append(per)
        return auths

    def get_auth_access(self):
        values = list()
        self.cur.execute("select DISTINCT permitted.id, permitted.name, permitted.org_id, permitted.image_id,  permitted.regestered_time ,monitoring.is_permitted from permitted inner join monitoring on permitted.id = monitoring.person_id and monitoring.is_permitted=1")
        for data in self.cur.executemany():
            per = Permitted(data[1], data[3], data[4], data[2],data[0])
            values.append(per)
        return values

    # def find_one_details(self, id):
    #     query = "select permitted.id, permitted.name, permitted.org_id, permitted.image_id, organizations.name, permitted.regestered_time from permitted join organizations on permitted.org_id = organizations.id where permitted.id=%s",(id,)
    #     self.cur.execute(query)
    #     data = self.cur.fetchone()
    #     per = Permitted(data[1], data[3], data[4], data[2],data[0])
    #     print(query)
    #
    #     return query

    def count_registered_employee(self):
        self.cur.execute("select count(id) from permitted")
        data = self.cur.fetchone()
        return data




dbh= AuthorizedDbHelper()
# per = Permitted("Zisan Khan", 'jisan', "", 4, 346)
# dbh.save(per)
li = dbh.find_one(1)
print(li)
# # print(li)
# # dbh.find_one(2)
#
# for t in li:
#     print(t.get_name())