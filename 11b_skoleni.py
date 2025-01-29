import sqlite3

baza = sqlite3.connect("11b_skoleni.db")

cur = baza.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS  skolens(
    ID_skolens INT PRIMARY KEY,
    vards text,
    uzvards text,
    epasta text)""")

num = int(input("Skolēna kartējas numurs: "))
vard = input("Skolēna vārds:")
uzv = input("Skolēna uzvārds: ")
pasts = input("Skolēna epasta: ")
saraksts = (num,vard,uzv,pasts)

cur.execute("""INSERT INTO skolens(ID_skolens,vards,uzvards,epasta)VALUES(?,?,?,?)""",saraksts)

baza.commit()
cur.close()