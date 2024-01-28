import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MS-msMarie27Rroaa22",
    database="Restaurant1"
)

payment_id_entry = None
order_id_entry = None
amount_entry = None
payment_date_entry = None


def insert_payment_data(payment_id, order_id, amount, payment_date):
    payment_id = payment_id_entry.get()
    order_id = order_id_entry.get()
    amount = amount_entry.get()
    payment_date = payment_date_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO Payment (PaymentID, OrderID, Amount, PaymentDate) VALUES (%s, %s, %s, %s)"
    val = (payment_id, order_id, amount, payment_date)

    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Insert successful")
    except Exception as e:
        print(f"Error inserting data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()


def fetch_payment_records():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT PaymentID, OrderID, Amount, PaymentDate FROM Payment")
    records = mycursor.fetchall()
    mycursor.close()
    return records


def display_payment_records():
    records = fetch_payment_records()
    display_window = Toplevel(root)
    display_window.geometry("400x300")
    listbox = Listbox(display_window, height = 200, width = 200)
    listbox.pack()
    for record in records:
        listbox.insert(END, f"PaymentID: {record[0]}, OrderID: {record[1]}, Amount: {record[2]}, PaymentDate: {record[3]}")


def update_payment_data(payment_id, new_amount):
    mycursor = mydb.cursor()
    sql = "UPDATE Payment SET Amount = %s WHERE PaymentID = %s"
    val = (new_amount, payment_id)

    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()


def delete_payment_data(payment_id):
    mycursor = mydb.cursor()

    try:
        mycursor.execute("DELETE FROM Payment WHERE PaymentID = %s", (payment_id,))
        mydb.commit()
        print("Delete successful")
    except Exception as e:
        print(f"Error deleting data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()


def open_insert_payment_window():
    insert_window = Toplevel(root)
    insert_window.geometry("400x300")
    global payment_id_entry, order_id_entry, amount_entry, payment_date_entry

    payment_id_label = Label(insert_window, text="Payment ID:")
    payment_id_label.pack()
    payment_id_entry = Entry(insert_window)
    payment_id_entry.pack()

    order_id_label = Label(insert_window, text="Order ID:")
    order_id_label.pack()
    order_id_entry = Entry(insert_window)
    order_id_entry.pack()

    amount_label = Label(insert_window, text="Amount:")
    amount_label.pack()
    amount_entry = Entry(insert_window)
    amount_entry.pack()

    payment_date_label = Label(insert_window, text="Payment Date:")
    payment_date_label.pack()
    payment_date_entry = Entry(insert_window)
    payment_date_entry.pack()

    submit_button = Button(insert_window, text="Insert", command=lambda: insert_payment_data(payment_id_entry.get(), order_id_entry.get(), amount_entry.get(), payment_date_entry.get()))
    submit_button.pack()


def open_update_payment_window():
    update_window = Toplevel(root)
    update_window.geometry("400x200")
    payment_id_label = Label(update_window, text="Payment ID:")
    payment_id_label.pack()
    payment_id_entry = Entry(update_window)
    payment_id_entry.pack()
    new_amount_label = Label(update_window, text="New Amount:")
    new_amount_label.pack()
    new_amount_entry = Entry(update_window)
    new_amount_entry.pack()
    submit_button = Button(update_window, text="Update", command=lambda: update_payment_data(payment_id_entry.get(), new_amount_entry.get()))
    submit_button.pack()


def open_delete_payment_window():
    delete_window = Toplevel(root)
    delete_window.geometry("400x200")
    payment_id_label = Label(delete_window, text="Payment ID:")
    payment_id_label.pack()
    payment_id_entry = Entry(delete_window)
    payment_id_entry.pack()
    submit_button = Button(delete_window, text="Delete", command=lambda: delete_payment_data(payment_id_entry.get()))
    submit_button.pack()


root = Tk()
root.geometry("600x600")

insert_button = Button(root, text="Insert Payment", command=open_insert_payment_window)
insert_button.pack()

display_button = Button(root, text="Display Payment Records", command=display_payment_records)
display_button.pack()

update_button = Button(root, text="Update Payment", command=open_update_payment_window)
update_button.pack()

delete_button = Button(root, text="Delete Payment", command=open_delete_payment_window)
delete_button.pack()

root.mainloop()
