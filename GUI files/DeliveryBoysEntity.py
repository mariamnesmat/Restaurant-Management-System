import mysql.connector
from tkinter import *
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MS-msMarie27Rroaa22",
  database="Restaurant1"
)
boy_id_entry = None
boy_name_entry = None
boy_email_entry = None
boy_phone_entry = None
delivery_area_entry = None
boy_available_entry = None
def insert_data(boy_id,boy_name,boy_email,boy_phone,delivery_area,boy_available):
     boy_id = boy_id_entry.get()
     boy_name = boy_name_entry.get()
     boy_email = boy_email_entry.get()
     boy_phone = boy_phone_entry.get()
     delivery_area = delivery_area_entry.get()
     boy_available = boy_available_entry.get()
     mycursor = mydb.cursor()
     sql = "INSERT INTO DeliveryBoy (BoyID, BoyName, BoyEmail, BoyPhone, DeliveryArea, BoyAvailable) VALUES (%s, %s, %s, %s, %s, %s)"
     val = (boy_id, boy_name, boy_email, boy_phone, delivery_area, boy_available)
     mycursor.execute(sql, val)
     mydb.commit()
     mycursor.close()
def fetch_records():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT BoyID, BoyName ,BoyAvailable FROM DeliveryBoy")
    records = mycursor.fetchall()
    mycursor.close()
    return records
def display_records():
    records = fetch_records()
    display_window = Toplevel(root)
    display_window.geometry("300x300")
    listbox = Listbox(display_window, height=20, width=100 )
    listbox.pack()
    for record in records:
        listbox.insert(END, f"ID: {record[0]}, Name: {record[1]}, Available: {record[2]}")  # Displaying ID and Name in the same line
def update_data(boy_id, new_available_status):
    mycursor = mydb.cursor()
    sql = "UPDATE DeliveryBoy SET BoyAvailable = %s WHERE BoyID = %s"
    val = (new_available_status, boy_id)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def delete_data(boy_id):
    mycursor = mydb.cursor()

    try:
        mycursor.execute("SELECT OrderID FROM Orders WHERE DeliveryBoyID = %s", (boy_id,))
        orders = mycursor.fetchall()

        for order in orders:
            mycursor.execute("DELETE FROM Payment WHERE OrderID = %s", (order[0],))

        mycursor.execute("DELETE FROM DeliveryBoy WHERE BoyID = %s", (boy_id,))
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
    global boy_id_entry, boy_name_entry, boy_email_entry, boy_phone_entry, delivery_area_entry, boy_available_entry  # Add this line
    boy_id_label = Label(insert_window, text="Boy ID:")
    boy_id_label.pack()
    boy_id_entry = Entry(insert_window)
    boy_id_entry.pack()
    boy_name_label = Label(insert_window, text="Boy Name:")
    boy_name_label.pack()
    boy_name_entry = Entry(insert_window)
    boy_name_entry.pack()
    boy_email_label = Label(insert_window, text="Boy Email:")
    boy_email_label.pack()
    boy_email_entry = Entry(insert_window)
    boy_email_entry.pack()
    boy_phone_label = Label(insert_window, text="Boy Phone:")
    boy_phone_label.pack()
    boy_phone_entry = Entry(insert_window)
    boy_phone_entry.pack()
    delivery_area_label = Label(insert_window, text="Delivery Area:")
    delivery_area_label.pack()
    delivery_area_entry = Entry(insert_window)
    delivery_area_entry.pack()
    boy_available_label = Label(insert_window, text="Boy Available:")
    boy_available_label.pack()
    boy_available_entry = Entry(insert_window)
    boy_available_entry.pack()
    submit_button = Button(insert_window, text="Insert", command=lambda: insert_data(boy_id_entry.get(), boy_name_entry.get(), boy_email_entry.get(), boy_phone_entry.get(), delivery_area_entry.get(), boy_available_entry.get()))
    submit_button.pack()
def open_update_window():
    update_window = Toplevel(root)
    update_window.geometry("700x700")
    boy_id_label = Label(update_window, text="Boy ID:")
    boy_id_label.pack()
    boy_id_entry = Entry(update_window)
    boy_id_entry.pack()
    new_available_status_label = Label(update_window, text="New Availability Status (True/False):")
    new_available_status_label.pack()
    new_available_status_entry = Entry(update_window)
    new_available_status_entry.pack()
    submit_button = Button(update_window, text="Update", command=lambda: update_data(boy_id_entry.get(), new_available_status_entry.get()))
    submit_button.pack()

def open_delete_window():
    delete_window = Toplevel(root)
    delete_window.geometry("400x200")
    boy_id_label = Label(delete_window, text="Boy ID:")
    boy_id_label.pack()
    boy_id_entry = Entry(delete_window)
    boy_id_entry.pack()
    submit_button = Button(delete_window, text="Delete", command=lambda: delete_data(boy_id_entry.get()))
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
