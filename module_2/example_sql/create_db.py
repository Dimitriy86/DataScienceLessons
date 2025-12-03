import sqlite3

def create_db():
    # Читаємо файл зі скриптом для створення БД
    with open('salary.sql', 'r') as file:
        sql = file.read()
    
    # Створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()

    # Виконуємо скрипт із файлу, який створить таблиці БД
    cur.executescript(sql)


if __name__ == "__main__":
    create_db()
