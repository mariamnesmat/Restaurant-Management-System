import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MS-msMarie27Rroaa22",
    database="Restaurant1"
)

customer_id_entry = None
customer_name_entry = None
email_entry = None
phone_number_entry = None
address_entry = None
premium_status_entry = None
discounts_entry = None

def insert_customer_data(customer_id, customer_name, email, phone_number, address, premium_status, discounts):
    customer_id = customer_id_entry.get()
    customer_name = customer_name_entry.get()
    email = email_entry.get()
    phone_number = phone_number_entry.get()
    address = address_entry.get()
    premium_status = premium_status_entry.get()
    discounts = discounts_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO Customer (CustomerID, customer_name, email, phone_number, address, premium_status, discounts) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (customer_id, customer_name, email, phone_number, address, premium_status, discounts)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def fetch_customer_records():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT CustomerID, customer_name, phone_number, address, discounts FROM Customer")
    records = mycursor.fetchall()
    mycursor.close()
    return records

def display_customer_records():
    records = fetch_customer_records()
    display_window = Toplevel(root)
    display_window.geometry("600x600")
    listbox = Listbox(display_window, height = 120, width = 200)
    listbox.pack()
    for record in records:
        listbox.insert(END, f"ID: {record[0]}, Name: {record[1]}, Phone: {record[2]},  Address: {record[3]} , Discount: {record[4]}")

def open_insert_customer_window():
    insert_window = Toplevel(root)
    insert_window.geometry("500x500")
    global customer_id_entry, customer_name_entry, email_entry, phone_number_entry, address_entry, premium_status_entry, discounts_entry

    customer_id_label = Label(insert_window, text="Customer ID:")
    customer_id_label.pack()
    customer_id_entry = Entry(insert_window)
    customer_id_entry.pack()

    customer_name_label = Label(insert_window, text="Customer Name:")
    customer_name_label.pack()
    customer_name_entry = Entry(insert_window)
    customer_name_entry.pack()

    email_label = Label(insert_window, text="Email:")
    email_label.pack()
    email_entry = Entry(insert_window)
    email_entry.pack()

    phone_number_label = Label(insert_window, text="Phone Number:")
    phone_number_label.pack()
    phone_number_entry = Entry(insert_window)
    phone_number_entry.pack()

    address_label = Label(insert_window, text="Address:")
    address_label.pack()
    address_entry = Entry(insert_window)
    address_entry.pack()

    premium_status_label = Label(insert_window, text="Premium Status:")
    premium_status_label.pack()
    premium_status_entry = Entry(insert_window)
    premium_status_entry.pack()

    discounts_label = Label(insert_window, text="Discounts:")
    discounts_label.pack()
    discounts_entry = Entry(insert_window)
    discounts_entry.pack()

    submit_button = Button(insert_window, text="Insert", command=lambda: insert_customer_data(
        customer_id_entry.get(), customer_name_entry.get(), email_entry.get(), phone_number_entry.get(),
        address_entry.get(), premium_status_entry.get(), discounts_entry.get()))
    submit_button.pack()

def open_update_premium_status_window():
    update_window = Toplevel(root)
    update_window.geometry("400x200")

    customer_id_label = Label(update_window, text="Customer ID:")
    customer_id_label.pack()
    customer_id_entry = Entry(update_window)
    customer_id_entry.pack()

    new_premium_status_label = Label(update_window, text="New Premium Status:")
    new_premium_status_label.pack()
    new_premium_status_entry = Entry(update_window)
    new_premium_status_entry.pack()

    submit_button = Button(update_window, text="Update Premium Status", command=lambda: update_premium_status(
        customer_id_entry.get(), new_premium_status_entry.get()))
    submit_button.pack()

def update_premium_status(customer_id, new_premium_status):
    mycursor = mydb.cursor()
    sql = "UPDATE Customer SET premium_status = %s WHERE CustomerID = %s"
    val = (new_premium_status, customer_id)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating premium status: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def open_select_data_window(discounts_value):
    select_window = Toplevel(root)
    select_window.geometry("500x300")

    select_label = Label(select_window, text=f"Select Customers where discounts = {discounts_value}")
    select_label.pack()

    mycursor = mydb.cursor()
    sql = f"SELECT * FROM Customer WHERE discounts = {discounts_value}"
    mycursor.execute(sql)
    records = mycursor.fetchall()
    mycursor.close()

    listbox = Listbox(select_window, width = 50, height = 100)
    listbox.pack()
    for record in records:
        listbox.insert(END, f"ID: {record[0]}, Name: {record[1]}, Email: {record[2]}, Phone: {record[3]}, Address: {record[4]}, Premium Status: {record[5]}, Discounts: {record[6]}")

root = Tk()
root.geometry("700x700")

insert_button = Button(root, text="Insert Customer", command=open_insert_customer_window)
insert_button.pack()

display_button = Button(root, text="Display Customer Records", command=display_customer_records)
display_button.pack()

update_premium_status_button = Button(root, text="Update Premium Status", command=open_update_premium_status_window)
update_premium_status_button.pack()

select_data_button = Button(root, text="Select Customers with Discounts", command=lambda: open_select_data_window(0.1))
select_data_button.pack()

root.mainloop()
