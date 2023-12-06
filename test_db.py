"""from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import Session,sessionmaker
engine = create_engine('sqlite:///CmpTelega3.db', echo = True)
meta = MetaData()
session = Session(bind=engine)

UsersData = Table(
   'Users', meta,
   Column('id', Integer, primary_key = True,unique=True),
   Column('Phone', Integer),
   Column('tag',String,unique=True)
)

newToner = (Phone = 1)

dbsession.add(newToner)   
dbsession.commit()

meta.create_all(engine)
"""
"""
import sqlite3
sqlite_connection = sqlite3.connect('CmpTelega3.db')
conn = sqlite3.connect('CmpTelega3.db')


cursor = conn.execute(SELECT * FROM Users)

print(cursor[0])
conn.close()
"""

#
# import sqlite3
#
# conn = sqlite3.connect('CmpTelega3.db')
# cursor = conn.cursor()
# #cursor.execute("""CREATE TABLE IF NOT EXISTS Users(id INT PRIMARY KEY)""")
# #id = 4567
# #cursor.execute("""INSERT INTO Users () VALUES (47895)""")
# #conn.commit()
# #cursor.execute("""SELECT users_id""")
# #print(cursor.fetchall("SELECT INTO users_id"))
#
ids = 76213855
# cursor.execute('''SELECT * FROM Users''')
# for row in cursor.fetchall():
#     print(row)
#
#
# #cursor.execute(f"""INSERT INTO users SELECT users_id VALUE(?)({id})""")








"""
Метод проверки наличия id в базе

import sqlite3

def select_id():
    con = sqlite3.connect('data/CmpTelega3.db')
    cursor = con.cursor()
    cursor.execute('SELECT id FROM Users')
    rows = cursor.fetchall()
    inside = []
    for row in rows:
        a = [*row]
        inside.append(a[0])

    if ids in inside:
        print('da')
    else:
        print('net')
select_id()
"""




import sqlite3

"""
Метод с выбором действия

import sqlite3

action = input('Выберите действие: ')
def select_id(action):
    con = sqlite3.connect('data/CmpTelega3.db')
    cursor = con.cursor()
    cursor.execute('SELECT id FROM Users')
    rows = cursor.fetchall()
    inside = []
    for row in rows:
        a = [*row]
        inside.append(a[0])
    if action == '1':
        if ids in inside:
            print('da')
        else:
            print('net')
    elif action == '2':
        print(inside)
select_id(action)
"""


def check_id():
    ids = 762138557
    con = sqlite3.connect('data/CmpTelega3.db')
    cursor = con.cursor()
    cursor.execute('SELECT id FROM Users')
    rows = cursor.fetchall()
    inside = []
    for row in rows:
        a = [*row]
        inside.append(a[0])

    if ids in inside:
        return True
    else:
        return False

if check_id():
    print(True)
else:
    print("net")