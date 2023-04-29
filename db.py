import mysql.connector


class Database:
    __table = "tasks"
    def __init__(self) -> None:
        self.__c = mysql.connector.connect(
            host="localhost",
            database="n19_todo_db",
            user="root",
            password="Qwerty!2345"
        )
    
    def get_all_tasks(self):
        query = f"SELECT * FROM {self.__table};"
        cursor = self.__c.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def make_done(self, id):
        query = f"UPDATE {self.__table} SET is_done = 1 WHERE id = {id};"
        self.__c.cursor().execute(query)
        self.__c.commit()
    

if __name__ == "__main__":
    d = Database()
    d.get_all_tasks()
