from email import header
from fileinput import filename
from msilib.schema import Error
import sqlite3
from os import curdir


def init_tables(cursor: sqlite3.Cursor, connection: sqlite3.Connection):
    init_file = open("db_prepare.txt", 'r')
    
    for line in init_file:
        #print(line)
        cursor.execute(line)
        connection.commit()
        
    
    print("Таблицы созданы!")






def init_data(cursor: sqlite3.Cursor, connection: sqlite3.Connection, file_name: str):
    init_file = open(file_name, 'r')
    command = "INSERT INTO " + file_name[:-4] + " VALUES ("
    for line in init_file:
        s = command + '\''+'\',\''.join(line.split(' '))[:-1]+'\')'
        #print(s)
        cursor.execute(s)
        connection.commit()
    
    print(f"Таблица {file_name[:-4]} проинициализорована!")



try:
    sql_connection = sqlite3.connect("database.db")
    print("Подключение к базе выполнено.")
    cursor = sql_connection.cursor()
    init_tables(cursor, sql_connection)
    
    #init_data(cursor, sql_connection, f"available_cars.txt")
    #init_data(cursor, sql_connection, f"manufacturer.txt")
    #init_data(cursor, sql_connection, f"clients_orders.txt")
    #init_data(cursor, sql_connection, f"sanction_countries.txt")
    command = input("Введите SQL команду: ")
    while command != "close":
        cursor.execute(command)
        
        if command.split(' ')[0] == "SELECT":
            headers = cursor.description
            header_s = (' '.join(t for x in headers for t in x if type(' ') == type(t)))
            #format_header_s = f''
            print(header_s) 
            records = cursor.fetchall()
            for line in records:
                print(' '.join([x for x in line]))
                #print(line)
                
        command = input("Введите SQL команду: ")
                
        
    
except sqlite3.Error as error:
    print("Ошибка при создании 'my_database.db'", error)
    