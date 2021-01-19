import mysql
from mysql.connector import (connection)

class StrangerDbHelper:

    def get_conn(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='12345678',
            host='127.0.0.1',
            database='hawk_eye'
        )
        return self.conn

    def getAllStrangers(self):
        conn = self.get_conn()
        cur = conn.cursor()
