from passlib.hash import pbkdf2_sha256
from sqlite3 import connect
from pandas import read_excel


class DB:
    def __init__(self):
        conn = connect('../database/crock.db', check_same_thread=False)
        self.conn = conn

    def get_connection(self):
        return self.conn

    def __del__(self):
        self.conn.close()


class UsersTable:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             login VARCHAR(25),
                             user_name VARCHAR(30),
                             password_hash VARCHAR(100)
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, login, user_name, password):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (login, user_name, password_hash) 
                          VALUES (?,?,?)''', (login, user_name, pbkdf2_sha256.hash(password)))
        cursor.close()
        self.connection.commit()

    def get(self, login):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE login = ?", (str(login),))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows

    def exists(self, login):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE login = ?",
                       (login, ))
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)

    def check_password(self, login, password):
        row = self.get(login)
        answer = 'error'

        if row and pbkdf2_sha256.verify(password, row[-1]):
            answer = 'success'

        return answer


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


class CleanTable:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS clear 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             problem_id VARCHAR(30),
                             description TEXT,
                             vector BLOB
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, problem_id, description, vector):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM clear WHERE problem_id = ?", (problem_id,))
        row = cursor.fetchone()

        if row is None:
            cursor.execute('''INSERT INTO clear 
                            (problem_id, description, vector) 
                            VALUES (?,?,?)''', (problem_id, description, vector))

        else:
            cursor.execute('''UPDATE clear
                              SET description = ? ,
                              vector = ?
                              WHERE problem_id = ?''', (description,
                                                        vector,
                                                        problem_id))
        cursor.close()
        self.connection.commit()

    def get(self, problem_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM clear WHERE problem_id = ?", (problem_id,))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM clear")
        rows = cursor.fetchall()
        return rows

    def delete(self, problem_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM clear WHERE problem_id = ?''', (problem_id,))
        cursor.close()
        self.connection.commit()


class DataToCleaning:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS cleaning 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             problem_id VARCHAR(30),
                             description TEXT
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, problem_id, description):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM cleaning WHERE problem_id = ?", (problem_id,))
        row = cursor.fetchone()

        if row is None:
            cursor.execute('''INSERT INTO cleaning 
                            (problem_id, description) 
                            VALUES (?,?)''', (problem_id, description))

        else:
            cursor.execute('''UPDATE cleaning
                              SET description = ? 
                              WHERE problem_id = ?''', (description, problem_id))
        cursor.close()
        self.connection.commit()

    def get(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM cleaning WHERE id = 1")
        row = cursor.fetchone()
        if row:
            cursor.execute('''DELETE FROM cleaning WHERE id = 1''')
            cursor.close()
            self.connection.commit()
        return row


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
    res = []

    for problem_id in problems_id:
        data = problem_table.get(problem_id)
        res.append({'CALLBACKMEMO': data[2],
                    'reply': data[3],
                    'description': data[4],
                    'problem_id': problem_id})

    return res

#
# def add_data_from_csv_to_clear(path):
#     from pandas import read_csv
#     import base64
#
#     db = DB()
#     clean_table = CleanTable(db.get_connection())
#     clean_table.init_table()
#
#     excel = read_csv(path)
#     case_nums = list(excel['Номер кейса'])
#     descriptions = list(excel['clear_text'])
#
#     for _ in range(len(excel)):
#         case_num = case_nums.pop(0)
#         description = descriptions.pop(0)
#
#         if all(map(lambda x: type(x) != float, [case_num, description])):
#             if description:
#                 vector = phrase_to_vector_to_str(description)
#                 # print(vector)
#                 # print(type(vector))
#                 clean_table.insert(case_num, description, vector)
#
#             print(_)
#
#
# from backend.cleaning import phrase_to_vector_to_str
#
# import base64
#
# db = DB()
# clean_table = CleanTable(db.get_connection())
# data = clean_table.get('SD1214250')
# print(data[3])
# print(data[3] == phrase_to_vector_to_str(data[2]))
# add_data_from_csv_to_clear('final_text.csv')
