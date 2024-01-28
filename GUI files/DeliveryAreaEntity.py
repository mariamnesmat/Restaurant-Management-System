import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MS-msMarie27Rroaa22",
    database="Restaurant1"
)

delivery_area_code_entry = None
area_name_entry = None

def insert_delivery_area_data(delivery_area_code, area_name):
    delivery_area_code = delivery_area_code_entry.get()
    area_name = area_name_entry.get()
    mycursor = mydb.cursor()
    sql = "INSERT INTO DeliveryArea (AreaCode, area_name) VALUES (%s, %s)"
    val = (delivery_area_code, area_name)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def fetch_delivery_area_records():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT AreaCode, area_name FROM DeliveryArea")
    records = mycursor.fetchall()
    mycursor.close()
    return records

def display_delivery_area_records():
    records = fetch_delivery_area_records()
    display_window = Toplevel(root)
    display_window.geometry("800x600")  
    listbox = Listbox(display_window, height=20, width=100)  
    listbox.pack()
    for record in records:
        listbox.insert(END, f"Area Code: {record[0]}, Area Name: {record[1]}")

def update_delivery_area_data(delivery_area_code, new_area_name):
    mycursor = mydb.cursor()
    sql = "UPDATE DeliveryArea SET area_name = %s WHERE AreaCode = %s"
    val = (new_area_name, delivery_area_code)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def delete_delivery_area_data(delivery_area_code):
    mycursor = mydb.cursor()

    try:
        sql = "DELETE FROM DeliveryArea WHERE AreaCode = %s"
        mycursor.execute(sql, (delivery_area_code,))
        mydb.commit()
        print("Delete successful")
    except Exception as e:
        print(f"Error deleting data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()
        
        
def open_insert_delivery_area_window():
    insert_window = Toplevel(root)
    insert_window.geometry("700x600")
    global delivery_area_code_entry, area_name_entry
    delivery_area_code_label = Label(insert_window, text="Area Code:")
    delivery_area_code_label.pack()
    delivery_area_code_entry = Entry(insert_window)
    delivery_area_code_entry.pack()
    area_name_label = Label(insert_window, text="Area Name:")
    area_name_label.pack()
    area_name_entry = Entry(insert_window)
    area_name_entry.pack()
    submit_button = Button(insert_window, text="Insert", command=lambda: insert_delivery_area_data(delivery_area_code_entry.get(), area_name_entry.get()))
    submit_button.pack()

def open_update_delivery_area_window():
    update_window = Toplevel(root)
    update_window.geometry("700x600")
    delivery_area_code_label = Label(update_window, text="Area Code:")
    delivery_area_code_label.pack()
    delivery_area_code_entry = Entry(update_window)
    delivery_area_code_entry.pack()
    new_area_name_label = Label(update_window, text="New Area Name:")
    new_area_name_label.pack()
    new_area_name_entry = Entry(update_window)
    new_area_name_entry.pack()
    submit_button = Button(update_window, text="Update", command=lambda: update_delivery_area_data(delivery_area_code_entry.get(), new_area_name_entry.get()))
    submit_button.pack()

def open_delete_delivery_area_window():
    delete_window = Toplevel(root)
    delete_window.geometry("700x600")
    delivery_area_code_label = Label(delete_window, text="Area Code:")
    delivery_area_code_label.pack()
    delivery_area_code_entry = Entry(delete_window)
    delivery_area_code_entry.pack()
    submit_button = Button(delete_window, text="Delete", command=lambda: delete_delivery_area_data(delivery_area_code_entry.get()))
    submit_button.pack()

root = Tk()
root.geometry("600x400")

insert_button = Button(root, text="Insert Delivery Area", command=open_insert_delivery_area_window)
insert_button.pack()
display_button = Button(root, text="Display Delivery Area Records", command=display_delivery_area_records)
display_button.pack()
update_button = Button(root, text="Update Delivery Area", command=open_update_delivery_area_window)
update_button.pack()
delete_button = Button(root, text="Delete Delivery Area", command=open_delete_delivery_area_window)
delete_button.pack()

root.mainloop()
