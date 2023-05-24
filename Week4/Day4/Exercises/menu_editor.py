# Week4 Day4
# Dmitry Dubrov
# Exercises XP
# Feature - you can insert price or name or both for update in on line in any order

# Exercise 1 : Restaurant Menu Manager
# Part 2
# 1. Create a file called menu_editor.py , which will have the following 
# functions

# 1. show_user_menu() - this function should display the program menu 
# (not the restaurant menu!), and ask the user to :
# View an Item (V)
# Add an Item (A)
# Delete an Item (D)
# Update an Item (U)
# Show the Menu (S)
# Call the appropriate function that matches the user’s input.
from menu_item import MenuItem
from menu_manager import MenuManager
import psycopg2

def show_user_menu():
    while True:
        print("\n***Program menu:***\n")
        print('''View an Item (V)
Add an Item (A)
Delete an Item (D)
Update an Item (U)
Show the Menu (S))
Exit (Q,E)
''')
        user_in = input("Input menu item:").lower()
        user_in = ''.join(user_in.split())
        if user_in in ["v",'a','d','u','s','q','e']:
            if user_in in ['q','e']:
                
                show_restaurant_menu()
                print('Exit!')
                break
            elif user_in == 'v':
                print('View an Item.')
                view_item() 
                
            elif user_in == 'a':
                print('Add an Item:')
                add_item_to_menu()
                
            elif user_in == 'd':
                print('Delete an Item.')
                remove_item_from_menu()
                
            elif user_in == 'u':
                print('Update an Item.')
                update_item_from_menu()
                input('Press Enter to go')
                
            elif user_in == 's':
                print('Show the Menu:')
                show_restaurant_menu()
                input('Press Enter to go')
        else:
            print("Wrong input. Try again.")
            input('Press Enter to go')

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def show_restaurant_menu():
    res = MenuManager.all_items()
    print("\n--- Menu: ----")
    for i in range(len(res)):
        print(f'{i+1} - {res[i][0]} - {res[i][1]}')
    
def view_item():               
    name = input("Input item name: ")
    res = MenuManager.get_by_name(name)
    if res != None:
        print(f'There is: {res[0]} , with prise: {res[1]}.')
        input('Press Enter to go')
    else: 
        print(f'In menu there is now {name}.')
        input('Press Enter to go')
  
def remove_item_from_menu():
    nm = input('Input name of Item for remove: ')
    nm = nm.strip()
    check_before = MenuManager.get_by_name(nm)
    if check_before != None: #if this item exist
        item_d = MenuItem(check_before[0], check_before[1])
        item_d.delete()
        check_after = MenuManager.get_by_name(nm)
        if check_after == None:
            print(f'Items with name: {nm} and price: {check_before[1]} was deleted.')
            input('Press Enter to go')
        else:
            print(f'Error. There is still item {check_after}')
            input('Press Enter to go')
    else:
        print(f'''Item with name: {nm} doesn't exist. Try new name.''')
        input('Press Enter to go')              

def add_item_to_menu():
    nm = input('Input name: ')
    pr = input('Inpur price: ')
    pr = ''.join(pr.split())
    if type(nm) == str and is_number(pr):
        pr = int(float(pr))
        item_new = MenuItem(nm, pr)
        item_new.save()
        check = MenuManager.get_by_name(nm)
        if check == (nm,pr):
            print(f'Item with naame: {nm} and price: {pr} added.')
        elif check == None:
            print('Problem, check table.')
            input('Press Enter to start')
                        
    else:
        print('Wrong data type. Try again.')
        input('Press Enter to start')
    
    
def update_item_from_menu():
    nm = input('Input name of Item to update: ')
    pr = input('Input price of Item to update: ')
    pr = ''.join(pr.split())
    if type(nm) == str and is_number(pr):
        pr = int(float(pr))
        # item_new = MenuItem(nm, pr)
        # item_new.save()
        check = MenuManager.get_by_name(nm)
        if check == (nm,pr):
            print(f'Item with name: {nm} and price: {pr} are in Menu. \nIt could be updated.')
            print('Input new information - name or price, or both (splyt by , in any order).')
            new_info_name = input("New info for update:").strip().split(",")
            if len(new_info_name) > 2 or len(new_info_name) == 0 or new_info_name in ['']:
                print('Wrong data type. Try again.')
            
            else: 
                
                for i in range(len(new_info_name)):
                    if new_info_name[i].isnumeric():
                        new_info_name[i] = int(new_info_name[i])
                        
                print(new_info_name) 
                item_update = MenuItem(nm, pr)
                if len(new_info_name) == 2:
                    item_update.update(new_info_name[0],new_info_name[1])
                else:
                    item_update.update(new_info_name[0])
                print('Item was updated.')
                
        elif check == None:
            print('Problem, check table.')
            input('Press Enter to go')
                        
    else:
        print('Wrong data type. Try again.')
        input('Press Enter to go')
    
#Driver           
show_user_menu()
