import mysql.connector

class OrganizationDbHelper:
    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='12345678',
            host='127.0.0.1',
            database='hawk_eye'
        )
        self.cur = self.conn.cursor()

        self.id
        self.name
        self.woner
        self.address
        self.reg_time


    def find_one(self):
        my_list = list()
        self.cur.execute("select * from organizations");
        for data in self.cur:
            my_list.append(data)
        return data;

    def find_one(self, id):
        self.cur.execute("select * from organizations where id= %s", (id,));
        data = self.cur.fetchone()
        return data




