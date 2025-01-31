import sqlite3

baza = sqlite3.connect("11b_skoleni.db")

cur = baza.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS  skolens(
    ID_skolens INT PRIMARY KEY,
    vards text,
    uzvards text,
    epasta text)""")

cur.execute("""CREATE TABLE IF NOT EXISTS prieksmeti(
    ID_prieksmets INT PRIMARY KEY,
    nosaukums text,
    skolena_id INT,
    FOREIGN KEY (skolena_id) REFERENCES skolens (ID_skolens)
    )""")


# num = int(input("Skolēna kartējas numurs: "))
# vard = input("Skolēna vārds:")
# uzv = input("Skolēna uzvārds: ")
# pasts = input("Skolēna epasta: ")
# saraksts = (num,vard,uzv,pasts)

# prieks = int(input("Priekšmeta numurs: "))
# nos = input("Priekšmeta nosaukums: ")
# skol = int(input("Skolēna numurs: "))
# prieksmet = (prieks,nos,skol)

# cur.execute("""INSERT INTO skolens(ID_skolens,vards,uzvards,epasta)VALUES(?,?,?,?)""",saraksts)
# cur.execute("""INSERT INTO prieksmeti(ID_prieksmets,nosaukums,skolena_ID)VALUES(?,?,?)""",prieksmet)

cur.execute("SELECT * FROM prieksmeti, skolens WHERE skolena_ID = skolens(ID_skolens)")

baza.commit()
cur.close()