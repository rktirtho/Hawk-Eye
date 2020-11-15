import mysql.connector
from cl_organization import Organization

class OrganizationDbHelper:
    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='12345678',
            host='127.0.0.1',
            database='hawk_eye'
        )
        self.cur = self.conn.cursor()

    def find_all(self):
        my_list = list()
        self.cur.execute("select * from organizations")
        for data in self.cur:
            org = Organization(data[1],data[2],data[3],data[0],data[4])
            my_list.append(org)
        return my_list

    def find_one(self, id):
        self.cur.execute("select * from organizations where id= %s", (id,));
        data = self.cur.fetchone()
        org = Organization(data[1], data[2], data[3], data[0], data[4])
        return org


# test = OrganizationDbHelper()
# call = test.find_all()
# for c in call:
#     print(c)

