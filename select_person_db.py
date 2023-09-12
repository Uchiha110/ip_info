import sqlite3
from time import sleep


def select_person_db_func(column_name="", date="", oneall=""):
    if oneall.lower() == 'one':
        with sqlite3.connect("person_db.db") as con:
            cur = con.cursor()

            person = cur.execute(f"SELECT * FROM persons WHERE {column_name} = {date}")
            person = cur.fetchone()
            return person
    elif oneall.lower() == 'all':
        with sqlite3.connect("person_db.db") as con:
            cur = con.cursor()

            person = cur.execute("SELECT * FROM persons")
            person = cur.fetchall()
            return person
