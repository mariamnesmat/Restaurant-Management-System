import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MS-msMarie27Rroaa22",
    database="Restaurant1"
)

report_id_entry = None
report_date_entry = None
delivery_area_code_entry = None

def insert_report(report_id, report_date, delivery_area_code):
    mycursor = mydb.cursor()
    sql = "INSERT INTO Report (ReportID, ReportDate, DeliveryAreaCode) VALUES (%s, %s, %s)"
    val = (report_id, report_date, delivery_area_code)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def fetch_reports():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ReportID, ReportDate, DeliveryAreaCode FROM Report")
    reports = mycursor.fetchall()
    mycursor.close()
    return reports

def display_reports():
    reports = fetch_reports()
    display_window = Toplevel(root)
    display_window.geometry("700x700")
    listbox = Listbox(display_window, width = 350, height = 350)
    listbox.pack()
    for report in reports:
        listbox.insert(END, f"ID: {report[0]}, Date: {report[1]}, Area Code: {report[2]}")

def update_report(report_id, new_date):
    mycursor = mydb.cursor()
    sql = "UPDATE Report SET ReportDate = %s WHERE ReportID = %s"
    val = (new_date, report_id)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Update successful")
    except Exception as e:
        print(f"Error updating data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def delete_report(report_id):
    mycursor = mydb.cursor()

    try:
        mycursor.execute("DELETE FROM Report WHERE ReportID = %s", (report_id,))
        mydb.commit()
        print("Delete successful")
    except Exception as e:
        print(f"Error deleting data: {e}")
        mydb.rollback()
    finally:
        mycursor.close()

def open_insert_report_window():
    insert_window = Toplevel(root)
    insert_window.geometry("500x500")
    global report_id_entry, report_date_entry, delivery_area_code_entry
    report_id_label = Label(insert_window, text="Report ID:")
    report_id_label.pack()
    report_id_entry = Entry(insert_window)
    report_id_entry.pack()
    report_date_label = Label(insert_window, text="Report Date:")
    report_date_label.pack()
    report_date_entry = Entry(insert_window)
    report_date_entry.pack()
    delivery_area_code_label = Label(insert_window, text="Delivery Area Code:")
    delivery_area_code_label.pack()
    delivery_area_code_entry = Entry(insert_window)
    delivery_area_code_entry.pack()
    submit_button = Button(insert_window, text="Insert", command=lambda: insert_report(report_id_entry.get(), report_date_entry.get(), delivery_area_code_entry.get()))
    submit_button.pack()

def open_update_report_window():
    update_window = Toplevel(root)
    update_window.geometry("700x700")
    report_id_label = Label(update_window, text="Report ID:")
    report_id_label.pack()
    report_id_entry = Entry(update_window)
    report_id_entry.pack()
    new_date_label = Label(update_window, text="New Date:")
    new_date_label.pack()
    new_date_entry = Entry(update_window)
    new_date_entry.pack()
    submit_button = Button(update_window, text="Update", command=lambda: update_report(report_id_entry.get(), new_date_entry.get()))
    submit_button.pack()

def open_delete_report_window():
    delete_window = Toplevel(root)
    delete_window.geometry("400x200")
    report_id_label = Label(delete_window, text="Report ID:")
    report_id_label.pack()
    report_id_entry = Entry(delete_window)
    report_id_entry.pack()
    submit_button = Button(delete_window, text="Delete", command=lambda: delete_report(report_id_entry.get()))
    submit_button.pack()

root = Tk()
root.geometry("700x700")
insert_report_button = Button(root, text="Insert Report", command=open_insert_report_window)
insert_report_button.pack()
display_reports_button = Button(root, text="Display Reports", command=display_reports)
display_reports_button.pack()
update_report_button = Button(root, text="Update Report", command=open_update_report_window)
update_report_button.pack()
delete_report_button = Button(root, text="Delete Report", command=open_delete_report_window)
delete_report_button.pack()
root.mainloop()
