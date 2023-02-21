import sqlite3


class BornDatabase:

    def __init__(self, database: str = "ZAGS.sqLite"):
        self._db = database

        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS born (
                                id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
                                fio TEXT NOT NULL,
                                date TEXT NOT NULL,
                                gender TEXT NOT NULL,
                                id_parents INTEGER );""")
        connection.commit()

    def get_born(self) -> list:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            result = cursor.execute("""SELECT born.id, born.fio, born.date, born.gender,born.id_parents, death.date FROM born LEFT 
            JOIN death ON born.id=death.id;""").fetchall()
        return result

    def delete_born(self, born_id) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM born WHERE id=? """, (born_id,))
            cursor.execute("""DELETE FROM death WHERE id=? """, (born_id,))
        connection.commit()

    def add_new_born(self, fio, date, gender, id_parents) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO born (fio, date, gender, id_parents) VALUES (?,?,?,?)""",
                           (fio, date, gender, int(id_parents)))
        connection.commit()

    def edit_born(self, id, fio, date, gender, id_parents):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE born SET fio = ?, date = ?, gender = ?, id_parents = ? WHERE id = ? """,
                           (fio, date, gender, int(id_parents), id))
        connection.commit()

    def get_born_key(self, key, value) -> list:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            if key == 'gender':
                result = cursor.execute("""SELECT born.id, born.fio, born.date, born.gender,born.id_parents, death.date FROM born LEFT 
            JOIN death ON born.id =death.id WHERE born.gender =?;""",
                                        (value,)).fetchall()
            elif key == 'fio':
                result = cursor.execute("""SELECT born.id, born.fio, born.date, born.gender,born.id_parents, death.date FROM born LEFT 
            JOIN death ON born.id =death.id WHERE born.fio =?;""",
                                        (value,)).fetchall()
            elif key == 'id':
                result = cursor.execute("""SELECT born.id, born.fio, born.date, born.gender,born.id_parents, death.date FROM born LEFT 
            JOIN death ON born.id =death.id WHERE born.id =?;""",
                                        (int(value),)).fetchall()
            elif key == 'date':
                result = cursor.execute("""SELECT born.id, born.fio, born.date, born.gender,born.id_parents, death.date FROM born LEFT 
            JOIN death ON born.id =death.id WHERE born.date =?;""",
                                        (value,)).fetchall()
            elif key == 'id_parents':
                result = cursor.execute("""SELECT born.id, born.fio, born.date, born.gender,born.id_parents, death.date FROM born LEFT 
            JOIN death ON born.id =death.id WHERE born.id_parents =?;""",
                                        (int(value),)).fetchall()
            elif key == 'death_date':
                result = cursor.execute("""SELECT born.id, born.fio, born.date, born.gender,born.id_parents, death.date FROM born LEFT 
            JOIN death ON born.id =death.id WHERE death.date =?;""",
                                        (value,)).fetchall()
            elif key == 'place':
                result = cursor.execute("""SELECT born.id, born.fio, born.date, born.gender,born.id_parents, death.date FROM born LEFT 
            JOIN death ON born.id =death.id WHERE death.place =?;""",
                                        (value,)).fetchall()
        return result
