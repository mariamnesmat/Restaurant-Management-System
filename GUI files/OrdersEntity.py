import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MS-msMarie27Rroaa22",
    database="Restaurant1"
)

order_id_entry = None
customer_id_entry = None
restaurant_id_entry = None
delivery_boy_id_entry = None
delivery_area_entry = None
OrderDate_entry = None
order_status_entry = None
total_amount_entry = None

def insert_order_data(order_id, customer_id, restaurant_id, delivery_boy_id, delivery_area, OrderDate, order_status, total_amount):
    order_id = order_id_entry.get()
    customer_id = customer_id_entry.get()
    restaurant_id = restaurant_id_entry.get()
    delivery_boy_id = delivery_boy_id_entry.get()
    delivery_area = delivery_area_entry.get()
    OrderDate = OrderDate_entry.get()
    order_status = order_status_entry.get()
    total_amount = total_amount_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO Orders (OrderID, CustomerID, RestaurantID, DeliveryBoyID, delivery_area,OrderDate, Orderstatus, total_amount) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"
    val = (order_id, customer_id, restaurant_id, delivery_boy_id, delivery_area, OrderDate,order_status, total_amount)
    
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def fetch_order_records():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Orders")
    records = mycursor.fetchall()
    mycursor.close()
    return records

def display_order_records():
    records = fetch_order_records()
    display_window = Toplevel(root)
    display_window.geometry("700x700")
    listbox = Listbox(display_window, width = 150, height = 150)
    listbox.pack()
    for record in records:
        listbox.insert(END, f"OrderID: {record[0]}, CustomerID: {record[1]}, RestaurantID: {record[2]}, DeliveryBoyID: {record[3]}, DeliveryArea: {record[4]}, OrderDate: {record[5]},OrderStatus: {record[6]}, TotalAmount: {record[7]}")

def update_order_data(order_id, new_order_status):
    mycursor = mydb.cursor()
    sql = "UPDATE Orders SET Orderstatus = %s WHERE OrderID = %s"
    val = (new_order_status, order_id)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def delete_order_data(order_id):
    mycursor = mydb.cursor()

    try:
        mycursor.execute("DELETE FROM Orders WHERE OrderID = %s", (order_id,))
        mydb.commit()
        print("Delete successful")
    except Exception as e:
        print(f"Error deleting data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def open_insert_order_window():
    insert_window = Toplevel(root)
    insert_window.geometry("400x300")
    global order_id_entry, customer_id_entry, restaurant_id_entry, delivery_boy_id_entry, delivery_area_entry, OrderDate_entry,order_status_entry, total_amount_entry

    order_id_label = Label(insert_window, text="Order ID:")
    order_id_label.pack()
    order_id_entry = Entry(insert_window)
    order_id_entry.pack()

    customer_id_label = Label(insert_window, text="Customer ID:")
    customer_id_label.pack()
    customer_id_entry = Entry(insert_window)
    customer_id_entry.pack()

    restaurant_id_label = Label(insert_window, text="Restaurant ID:")
    restaurant_id_label.pack()
    restaurant_id_entry = Entry(insert_window)
    restaurant_id_entry.pack()

    delivery_boy_id_label = Label(insert_window, text="Delivery Boy ID:")
    delivery_boy_id_label.pack()
    delivery_boy_id_entry = Entry(insert_window)
    delivery_boy_id_entry.pack()

    delivery_area_label = Label(insert_window, text="Delivery Area:")
    delivery_area_label.pack()
    delivery_area_entry = Entry(insert_window)
    delivery_area_entry.pack()

    OrderDate_label = Label(insert_window, text="Order date:")
    OrderDate_label.pack()
    OrderDate_entry = Entry(insert_window)
    OrderDate_entry.pack()
    
    order_status_label = Label(insert_window, text="Order Status:")
    order_status_label.pack()
    order_status_entry = Entry(insert_window)
    order_status_entry.pack()

    total_amount_label = Label(insert_window, text="Total Amount:")
    total_amount_label.pack()
    total_amount_entry = Entry(insert_window)
    total_amount_entry.pack()

    submit_button = Button(insert_window, text="Insert", command=lambda: insert_order_data(order_id_entry.get(), customer_id_entry.get(), restaurant_id_entry.get(), delivery_boy_id_entry.get(), delivery_area_entry.get(), OrderDate_entry.get(), order_status_entry.get(), total_amount_entry.get()))
    submit_button.pack()

def open_update_order_window():
    update_window = Toplevel(root)
    update_window.geometry("400x200")
    order_id_label = Label(update_window, text="Order ID:")
    order_id_label.pack()
    order_id_entry = Entry(update_window)
    order_id_entry.pack()
    new_order_status_label = Label(update_window, text="New Order Status:")
    new_order_status_label.pack()
    new_order_status_entry = Entry(update_window)
    new_order_status_entry.pack()
    submit_button = Button(update_window, text="Update", command=lambda: update_order_data(order_id_entry.get(), new_order_status_entry.get()))
    submit_button.pack()

def open_delete_order_window():
    delete_window = Toplevel(root)
    delete_window.geometry("300x100")
    order_id_label = Label(delete_window, text="Order ID:")
    order_id_label.pack()
    order_id_entry = Entry(delete_window)
    order_id_entry.pack()
    submit_button = Button(delete_window, text="Delete", command=lambda: delete_order_data(order_id_entry.get()))
    submit_button.pack()

root = Tk()
root.geometry("600x400")

insert_button = Button(root, text="Insert Order", command=open_insert_order_window)
insert_button.pack()
display_button = Button(root, text="Display Order Records", command=display_order_records)
display_button.pack()
update_button = Button(root, text="Update Order", command=open_update_order_window)
update_button.pack()
delete_button = Button(root, text="Delete Order", command=open_delete_order_window)
delete_button.pack()

root.mainloop()
