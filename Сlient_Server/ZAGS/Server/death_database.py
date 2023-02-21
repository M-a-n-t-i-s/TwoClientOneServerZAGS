import sqlite3


class DeathDatabase:

    def __init__(self, database: str = "ZAGS.sqLite"):
        self._db = database

        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS death (
                                id INTEGER  NOT NULL PRIMARY KEY,
                                date TEXT NOT NULL,
                                place TEXT NOT NULL,
                                description TEXT);""")
        connection.commit()

    def delete_death(self, death_id) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM death WHERE id=? """, (death_id,))
        connection.commit()

    def get_death(self) -> list:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            result = cursor.execute("""SELECT death.id,  death.date, death.place, death.description, born.fio FROM 
            death LEFT JOIN born on death.id=born.id;""").fetchall()
        return result

    def get_death_key(self, key, value) -> list:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            if key == 'place':
                result = cursor.execute("""SELECT death.id,  death.date, death.place, death.description, born.fio 
                FROM death LEFT JOIN born on death.id=born.id WHERE  death.place = ?;""",
                                        (value,)).fetchall()
            elif key == 'id':
                result = cursor.execute("""SELECT death.id,  death.date, death.place, death.description, born.fio 
                FROM death LEFT JOIN born on death.id=born.id WHERE  death.id = ?;""",
                                        (int(value),)).fetchall()
            elif key == 'date':
                result = cursor.execute("""SELECT death.id,  death.date, death.place, death.description, born.fio 
                FROM death LEFT JOIN born on death.id=born.id WHERE  death.date = ?;""",
                                        (value,)).fetchall()
            elif key == 'fio':
                result = cursor.execute("""SELECT death.id,  death.date, death.place, death.description, born.fio 
                FROM death LEFT JOIN born on death.id=born.id WHERE  born.fio = ?;""",
                                        (value,)).fetchall()
        return result

    def add_new_death(self, id, date, place, description) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO death (id, date, place, description) VALUES (?,?,?,?);""",
                           (int(id), date, place, description))
        connection.commit()

    def edit_death(self, death_id, new_date, new_place, new_description):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE death SET date = ?, place = ?, description = ? WHERE id = ? """,
                           (new_date, new_place, new_description, death_id))
        connection.commit()
