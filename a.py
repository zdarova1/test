from email import header
from fileinput import filename
from msilib.schema import Error
import sqlite3
from os import curdir
from prettytable import PrettyTable


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
        print(s)
        cursor.execute(s)
        connection.commit()
    
    print(f"Таблица {file_name[:-4]} проинициализорована!")


def  my_selects():
    str = input(f''' 
          show TABLES - 1
          show client's orders with  
          ''')



try:
    sql_connection = sqlite3.connect("database.db")
    print("Подключение к базе выполнено.")
    cursor = sql_connection.cursor()
    init_tables(cursor, sql_connection)
    
    #init_data(cursor, sql_connection, f"available_cars.txt") раскоменть
   # init_data(cursor, sql_connection, f"manufacturer.txt")
    #init_data(cursor, sql_connection, f"clients_orders.txt")
    #init_data(cursor, sql_connection, f"sanction_countries.txt")раскоменть
    command = input("Введите SQL команду: ")
    while command != "close":
        cursor.execute(command)
        
        if command.split(' ')[0] == "SELECT":
            headers = [t for x in cursor.description for t in x if type(' ') == type(t)] 
            table = PrettyTable(headers)
            #print(headers)
            
            records = cursor.fetchall()
            for line in records:
                table.add_row(([x for x in line]))
                #print(([x for x in line]))
            print(table)
        command = input("Введите SQL команду: ")
                
        
    
except sqlite3.Error as error:
    print("Ошибка при создании 'my_database.db'", error)
    