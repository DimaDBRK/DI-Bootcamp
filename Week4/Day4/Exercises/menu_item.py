# Week4 Day4
# Dmitry Dubrov
# Exercises XP

# Exercise 1 : Restaurant Menu Manager
# PART 1
# In this exercise we will use PostgreSQL and Python.

# 1. Create a new database and a new table in pgAdmin (or in psql). The table is named Menu_Items and contains the columns
# item_id : SERIAL PRIMARY KEY
# item_name : VARCHAR(30) NOT NULL
# item_price : SMALLINT DEFAULT 0

# -- CREATE TABLE Menu_Items (
# -- 	item_id SERIAL PRIMARY KEY,
# -- 	item_name VARCHAR(30) NOT NULL,
# -- 	item_price SMALLINT DEFAULT 0
# -- )

# 2. Class called MenuItem, the attributes should be the name and
# price of each item.

import psycopg2

class MenuItem: 
    def __init__(self, item_name, item_price):
        self.name = item_name
        self.price = item_price

# Create several methods (save, delete, update) these methods will allow a 
# user to save, delete and update items from the Menu_Items table. 
# The update method can update the name as well as the price of an item.

# connect to the database
   
    def manage_connection(self, query):
        try:
            connection = psycopg2.connect(
                host='localhost',
                port = '5432',
                database='U',
                user='postgres',
                password='Kachkanar'
            )
            with connection:
                with connection.cursor() as cursor:   #it will close the cursor automatically
                    if 'SELECT' in query:
                        print('SELECT')
                        cursor.execute(query)
                        result = cursor.fetchall()
                        return result
                    else:
                        print('INSERT')
                        cursor.execute(query)
                        connection.commit()
        except:
            pass
        finally:
             #it will close the connection automatically
            if connection != None:
                connection.close()   
    
    #save
    def save(self):
        query = f'''
INSERT INTO Menu_Items (item_name, item_price)
VALUES ('{self.name}', {self.price})'''
        self.manage_connection(query)
       
    def delete(self):
        query = f'''
    DELETE FROM Menu_Items WHERE item_name = '{self.name}' AND item_price = '{self.price}';
    '''
        self.manage_connection(query)
    
    def update(self,*args):
        # we can inser parametrs in any order or only name or only price
        column = ''
        if len(args) == 1 and type(args[0]) in [str, int,float]:
            if type(args[0]) == str:
                column = f'''item_name = '{args[0]}' '''
                print("name")
            elif type(args[0]) in [int,float] :
                print(type(args[0]))
                column = f'''item_price = {args[0]} '''
        elif len(args) == 2 and ((type(args[0]) == str and type(args[1]) in [int,float]) or (type(args[1]) == str and type(args[0]) in [int,float])):
            if type(args[0]) == str and type(args[1]) in [int,float]:
                column = f'''item_name = '{args[0]}', item_price = {args[1]}'''    
            else:
                column = f'''item_name = '{args[1]}', item_price = {args[0]}'''
        else:
            print('Wrong parametrs name and price')
        
        query = f'''
    UPDATE Menu_Items 
    SET {column}
    WHERE item_name = '{self.name}' AND item_price = {self.price};
    '''
        self.manage_connection(query)
          
#Driver
