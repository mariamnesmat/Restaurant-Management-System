import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MS-msMarie27Rroaa22",
    database="Restaurant1"
)

request_id_entry = None
request_name_entry = None
request_details_entry = None
request_status_entry = None
customer_id_entry = None
delivery_boy_id_entry = None

def insert_request_data(request_id, request_name, request_details, request_status, customer_id, delivery_boy_id):
    mycursor = mydb.cursor()
    sql = "INSERT INTO Request (RequestID, RequestName, RequestDetails, RequestStatus, CustomerID, DeliveryBoyID) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (request_id, request_name, request_details, request_status, customer_id, delivery_boy_id)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def fetch_request_records():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT RequestID, RequestName, RequestDetails, RequestStatus,CustomerID, DeliveryBoyID FROM Request")
    records = mycursor.fetchall()
    mycursor.close()
    return records

def display_request_records():
    records = fetch_request_records()
    display_window = Toplevel(root)
    display_window.geometry("700x700")
    listbox = Listbox(display_window, width = 300, height = 500)
    listbox.pack()
    for record in records:
        listbox.insert(END, f"ID: {record[0]}, Name: {record[1]}, Detailes: {record[2]}, Status: {record[3]}, Customer ID: {record[4]}, Delivery ID: {record[5]} ")

def update_request_data(request_id, new_status):
    mycursor = mydb.cursor()
    sql = "UPDATE Request SET RequestStatus = %s WHERE RequestID = %s"
    val = (new_status, request_id)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def delete_request_data(request_id):
    mycursor = mydb.cursor()
    try:
        mycursor.execute("DELETE FROM Request WHERE RequestID = %s", (request_id,))
        mydb.commit()
        print("Delete successful")
    except Exception as e:
        print(f"Error deleting data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def open_insert_request_window():
    insert_window = Toplevel(root)
    insert_window.geometry("500x500")
    global request_id_entry, request_name_entry, request_details_entry, request_status_entry, customer_id_entry, delivery_boy_id_entry
    request_id_label = Label(insert_window, text="Request ID:")
    request_id_label.pack()
    request_id_entry = Entry(insert_window)
    request_id_entry.pack()
    request_name_label = Label(insert_window, text="Request Name:")
    request_name_label.pack()
    request_name_entry = Entry(insert_window)
    request_name_entry.pack()
    request_details_label = Label(insert_window, text="Request Details:")
    request_details_label.pack()
    request_details_entry = Entry(insert_window)
    request_details_entry.pack()
    request_status_label = Label(insert_window, text="Request Status:")
    request_status_label.pack()
    request_status_entry = Entry(insert_window)
    request_status_entry.pack()
    customer_id_label = Label(insert_window, text="Customer ID:")
    customer_id_label.pack()
    customer_id_entry = Entry(insert_window)
    customer_id_entry.pack()
    delivery_boy_id_label = Label(insert_window, text="Delivery Boy ID:")
    delivery_boy_id_label.pack()
    delivery_boy_id_entry = Entry(insert_window)
    delivery_boy_id_entry.pack()
    submit_button = Button(insert_window, text="Insert", command=lambda: insert_request_data(
        request_id_entry.get(), request_name_entry.get(), request_details_entry.get(),
        request_status_entry.get(), customer_id_entry.get(), delivery_boy_id_entry.get()
    ))
    submit_button.pack()

def open_update_request_window():
    update_window = Toplevel(root)
    update_window.geometry("400x400")
    request_id_label = Label(update_window, text="Request ID:")
    request_id_label.pack()
    request_id_entry = Entry(update_window)
    request_id_entry.pack()
    new_status_label = Label(update_window, text="New Status:")
    new_status_label.pack()
    new_status_entry = Entry(update_window)
    new_status_entry.pack()
    submit_button = Button(update_window, text="Update", command=lambda: update_request_data(
        request_id_entry.get(), new_status_entry.get()
    ))
    submit_button.pack()

def open_delete_request_window():
    delete_window = Toplevel(root)
    delete_window.geometry("300x200")
    request_id_label = Label(delete_window, text="Request ID:")
    request_id_label.pack()
    request_id_entry = Entry(delete_window)
    request_id_entry.pack()
    submit_button = Button(delete_window, text="Delete", command=lambda: delete_request_data(request_id_entry.get()))
    submit_button.pack()

root = Tk()
root.geometry("700x700")
insert_button = Button(root, text="Insert Request", command=open_insert_request_window)
insert_button.pack()
display_button = Button(root, text="Display Request Records", command=display_request_records)
display_button.pack()
update_button = Button(root, text="Update Request", command=open_update_request_window)
update_button.pack()
delete_button = Button(root, text="Delete Request", command=open_delete_request_window)
delete_button.pack()
root.mainloop()
