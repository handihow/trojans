import sqlite3


class Database:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS astronomical_objects (
                                            id INTEGER PRIMARY KEY,
                                            name TEXT NOT NULL UNIQUE,
                                            pos_x REAL NOT NULL,
                                            pos_y REAL NOT NULL,
                                            pos_z REAL NOT NULL,
                                            radius REAL NOT NULL,
                                            color TEXT NOT NULL,
                                            mass REAL NOT NULL,
                                            velocity_x REAL NOT NULL,
                                            velocity_y REAL NOT NULL,
                                            velocity_z REAL NOT NULL,
                                            trail INTEGER NOT NULL,
                                            simulate INTEGER NOT NULL)''')
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM astronomical_objects")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, pos_x, pos_y, pos_z, radius, color, mass, velocity_x, velocity_y, velocity_z, trail,
               simulate):
        self.cur.execute("INSERT INTO astronomical_objects VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (name, pos_x, pos_y, pos_z, radius, color, mass, velocity_x, velocity_y, velocity_z, trail,
                          simulate))
        self.conn.commit()

    def remove(self, unique_number):
        self.cur.execute("DELETE FROM astronomical_objects WHERE id=?", (unique_number,))
        self.conn.commit()

    def update(self, unique_number,
               name, pos_x, pos_y, pos_z, radius, color, mass, velocity_x, velocity_y, velocity_z, trail, simulate):
        self.cur.execute('''UPDATE astronomical_objects SET 
                                name = ?, 
                                pos_x = ?, 
                                pos_y = ?, 
                                pos_z = ?,
                                radius = ?,
                                color = ?, 
                                mass = ?,
                                velocity_x = ?,
                                velocity_y = ?,
                                velocity_z = ?,
                                trail = ?,
                                simulate = ? WHERE id = ?''',
                         (name, pos_x, pos_y, pos_z, radius, color, mass, velocity_x, velocity_y, velocity_z, trail,
                          simulate, unique_number))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


