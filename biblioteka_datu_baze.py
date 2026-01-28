import sqlite3

datu_baze = sqlite3.connect("biblioteka.db")
kursor = datu_baze.cursor()

kursor.execute('''
    CREATE TABLE IF NOT EXISTS gramatas (
        id_gramata INTEGER PRIMARY KEY AUTOINCREMENT,
        nosaukums TEXT,
        autors TEXT,
        izdošanas_gads INTEGER
    )
''')
kursor.execute('''
    CREATE TABLE IF NOT EXISTS lasitaji (
        id_lasitajs INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT,
        uzvards TEXT,
        epasts TEXT
    )
''')
kursor.execute('''
    INSERT INTO lasitaji (vards, uzvards, epasts) VALUES
    ('Jānis', 'Bērziņš', 'janis@example.com'),
    ('Anna', 'Ozoliņa', 'anna@example.com'),
    ('Pēteris', 'Kalniņš', 'peteris@example.com')
''')
kursor.execute('''
    INSERT INTO gramatas (nosaukums, autors, izdošanas_gads) VALUES
    ('Grāmata 1', 'Autors 1', 2020),
    ('Grāmata 2', 'Autors 2', 2021),
    ('Grāmata 3', 'Autors 3', 2022)
''')
kursor.execute('''
    CREATE TABLE IF NOT EXISTS aizdevumi (
        id_aizdevums INTEGER PRIMARY KEY AUTOINCREMENT,
        id_gramata INTEGER,
        id_lasitajs INTEGER,
        aizdevuma_datums TEXT,
        atgrieziena_datums TEXT,
        FOREIGN KEY (id_gramata) REFERENCES gramatas (id_gramata),
        FOREIGN KEY (id_lasitajs) REFERENCES lasitaji (id_lasitajs)
    )
''')
kursor.execute('''
    INSERT INTO aizdevumi (id_gramata, id_lasitajs, aizdevuma_datums, atgrieziena_datums) VALUES
    (1, 1, '2023-01-01', '2023-01-15'),
    (2, 2, '2023-02-01', '2023-02-15'),
    (3, 3, '2023-03-01', '2023-03-15')
''')

kursor.execute('''SELECT vards, uzvards, aizdevuma_datums, atgrieziena_datums,nosaukums,autors,izdošanas_gads
               FROM aizdevumi JOIN lasitaji ON aizdevumi.id_lasitajs = lasitaji.id_lasitajs
               JOIN gramatas ON aizdevumi.id_gramata = gramatas.id_gramata''')
aizdevumi = kursor.fetchall()
print("Vārds, Uzvārds, Aizdevuma Datums, Atgrieziena Datums, Nosaukums, Autors, Izdošanas Gads")
for aizdevums in aizdevumi:
    print(aizdevums)

kursor.close()
datu_baze.commit()
datu_baze.close()