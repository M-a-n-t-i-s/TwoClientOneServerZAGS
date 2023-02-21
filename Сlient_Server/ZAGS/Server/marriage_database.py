import sqlite3


class MarriageDatabase:

    def __init__(self, database: str = "ZAGS.sqLite"):
        self._db = database

        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS marriage (
                                id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
                                id_husband INTEGER NOT NULL,
                                id_wife INTEGER  NOT NULL,
                                date TEXT NOT NULL,
                                date_divorce TEXT
                                );""")
        connection.commit()

    def get_marriage(self) -> list:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            result = cursor.execute("""SELECT marriage.id, born.fio, woman.fio, marriage.date, marriage.date_divorce, marriage.id_husband, marriage.id_wife FROM marriage LEFT 
            JOIN born ON born.id=marriage.id_husband LEFT JOIN (SELECT fio, id from born) as woman ON woman.id=marriage.id_wife;""").fetchall()
        return result

    def delete_marriage(self, marriage_id) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM marriage WHERE id = ? """, (marriage_id,))
        connection.commit()

    def add_new_marriage(self, id_husband, id_wife, date) -> bool:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO marriage  (id_husband, id_wife , date) VALUES (?,?,?)""",
                           (int(id_husband), int(id_wife), date))
        connection.commit()

    def edit_marriage(self, id, id_husband, id_wife, date):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE marriage  SET id_husband = ?, date = ?, id_wife = ? WHERE id = ? """,
                           (int(id_husband), date, int(id_wife),  id))
        connection.commit()

    def edit_marriage_push_divorce(self, id, date_divorce):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""UPDATE marriage  SET date_divorce = ?  WHERE id = ? """, (date_divorce, id))
        connection.commit()

    def get_marriage_key(self, key, value) -> list:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            if key == 'id_husband':
                result = cursor.execute("""SELECT marriage.id, born.fio, woman.fio, marriage.date, marriage.date_divorce FROM marriage LEFT 
            JOIN born ON born.id=marriage.id_husband LEFT JOIN (SELECT fio, id from born) as woman ON woman.id=marriage.id_wife WHERE marriage.id_husband =?;""",
                                        (int(value),)).fetchall()
            elif key == 'id_wife ':
                result = cursor.execute("""SELECT marriage.id, born.fio, woman.fio, marriage.date, marriage.date_divorce FROM marriage LEFT 
            JOIN born ON born.id=marriage.id_husband LEFT JOIN (SELECT fio, id from born) as woman ON woman.id=marriage.id_wife WHERE marriage.id_wife =?;""",
                                        (int(value),)).fetchall()
            elif key == 'id':
                result = cursor.execute("""SELECT marriage.id, born.fio, woman.fio, marriage.date, marriage.date_divorce FROM marriage LEFT 
            JOIN born ON born.id=marriage.id_husband LEFT JOIN (SELECT fio, id from born) as woman ON woman.id=marriage.id_wife WHERE marriage.id =?;""",
                                        (int(value),)).fetchall()
            elif key == 'date':
                result = cursor.execute("""SELECT marriage.id, born.fio, woman.fio, marriage.date, marriage.date_divorce FROM marriage LEFT 
            JOIN born ON born.id=marriage.id_husband LEFT JOIN (SELECT fio, id from born) as woman ON woman.id=marriage.id_wife WHERE marriage.date =?;""",
                                        (value,)).fetchall()
            elif key == 'fio_husband':
                result = cursor.execute("""SELECT marriage.id, born.fio, woman.fio, marriage.date, marriage.date_divorce FROM marriage LEFT 
            JOIN born ON born.id=marriage.id_husband LEFT JOIN (SELECT fio, id from born) as woman ON woman.id=marriage.id_wife WHERE born.fio =?;""",
                                        (value,)).fetchall()
            elif key == 'date_divorce':
                result = cursor.execute("""SELECT marriage.id, born.fio, woman.fio, marriage.date, marriage.date_divorce FROM marriage LEFT 
            JOIN born ON born.id=marriage.id_husband LEFT JOIN (SELECT fio, id from born) as woman ON woman.id=marriage.id_wife WHERE marriage.date_divorce =?;""",
                                        (value,)).fetchall()
            elif key == 'fio_wife':
                result = cursor.execute("""SELECT marriage.id, born.fio, woman.fio, marriage.date, marriage.date_divorce FROM marriage LEFT 
             JOIN born ON born.id=marriage.id_husband LEFT JOIN (SELECT fio, id from born) as woman ON woman.id=marriage.id_wife WHERE woman.fio =?;""",
                                        (value,)).fetchall()
        return result
