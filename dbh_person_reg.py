import mysql.connector


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
        for data in self.cur:
            print(data)

    # def find_all_details(self):
    #     auths = list()
    #     self.cur.execute("select permitted.name, permitted.org_id, permitted.image_id, organizations.name inner join q")
    #

dbh= AuthorizedDbHelper()
li = dbh.find_all()
print(li)
# dbh.find_one(2)
for t in li:
    if 'Rejaul Karim' in t[1]:
        print("Found", t[2])
    else:
        print('Not Found')