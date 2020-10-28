import sqlite3
import datetime
import object_model


def insert(employee):
    conn = sqlite3.connect('hawk_eye')
    cur = conn.cursor()
    cur.execute("insert into employee (name,username, email,password,last_excess,creation_time) values (:name, :username, :email, :password, :last_excess, :creation_time)",
                {
                    'name': 'Shima Akter',
                    'username': 'shima123',
                    'email': 'shima@gmail.com',
                    'password': 'qwert',
                    'last_excess': str(datetime.datetime.now()),
                    'creation_time': str(datetime.datetime.now())

                }
                )
    conn.commit()
    conn.close()


def get_all():
    conn = sqlite3.connect('hawk_eye')
    cur = conn.cursor()
    cur.execute('select * from employee')
    for item in cur:
        print(item)


insert()
get_all()
print(datetime.datetime.now())
