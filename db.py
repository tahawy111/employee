import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
    `id` INT PRIMARY KEY,
    `name` TEXT,
    `age` TEXT,
    `job` TEXT,
    `email` TEXT,
    `gender` TEXT,
    `mobile` TEXT,
    `address` TEXT,
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, name, age, job, email, gender, mobile, address):
        self.cur.execute("insert into employees values(NULL,?,?,?,?,?,?,?)",
                         (name, age, job, email, gender, mobile, address))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("delete from employees where id=?", (id))
        rows = self.cur.fetchall()

    def update(self, id, name, age, job, email, gender, mobile, address):
        self.cur.execute(
            "update employees ser name=?,age=?,job=?,email=?,gender=?,mobile=?,address=? where id=?", (name, age, job, email, gender, mobile, address, id))
        self.con.commit()
