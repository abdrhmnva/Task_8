import sqlite3
from employee import Employee

class EmployeeDAO:
    def __init__(self):
        self.conn = sqlite3.connect("employee_db.sqlite")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                position TEXT,
                salary REAL,
                hire_date TEXT
            )
        """)
        self.conn.commit()

    def insert(self, employee: Employee):
        self.cursor.execute("""
            INSERT INTO employee (name, position, salary, hire_date)
            VALUES (?, ?, ?, ?)
        """, (employee.name, employee.position, employee.salary, employee.hire_date))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_by_id(self, id: int):
        self.cursor.execute("SELECT * FROM employee WHERE id = ?", (id,))
        row = self.cursor.fetchone()
        if row:
            return Employee(id=row[0], name=row[1], position=row[2], salary=row[3], hire_date=row[4])
        return None

    def get_all(self):
        self.cursor.execute("SELECT * FROM employee")
        rows = self.cursor.fetchall()
        return [Employee(id=row[0], name=row[1], position=row[2], salary=row[3], hire_date=row[4]) for row in rows]

    def update(self, employee: Employee):
        self.cursor.execute("""
            UPDATE employee
            SET name = ?, position = ?, salary = ?, hire_date = ?
            WHERE id = ?
        """, (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        self.conn.commit()

    def delete(self, id: int):
        self.cursor.execute("DELETE FROM employee WHERE id = ?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
