import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MS-msMarie27Rroaa22",
    database="Restaurant1"
)

refund_id_entry = None
order_id_entry = None
refund_amount_entry = None
refund_date_entry = None
reason_entry = None

def insert_refund_data(refund_id, order_id, refund_amount, refund_date, reason):
    refund_id = refund_id_entry.get()
    order_id = order_id_entry.get()
    refund_amount = refund_amount_entry.get()
    refund_date = refund_date_entry.get()
    reason = reason_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO CustomerRefund (RefundID, OrderID, RefundAmount, RefundDate, Reason) VALUES (%s, %s, %s, %s, %s)"
    val = (refund_id, order_id, refund_amount, refund_date, reason)

    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def fetch_refund_records():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT RefundID, OrderID FROM CustomerRefund")
    records = mycursor.fetchall()
    mycursor.close()
    return records

def display_refund_records():
    records = fetch_refund_records()
    display_window = Toplevel(root)
    display_window.geometry("700x700")
    listbox = Listbox(display_window, width = 350, height = 350)
    listbox.pack()
    for record in records:
        listbox.insert(END, f"Refund ID: {record[0]}, Order ID: {record[1]}")

def delete_refund_data(refund_id):
    mycursor = mydb.cursor()

    try:
        mycursor.execute("DELETE FROM CustomerRefund WHERE RefundID = %s", (refund_id,))
        mydb.commit()

        print("Delete successful")
    except Exception as e:
        print(f"Error deleting data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def open_insert_refund_window():
    insert_window = Toplevel(root)
    insert_window.geometry("500x500")
    global refund_id_entry, order_id_entry, refund_amount_entry, refund_date_entry, reason_entry
    refund_id_label = Label(insert_window, text="Refund ID:")
    refund_id_label.pack()
    refund_id_entry = Entry(insert_window)
    refund_id_entry.pack()
    order_id_label = Label(insert_window, text="Order ID:")
    order_id_label.pack()
    order_id_entry = Entry(insert_window)
    order_id_entry.pack()
    refund_amount_label = Label(insert_window, text="Refund Amount:")
    refund_amount_label.pack()
    refund_amount_entry = Entry(insert_window)
    refund_amount_entry.pack()
    refund_date_label = Label(insert_window, text="Refund Date:")
    refund_date_label.pack()
    refund_date_entry = Entry(insert_window)
    refund_date_entry.pack()
    reason_label = Label(insert_window, text="Reason:")
    reason_label.pack()
    reason_entry = Entry(insert_window)
    reason_entry.pack()
    submit_button = Button(insert_window, text="Insert", command=lambda: insert_refund_data(refund_id_entry.get(), order_id_entry.get(), refund_amount_entry.get(), refund_date_entry.get(), reason_entry.get()))
    submit_button.pack()

def open_delete_refund_window():
    delete_window = Toplevel(root)
    delete_window.geometry("400x200")
    refund_id_label = Label(delete_window, text="Refund ID:")
    refund_id_label.pack()
    refund_id_entry = Entry(delete_window)
    refund_id_entry.pack()
    submit_button = Button(delete_window, text="Delete", command=lambda: delete_refund_data(refund_id_entry.get()))
    submit_button.pack()

root = Tk()
root.geometry("700x700")

insert_refund_button = Button(root, text="Insert Refund", command=open_insert_refund_window)
insert_refund_button.pack()

display_refund_button = Button(root, text="Display Refund Records", command=display_refund_records)
display_refund_button.pack()

delete_refund_button = Button(root, text="Delete Refund", command=open_delete_refund_window)
delete_refund_button.pack()

root.mainloop()
