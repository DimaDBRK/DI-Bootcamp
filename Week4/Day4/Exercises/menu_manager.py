# Week4 Day4
# Dmitry Dubrov
# Exercises XP

# Exercise 1 : Restaurant Menu Manager
# PART 1
import psycopg2

class MenuManager:
    
    
    
# In the file menu_manager.py, create a new class called MenuManager
# Create a Class Method called get_by_name that will return a single 
# item from the Menu_Items table depending on it’s name, if an object 
# is not found (there is no item matching the name in the get_by_name method)
# return None.

# Create a Class Method called all_items which will return a list of all 
# the items from the Menu_Items table.  
    @classmethod
    def get_by_name(cls, name):
        query = f'''
SELECT  item_name, item_price FROM Menu_Items
WHERE item_name = '{name}' '''
        res = cls.manage_connection(query)
        if len(res) == 0:
            return  None
        else:
            return res[0]
    
    @classmethod
    def all_items(cls):
        query = f'''
SELECT  item_name, item_price FROM Menu_Items
'''
        res = cls.manage_connection(query)
        if len(res) == 0:
            return  None
        else:
            return res
    
    @staticmethod
    def manage_connection(query):
        try:
            connection = psycopg2.connect(
                host='localhost',
                port = '5432',
                database='Public',
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
    

#Driver

