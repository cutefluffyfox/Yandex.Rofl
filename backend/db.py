import sqlite3
from pandas import read_excel


class DB:
    def __init__(self):
        conn = sqlite3.connect('crock.db', check_same_thread=False)
        self.conn = conn

    def get_connection(self):
        return self.conn

    def __del__(self):
        self.conn.close()


class UsersModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             user_name VARCHAR(50),
                             password_hash VARCHAR(128)
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (user_name, password_hash) 
                          VALUES (?,?)''', (user_name, password_hash))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id),))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password_hash):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = ? AND password_hash = ?",
                       (user_name, password_hash))
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)


class ProblemsTable:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS problems 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             problem_id VARCHAR(30),
                             callbackmemo TEXT,
                             reply TEXT,
                             description TEXT
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, problem_id, callbackememo, reply, description):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM problems WHERE problem_id = ?", (problem_id,))
        row = cursor.fetchone()

        if row is None:
            cursor.execute('''INSERT INTO problems 
                            (problem_id, callbackmemo, reply, description) 
                            VALUES (?,?,?,?)''', (problem_id, callbackememo, reply, description))

        else:
            cursor.execute('''UPDATE problems
                              SET callbackmemo = ?,
                                  reply = ?,
                                  description = ? 
                              WHERE problem_id = ?''', (callbackememo, reply, description, problem_id))

        cursor.close()
        self.connection.commit()

    def get(self, problem_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM problems WHERE problem_id = ?", (problem_id,))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM problems")
        rows = cursor.fetchall()
        return rows

    def delete(self, problem_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM problems WHERE problem_id = ?''', (problem_id,))
        cursor.close()
        self.connection.commit()


def add_data_from_excel(path):
    db = DB()
    problem_table = ProblemsTable(db.get_connection())
    problem_table.init_table()

    excel = read_excel(path)
    case_nums = list(excel['Номер кейса'])
    callbacks = list(excel['CALLBACKMEMO'])
    replies = list(excel['Решение'])
    descriptions = list(excel['Подробное описание'])

    for _ in range(len(excel)):
        case_num = case_nums.pop(0)
        callback = callbacks.pop(0)
        reply = replies.pop(0)
        description = descriptions.pop(0)

        if all(map(lambda x: type(x) != float, [case_num, reply, description])):
            problem_table.insert(case_num, callback, reply, description)
            print(_)


def get_results(problems_id: list):
    db = DB()
    problem_table = ProblemsTable(db.get_connection())
    res = {}

    for problem_id in problems_id:
        data = problem_table.get(problem_id)
        res[problem_id] = {'CALLBACKMEMO': data[2],
                           'answer': data[3],
                           'description': data[4]}

    return str(res)
