from cl_Person import Person
import sqlite3
import datetime


class PersonDBHelper:

    def insert(person):
        conn = sqlite3.connect('hawk_eye')
        cur = conn.cursor()
        cur.execute('INSERT INTO reg_person(emp_id, name, org_id, regester_time) values (:emp_id, :name, :org_id, :regester_time)',
                    {
                        'emp_id' : person.get_id(),
                        'name' : person.get_name(),
                        'org_id' : person.get_org_id(),
                        'regester_time' : datetime.datetime.now()
                    })
        conn.commit()
        conn.close()

        print("inserted")

    def update(self):
        print("inserted")

    def getAll(self):
        conn = sqlite3.connect('hawk_eye')
        cur = conn.cursor()
        cur.execute("select * from reg_person")
        regs = cur.fetchall()
        for p in regs:
            print(p)
        conn.close()

    def getOne(self):
        print("inserted")

    def getById(self, id):
        print(id)

    def getByTime(self, time):
        print(time)


myP = Person(951, "Rejaul Karim", "AA-01")
PersonDBHelper.getAll(self=None);