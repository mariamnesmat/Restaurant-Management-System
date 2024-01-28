import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MS-msMarie27Rroaa22",
    database="Restaurant1"
)

restaurant_id_entry = None
restaurant_name_entry = None
city_entry = None
address_line1_entry = None
restaurant_category_entry = None
phone_entry = None
contact_info_entry = None

def insert_data(restaurant_id, restaurant_name, city, address_line1, restaurant_category, phone, contact_info):
    restaurant_id = restaurant_id_entry.get()
    restaurant_name = restaurant_name_entry.get()
    city = city_entry.get()
    address_line1 = address_line1_entry.get()
    restaurant_category = restaurant_category_entry.get()
    phone = phone_entry.get()
    contact_info = contact_info_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO Restaurant (RestaurantID, restaurant_name, city, addressLine1, restaurant_category, phone, ContactInfo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (restaurant_id, restaurant_name, city, address_line1, restaurant_category, phone, contact_info)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def fetch_records():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT RestaurantID, restaurant_name, city, phone FROM Restaurant")
    records = mycursor.fetchall()
    mycursor.close()
    return records

def display_records():
    records = fetch_records()
    display_window = Toplevel(root)
    display_window.geometry("700x700")
    listbox = Listbox(display_window, height = 40, width = 100)
    listbox.pack()
    for record in records:
        listbox.insert(END, f"ID: {record[0]}, Name: {record[1]}, city: {record[2]}, Phone: {record [3]}")

def open_insert_window():
    insert_window = Toplevel(root)
    insert_window.geometry("500x500")
    global restaurant_id_entry, restaurant_name_entry, city_entry, address_line1_entry, restaurant_category_entry, phone_entry, contact_info_entry

    restaurant_id_label = Label(insert_window, text="Restaurant ID:")
    restaurant_id_label.pack()
    restaurant_id_entry = Entry(insert_window)
    restaurant_id_entry.pack()

    restaurant_name_label = Label(insert_window, text="Restaurant Name:")
    restaurant_name_label.pack()
    restaurant_name_entry = Entry(insert_window)
    restaurant_name_entry.pack()

    city_label = Label(insert_window, text="City:")
    city_label.pack()
    city_entry = Entry(insert_window)
    city_entry.pack()

    address_line1_label = Label(insert_window, text="Address Line 1:")
    address_line1_label.pack()
    address_line1_entry = Entry(insert_window)
    address_line1_entry.pack()

    restaurant_category_label = Label(insert_window, text="Restaurant Category:")
    restaurant_category_label.pack()
    restaurant_category_entry = Entry(insert_window)
    restaurant_category_entry.pack()

    phone_label = Label(insert_window, text="Phone:")
    phone_label.pack()
    phone_entry = Entry(insert_window)
    phone_entry.pack()

    contact_info_label = Label(insert_window, text="Contact Info:")
    contact_info_label.pack()
    contact_info_entry = Entry(insert_window)
    contact_info_entry.pack()

    submit_button = Button(insert_window, text="Insert", command=lambda: insert_data(
        restaurant_id_entry.get(), restaurant_name_entry.get(), city_entry.get(), address_line1_entry.get(),
        restaurant_category_entry.get(), phone_entry.get(), contact_info_entry.get()))
    submit_button.pack()

def open_update_window():
    update_window = Toplevel(root)
    update_window.geometry("700x700")

    restaurant_id_label = Label(update_window, text="Restaurant ID:")
    restaurant_id_label.pack()
    restaurant_id_entry = Entry(update_window)
    restaurant_id_entry.pack()

    new_contact_info_label = Label(update_window, text="New Contact Info:")
    new_contact_info_label.pack()
    new_contact_info_entry = Entry(update_window)
    new_contact_info_entry.pack()

    submit_button = Button(update_window, text="Update", command=lambda: update_data(restaurant_id_entry.get(),
                                                                                    new_contact_info_entry.get()))
    submit_button.pack()

def open_delete_window():
    delete_window = Toplevel(root)
    delete_window.geometry("400x200")

    restaurant_id_label = Label(delete_window, text="Restaurant ID:")
    restaurant_id_label.pack()
    restaurant_id_entry = Entry(delete_window)
    restaurant_id_entry.pack()

    submit_button = Button(delete_window, text="Delete", command=lambda: delete_data(restaurant_id_entry.get()))
    submit_button.pack()

def update_data(restaurant_id, new_contact_info):
    mycursor = mydb.cursor()
    sql = "UPDATE Restaurant SET ContactInfo = %s WHERE RestaurantID = %s"
    val = (new_contact_info, restaurant_id)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def delete_data(restaurant_id):
    mycursor = mydb.cursor()

    try:
        mycursor.execute("SELECT * FROM MenuItem WHERE RestaurantID = %s", (restaurant_id,))
        menu_items = mycursor.fetchall()

        for menu_item in menu_items:
            mycursor.execute("DELETE FROM MenuItem WHERE MenuItemID = %s", (menu_item[0],))

        mycursor.execute("SELECT * FROM Orders WHERE RestaurantID = %s", (restaurant_id,))
        orders = mycursor.fetchall()
        for order in orders:
            mycursor.execute("DELETE FROM Payment WHERE OrderID = %s", (order[0],))
            mycursor.execute("DELETE FROM Orders WHERE OrderID = %s", (order[0],))

        mycursor.execute("DELETE FROM Restaurant WHERE RestaurantID = %s", (restaurant_id,))
        mydb.commit()

        print("Delete successful")
    except Exception as e:
        print(f"Error deleting data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()
root = Tk()
root.geometry("700x700")

insert_button = Button(root, text="Insert", command=open_insert_window)
insert_button.pack()

display_button = Button(root, text="Display Records", command=display_records)
display_button.pack()

update_button = Button(root, text="Update", command=open_update_window)
update_button.pack()

delete_button = Button(root, text="Delete", command=open_delete_window)
delete_button.pack()

root.mainloop()
