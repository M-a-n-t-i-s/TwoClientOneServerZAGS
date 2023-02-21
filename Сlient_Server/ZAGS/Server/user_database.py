import sqlite3

from enum import Enum


class Role(Enum):
    ADMIN = 1
    OPERATOR = 2
    ENGINEER = 3


class UserNotFoundError(Exception):
    pass


# noinspection SqlNoDataSourceInspection
class UserDatabase:

    def __init__(self, database: str = "user.sqLite"):
        self._db = database
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS user( 
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            role INTEGER NOT NULL,
            password TEXT NOT NULL);""")
            connection.commit()

    print("Server run")

    def get_users(self) -> list:
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            result = cursor.execute("""SELECT id, name, surname, role
                                           FROM user;""").fetchall()
        return [(id_, name, surname, Role[role].name)
                for id_, name, surname, role in result]

    def get_user_role(self, id_):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            try:
                role = cursor.execute("""SELECT role FROM user WHERE id=?""", (id_,)).fetchone()[0]
            except TypeError:
                raise UserNotFoundError
        return Role(role).name

    def add_user(self, name, surname, role, password):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO user (name, surname, role, password) VALUES (?,?,?,?)""",
                           (name, surname, Role[role].value, password))
            connection.commit()

    def delete_user(self, id_):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM user WHERE id = ?""", (id_,))
            connection.commit()

    def check_password(self, id_, password):
        with sqlite3.connect(self._db) as connection:
            cursor = connection.cursor()
            real_password = cursor.execute("""SELECT password FROM user WHERE id=?""", (id_,)).fetchone()[0]
        return password == real_password
