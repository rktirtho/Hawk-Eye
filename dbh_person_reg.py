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

    def find_all(self):
        auths = list()
        self.cur.execute("select * from permitted")
        for data in self.cur:
            auths.append(data)
        return auths

    def find_one(self, id):
        self.cur.execute("select * from permitted")
        query = "select permitted.id, permitted.name, permitted.org_id, permitted.image_id, organizations.name, permitted.regestered_time from permitted join organizations on permitted.org_id = organizations.id and permitted.id = 1 "

        for data in self.cur:
            print(data)

    def find_all_details(self):

        auths = list()
        query = "select permitted.id, permitted.name, permitted.org_id, permitted.image_id, organizations.name, permitted.regestered_time from permitted join organizations on permitted.org_id = organizations.id"
        self.cur.execute(query)
        for data in self.cur:
            per = Permitted(data[1], data[3], data[4], data[2],data[0])
            auths.append(per)
        return auths


# dbh= AuthorizedDbHelper()
# li = dbh.find_all_details()
# # print(li)
# # dbh.find_one(2)
#
# for t in li:
#     print(t.get_name())