from database.db import *
from backend.function_for_clean import tokenize_me
database = DB()
cleaning_table = DataToCleaning(database.get_connection())
clean_table = CleanTable(database.get_connection())

while True:
    data = cleaning_table.get()

    if data:
        clean_table.insert(data[1], tokenize_me(data[2]))

