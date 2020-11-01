import datetime
import sqlite3


def insert(employee):
    conn = sqlite3.connect('hawk_eye')
    cur = conn.cursor()
    cur.execute(
        "insert into employee (emp_id, name,username, email,password,last_excess,creation_time) values (:emp_id, :name, :username, :email, :password, :last_excess, :creation_time)",
        {
            'emp_id': employee.get_id(),
            'name': employee.get_name(),
            'username': employee.get_username(),
            'email': employee.get_email(),
            'password': employee.get_password(),
            'last_excess': str(datetime.datetime.now()),
            'creation_time': str(datetime.datetime.now())

        }
        )
    conn.commit()
    conn.close()


def update():
    conn = sqlite3.connect('hawk_eye')
    cur = conn.cursor()
    cur.execute('UPDATE employee set username=?, password=? where employee id=?')


def login(username, password):
    sql_select_query = """select username from employee where username=? and password=?"""
    conn = sqlite3.connect("hawk_eye")
    cur = conn.cursor()
    cur.execute(sql_select_query, (username, password,))
    records = cur.fetchall()
    conn.close()
    return records


def get_all():
    conn = sqlite3.connect('hawk_eye')
    cur = conn.cursor()
    cur.execute('select * from employee')
    for item in cur:
        print(item)


# insert()
get_all()
print(datetime.datetime.now())
