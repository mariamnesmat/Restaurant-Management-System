import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MS-msMarie27Rroaa22",
    database="Restaurant1"
)

location_id_entry = None
location_name_entry = None


def insert_data(location_id, location_name):
    location_id = location_id_entry.get()
    location_name = location_name_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO GeoLocation (LocationID, LocationName) VALUES (%s, %s)"
    val = (location_id, location_name)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()


def fetch_records():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT LocationID, LocationName FROM GeoLocation")
    records = mycursor.fetchall()
    mycursor.close()
    return records


def display_records():
    records = fetch_records()
    display_window = Toplevel(root)
    display_window.geometry("700x700")
    listbox = Listbox(display_window, width = 350, height = 350)
    listbox.pack()
    for record in records:
        listbox.insert(END, f"ID: {record[0]}, Name: {record[1]}")


def update_data(location_id, new_location_name):
    mycursor = mydb.cursor()
    sql = "UPDATE GeoLocation SET LocationName = %s WHERE LocationID = %s"
    val = (new_location_name, location_id)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()


def delete_data(location_id):
    mycursor = mydb.cursor()

    try:
        mycursor.execute("DELETE FROM GeoLocation WHERE LocationID = %s", (location_id,))
        mydb.commit()

        print("Delete successful")
    except Exception as e:
        print(f"Error deleting data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()


def open_insert_window():
    insert_window = Toplevel(root)
    insert_window.geometry("500x500")
    global location_id_entry, location_name_entry
    location_id_label = Label(insert_window, text="Location ID:")
    location_id_label.pack()
    location_id_entry = Entry(insert_window)
    location_id_entry.pack()
    location_name_label = Label(insert_window, text="Location Name:")
    location_name_label.pack()
    location_name_entry = Entry(insert_window)
    location_name_entry.pack()
    submit_button = Button(insert_window, text="Insert",
                           command=lambda: insert_data(location_id_entry.get(), location_name_entry.get()))
    submit_button.pack()


def open_update_window():
    update_window = Toplevel(root)
    update_window.geometry("700x700")
    location_id_label = Label(update_window, text="Location ID:")
    location_id_label.pack()
    location_id_entry = Entry(update_window)
    location_id_entry.pack()
    new_location_name_label = Label(update_window, text="New Location Name:")
    new_location_name_label.pack()
    new_location_name_entry = Entry(update_window)
    new_location_name_entry.pack()
    submit_button = Button(update_window, text="Update",
                           command=lambda: update_data(location_id_entry.get(), new_location_name_entry.get()))
    submit_button.pack()


def open_delete_window():
    delete_window = Toplevel(root)
    delete_window.geometry("400x200")
    location_id_label = Label(delete_window, text="Location ID:")
    location_id_label.pack()
    location_id_entry = Entry(delete_window)
    location_id_entry.pack()
    submit_button = Button(delete_window, text="Delete", command=lambda: delete_data(location_id_entry.get()))
    submit_button.pack()


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
