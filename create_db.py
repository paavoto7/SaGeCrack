import sqlite3

with open("populate.sql") as sql:
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.executescript(sql.read())