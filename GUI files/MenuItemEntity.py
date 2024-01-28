import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MS-msMarie27Rroaa22",
    database="Restaurant1"
)

menu_item_id_entry = None
name_entry = None
restaurant_id_entry = None
description_entry = None
price_entry = None
category_entry = None

def insert_menu_item_data(menu_item_id, name, restaurant_id, description, price, category):
    menu_item_id = menu_item_id_entry.get()
    name = name_entry.get()
    restaurant_id = restaurant_id_entry.get()
    description = description_entry.get()
    price = price_entry.get()
    category = category_entry.get()
    mycursor = mydb.cursor()
    sql = "INSERT INTO MenuItem (MenuItemID, Name, RestaurantID, Description, Price, Category) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (menu_item_id, name, restaurant_id, description, price, category)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def fetch_menu_item_records():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT MenuItemID, Name, RestaurantID, Description, Price, Category FROM MenuItem")
    records = mycursor.fetchall()
    mycursor.close()
    return records

def display_menu_item_records():
    records = fetch_menu_item_records()
    display_window = Toplevel(root)
    display_window.geometry("600x600")
    listbox = Listbox(display_window, width = 250, height = 300)
    listbox.pack()
    for record in records:
        listbox.insert(END, f"Item ID: {record[0]}, Name: {record[1]}, Restaurant ID: {record[2]}, Description: {record[3]}, Price: {record[4]}, Category: {record[5]}")

def update_menu_item_data(menu_item_id, new_price):
    mycursor = mydb.cursor()
    sql = "UPDATE MenuItem SET Price = %s WHERE MenuItemID = %s"
    val = (new_price, menu_item_id)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def delete_menu_item_data(menu_item_id):
    mycursor = mydb.cursor()

    try:
        mycursor.execute("DELETE FROM MenuItem WHERE MenuItemID = %s", (menu_item_id,))
        mydb.commit()
        print("Delete successful")
    except Exception as e:
        print(f"Error deleting data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def open_insert_menu_item_window():
    insert_window = Toplevel(root)
    insert_window.geometry("400x300")
    global menu_item_id_entry, name_entry, restaurant_id_entry, description_entry, price_entry, category_entry
    menu_item_id_label = Label(insert_window, text="Menu Item ID:")
    menu_item_id_label.pack()
    menu_item_id_entry = Entry(insert_window)
    menu_item_id_entry.pack()
    name_label = Label(insert_window, text="Name:")
    name_label.pack()
    name_entry = Entry(insert_window)
    name_entry.pack()
    restaurant_id_label = Label(insert_window, text="Restaurant ID:")
    restaurant_id_label.pack()
    restaurant_id_entry = Entry(insert_window)
    restaurant_id_entry.pack()
    description_label = Label(insert_window, text="Description:")
    description_label.pack()
    description_entry = Entry(insert_window)
    description_entry.pack()
    price_label = Label(insert_window, text="Price:")
    price_label.pack()
    price_entry = Entry(insert_window)
    price_entry.pack()
    category_label = Label(insert_window, text="Category:")
    category_label.pack()
    category_entry = Entry(insert_window)
    category_entry.pack()
    submit_button = Button(insert_window, text="Insert", command=lambda: insert_menu_item_data(
        menu_item_id_entry.get(), name_entry.get(), restaurant_id_entry.get(),
        description_entry.get(), price_entry.get(), category_entry.get()))
    submit_button.pack()

def open_update_menu_item_window():
    update_window = Toplevel(root)
    update_window.geometry("400x200")
    menu_item_id_label = Label(update_window, text="Menu Item ID:")
    menu_item_id_label.pack()
    menu_item_id_entry = Entry(update_window)
    menu_item_id_entry.pack()
    new_price_label = Label(update_window, text="New Price:")
    new_price_label.pack()
    new_price_entry = Entry(update_window)
    new_price_entry.pack()
    submit_button = Button(update_window, text="Update", command=lambda: update_menu_item_data(
        menu_item_id_entry.get(), new_price_entry.get()))
    submit_button.pack()

def open_delete_menu_item_window():
    delete_window = Toplevel(root)
    delete_window.geometry("300x100")
    menu_item_id_label = Label(delete_window, text="Menu Item ID:")
    menu_item_id_label.pack()
    menu_item_id_entry = Entry(delete_window)
    menu_item_id_entry.pack()
    submit_button = Button(delete_window, text="Delete", command=lambda: delete_menu_item_data(menu_item_id_entry.get()))
    submit_button.pack()

root = Tk()
root.geometry("600x400")

insert_button = Button(root, text="Insert Menu Item", command=open_insert_menu_item_window)
insert_button.pack()
display_button = Button(root, text="Display Menu Item Records", command=display_menu_item_records)
display_button.pack()
update_button = Button(root, text="Update Menu Item", command=open_update_menu_item_window)
update_button.pack()
delete_button = Button(root, text="Delete Menu Item", command=open_delete_menu_item_window)
delete_button.pack()

root.mainloop()
