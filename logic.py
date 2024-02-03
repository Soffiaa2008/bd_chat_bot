import sqlite3
class TaskManager:
    def __init__(self, database):
        self.database = database
        
    def create_table(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            id_user INTEGER
            )
            """)
            conn.commit()

    def add_task(self, user_id, name, description):
        con = sqlite3.connect(self.database)
        with con:
            con.execute('''INSERT INTO tasks (id_user, name, description) VALUES(?, ?, ?)''',(user_id, name, description))
            con.commit()
            
    def delete_task(self,name: str):
        con = sqlite3.connect(self.database)
        with con:
            con.execute(f'DELETE FROM tasks WHERE name = ?', (name,))
            con.commit()
        
def show_task(self, user_id):
    conn = sqlite3.connect(self.database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM tasks WHERE user_id = ?", (user_id,))
        return cur.fetchall()