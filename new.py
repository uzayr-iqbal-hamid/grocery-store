import tkinter as tk
from tkinter import ttk
import mysql.connector
from mysql.connector import errorcode
from tkinter import messagebox
from ttkthemes import ThemedTk

# Database connection
def initialize_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="uzayrinmysql"
    )
    cursor = connection.cursor()

    # Check if the database exists
    cursor.execute("SHOW DATABASES LIKE 'grocery_store_db'")
    result = cursor.fetchone()

    if not result:
        # Database does not exist, so create it and the tables
        db_setup_sql = """
        CREATE DATABASE IF NOT EXISTS grocery_store_db;
        USE grocery_store_db;
        CREATE TABLE IF NOT EXISTS inventory (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            category VARCHAR(255),
            quantity INT,
            price DECIMAL(10, 2)
        );
        CREATE TABLE IF NOT EXISTS customers (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(20),
            address TEXT
        );
        CREATE TABLE IF NOT EXISTS ledger (
            id INT PRIMARY KEY,
            date DATE,
            details TEXT,
            amount DECIMAL(10, 2)
        );
        CREATE TABLE IF NOT EXISTS bill (
            id INT PRIMARY KEY,
            customer_id INT,
            date DATE,
            total_amount DECIMAL(10, 2),
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        );
        """
        for statement in db_setup_sql.split(';'):
            if statement.strip():
                cursor.execute(statement)
        connection.commit()
        print("Database and tables created successfully.")
    else:
        print("Database already exists.")

    cursor.close()
    connection.close()

# Create a function to establish a connection to the grocery_store_db
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="uzayrinmysql",
        database="grocery_store_db"
    )

# Initialize the main window
def initialize_main_window():
    root = ThemedTk()
    root.title("Grocery Store Management System")
    root.geometry("1200x800")

    root.set_theme("arc") # arc, breeze, clearlooks elegance plastik radiance scidgreen ubuntu alt black clam classic keramik mocha
 
    tab_control = ttk.Notebook(root)

    # Inventory Tab
    inventory_tab = ttk.Frame(tab_control)
    tab_control.add(inventory_tab, text='Inventory')
    create_inventory_tab(inventory_tab)

    # Customers Tab
    customers_tab = ttk.Frame(tab_control)
    tab_control.add(customers_tab, text='Customers')
    create_customers_tab(customers_tab)

    # Ledger Tab
    ledger_tab = ttk.Frame(tab_control)
    tab_control.add(ledger_tab, text='Ledger')
    create_ledger_tab(ledger_tab)

    # Bill Tab
    bill_tab = ttk.Frame(tab_control)
    tab_control.add(bill_tab, text='Bill')
    create_bill_tab(bill_tab)

    tab_control.pack(expand=1, fill='both')

    return root

# Inventory Tab
def create_inventory_tab(tab):
    connection = get_db_connection()
    cursor = connection.cursor()

    def refresh_inventory():
        for item in inventory_tree.get_children():
            inventory_tree.delete(item)
        cursor.execute("SELECT * FROM inventory")
        for row in cursor.fetchall():
            inventory_tree.insert('', 'end', values=row)

    # Treeview for inventory
    inventory_tree = ttk.Treeview(tab, columns=('ID', 'Name', 'Category', 'Quantity', 'Price'), show='headings')
    inventory_tree.heading('ID', text='ID')
    inventory_tree.heading('Name', text='Name')
    inventory_tree.heading('Category', text='Category')
    inventory_tree.heading('Quantity', text='Quantity')
    inventory_tree.heading('Price', text='Price')
    inventory_tree.pack(side=tk.BOTTOM, fill='both', expand=True)

    refresh_inventory()

    # Add Inventory
    def add_inventory():
        id = entry_id.get()
        name = entry_name.get()
        category = entry_category.get()
        quantity = entry_quantity.get()
        price = entry_price.get()
        cursor.execute("INSERT INTO inventory (id, name, category, quantity, price) VALUES (%s, %s, %s, %s, %s)",
                       (id, name, category, quantity, price))
        connection.commit()
        refresh_inventory()
        messagebox.showinfo("Success", "Inventory added successfully")

    # Update Inventory
    def update_inventory():
        try:
            selected_item = inventory_tree.selection()[0]
            values = inventory_tree.item(selected_item, 'values')
            id = values[0]
            name = entry_name.get()
            category = entry_category.get()
            quantity = entry_quantity.get()
            price = entry_price.get()
            cursor.execute("UPDATE inventory SET name=%s, category=%s, quantity=%s, price=%s WHERE id=%s",
                           (name, category, quantity, price, id))
            connection.commit()
            refresh_inventory()
            messagebox.showinfo("Success", "Inventory updated successfully")
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item to update")

    # Delete Inventory
    def delete_inventory():
        try:
            selected_item = inventory_tree.selection()[0]
            values = inventory_tree.item(selected_item, 'values')
            id = values[0]
            cursor.execute("DELETE FROM inventory WHERE id=%s", (id,))
            connection.commit()
            refresh_inventory()
            messagebox.showinfo("Success", "Inventory deleted successfully")
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item to delete")

    # Search Inventory
    def search_inventory():
        search_term = entry_search.get()
        for item in inventory_tree.get_children():
            inventory_tree.delete(item)
        cursor.execute("SELECT * FROM inventory WHERE name LIKE %s OR category LIKE %s", 
                       ('%' + search_term + '%', '%' + search_term + '%'))
        for row in cursor.fetchall():
            inventory_tree.insert('', 'end', values=row)

    # Input fields and buttons
    input_frame = tk.Frame(tab)
    input_frame.pack(side=tk.TOP, fill=tk.X)

    tk.Label(input_frame, text='ID').grid(row=0, column=0)
    entry_id = tk.Entry(input_frame)
    entry_id.grid(row=0, column=1)
    
    tk.Label(input_frame, text='Name').grid(row=1, column=0)
    entry_name = tk.Entry(input_frame)
    entry_name.grid(row=1, column=1)
    
    tk.Label(input_frame, text='Category').grid(row=2, column=0)
    entry_category = tk.Entry(input_frame)
    entry_category.grid(row=2, column=1)
    
    tk.Label(input_frame, text='Quantity').grid(row=3, column=0)
    entry_quantity = tk.Entry(input_frame)
    entry_quantity.grid(row=3, column=1)
    
    tk.Label(input_frame, text='Price').grid(row=4, column=0)
    entry_price = tk.Entry(input_frame)
    entry_price.grid(row=4, column=1)

    tk.Button(input_frame, text='Add Inventory', command=add_inventory).grid(row=5, column=0)
    tk.Button(input_frame, text='Update Inventory', command=update_inventory).grid(row=5, column=1)
    tk.Button(input_frame, text='Delete Inventory', command=delete_inventory).grid(row=5, column=2)

    # Search
    search_frame = tk.Frame(tab)
    search_frame.pack(side=tk.TOP, fill=tk.X)

    tk.Label(search_frame, text='Search').pack(side=tk.LEFT)
    entry_search = tk.Entry(search_frame)
    entry_search.pack(side=tk.LEFT)
    tk.Button(search_frame, text='Search', command=search_inventory).pack(side=tk.LEFT)

    # View All Records button
    view_all_button = tk.Button(tab, text='View All Records', command=refresh_inventory)
    view_all_button.pack(side=tk.BOTTOM, pady=10)

# Customers Tab
def create_customers_tab(tab):
    connection = get_db_connection()
    cursor = connection.cursor()

    def refresh_customers():
        for item in customers_tree.get_children():
            customers_tree.delete(item)
        cursor.execute("SELECT * FROM customers")
        for row in cursor.fetchall():
            customers_tree.insert('', 'end', values=row)

    # Treeview for customers
    customers_tree = ttk.Treeview(tab, columns=('ID', 'Name', 'Email', 'Phone', 'Address'), show='headings')
    customers_tree.heading('ID', text='ID')
    customers_tree.heading('Name', text='Name')
    customers_tree.heading('Email', text='Email')
    customers_tree.heading('Phone', text='Phone')
    customers_tree.heading('Address', text='Address')
    customers_tree.pack(side=tk.BOTTOM, fill='both', expand=True)

    refresh_customers()

    # Add Customer
    def add_customer():
        id = entry_id.get()
        name = entry_name.get()
        email = entry_email.get()
        phone = entry_phone.get()
        address = entry_address.get()
        cursor.execute("INSERT INTO customers (id, name, email, phone, address) VALUES (%s, %s, %s, %s, %s)",
                       (id, name, email, phone, address))
        connection.commit()
        refresh_customers()
        messagebox.showinfo("Success", "Customer added successfully")

    # Update Customer
    def update_customer():
        try:
            selected_item = customers_tree.selection()[0]
            values = customers_tree.item(selected_item, 'values')
            id = values[0]
            name = entry_name.get()
            email = entry_email.get()
            phone = entry_phone.get()
            address = entry_address.get()
            cursor.execute("UPDATE customers SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s",
                           (name, email, phone, address, id))
            connection.commit()
            refresh_customers()
            messagebox.showinfo("Success", "Customer updated successfully")
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item to update")

    # Delete Customer
    def delete_customer():
        try:
            selected_item = customers_tree.selection()[0]
            values = customers_tree.item(selected_item, 'values')
            id = values[0]
            cursor.execute("DELETE FROM customers WHERE id=%s", (id,))
            connection.commit()
            refresh_customers()
            messagebox.showinfo("Success", "Customer deleted successfully")
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item to delete")

    # Search Customer
    def search_customer():
        search_term = entry_search.get()
        for item in customers_tree.get_children():
            customers_tree.delete(item)
        cursor.execute("SELECT * FROM customers WHERE name LIKE %s OR email LIKE %s OR phone LIKE %s OR address LIKE %s", 
                       ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        for row in cursor.fetchall():
            customers_tree.insert('', 'end', values=row)

    # Input fields and buttons
    input_frame = tk.Frame(tab)
    input_frame.pack(side=tk.TOP, fill=tk.X)

    tk.Label(input_frame, text='ID').grid(row=0, column=0)
    entry_id = tk.Entry(input_frame)
    entry_id.grid(row=0, column=1)
    
    tk.Label(input_frame, text='Name').grid(row=1, column=0)
    entry_name = tk.Entry(input_frame)
    entry_name.grid(row=1, column=1)
    
    tk.Label(input_frame, text='Email').grid(row=2, column=0)
    entry_email = tk.Entry(input_frame)
    entry_email.grid(row=2, column=1)
    
    tk.Label(input_frame, text='Phone').grid(row=3, column=0)
    entry_phone = tk.Entry(input_frame)
    entry_phone.grid(row=3, column=1)
    
    tk.Label(input_frame, text='Address').grid(row=4, column=0)
    entry_address = tk.Entry(input_frame)
    entry_address.grid(row=4, column=1)

    tk.Button(input_frame, text='Add Customer', command=add_customer).grid(row=5, column=0)
    tk.Button(input_frame, text='Update Customer', command=update_customer).grid(row=5, column=1)
    tk.Button(input_frame, text='Delete Customer', command=delete_customer).grid(row=5, column=2)

    # Search
    search_frame = tk.Frame(tab)
    search_frame.pack(side=tk.TOP, fill=tk.X)

    tk.Label(search_frame, text='Search').pack(side=tk.LEFT)
    entry_search = tk.Entry(search_frame)
    entry_search.pack(side=tk.LEFT)
    tk.Button(search_frame, text='Search', command=search_customer).pack(side=tk.LEFT)

    # View All Records button
    view_all_button = tk.Button(tab, text='View All Records', command=refresh_customers)
    view_all_button.pack(side=tk.BOTTOM, pady=10)

# Ledger Tab
def create_ledger_tab(tab):
    connection = get_db_connection()
    cursor = connection.cursor()

    def refresh_ledger():
        for item in ledger_tree.get_children():
            ledger_tree.delete(item)
        cursor.execute("SELECT * FROM ledger")
        for row in cursor.fetchall():
            ledger_tree.insert('', 'end', values=row)

    # Treeview for ledger
    ledger_tree = ttk.Treeview(tab, columns=('ID', 'Date', 'Details', 'Amount'), show='headings')
    ledger_tree.heading('ID', text='ID')
    ledger_tree.heading('Date', text='Date')
    ledger_tree.heading('Details', text='Details')
    ledger_tree.heading('Amount', text='Amount')
    ledger_tree.pack(side=tk.BOTTOM, fill='both', expand=True)

    refresh_ledger()

    # Add Ledger Entry
    def add_ledger_entry():
        id = entry_id.get()
        date = entry_date.get()
        details = entry_details.get()
        amount = entry_amount.get()
        cursor.execute("INSERT INTO ledger (id, date, details, amount) VALUES (%s, %s, %s, %s)",
                       (id, date, details, amount))
        connection.commit()
        refresh_ledger()
        messagebox.showinfo("Success", "Ledger entry added successfully")

    # Update Ledger Entry
    def update_ledger_entry():
        try:
            selected_item = ledger_tree.selection()[0]
            values = ledger_tree.item(selected_item, 'values')
            id = values[0]
            date = entry_date.get()
            details = entry_details.get()
            amount = entry_amount.get()
            cursor.execute("UPDATE ledger SET date=%s, details=%s, amount=%s WHERE id=%s",
                           (date, details, amount, id))
            connection.commit()
            refresh_ledger()
            messagebox.showinfo("Success", "Ledger entry updated successfully")
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item to update")

    # Delete Ledger Entry
    def delete_ledger_entry():
        try:
            selected_item = ledger_tree.selection()[0]
            values = ledger_tree.item(selected_item, 'values')
            id = values[0]
            cursor.execute("DELETE FROM ledger WHERE id=%s", (id,))
            connection.commit()
            refresh_ledger()
            messagebox.showinfo("Success", "Ledger entry deleted successfully")
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item to delete")

    # Search Ledger Entry
    def search_ledger_entry():
        search_term = entry_search.get()
        for item in ledger_tree.get_children():
            ledger_tree.delete(item)
        cursor.execute("SELECT * FROM ledger WHERE details LIKE %s", 
                       ('%' + search_term + '%',))
        for row in cursor.fetchall():
            ledger_tree.insert('', 'end', values=row)

    # Input fields and buttons
    input_frame = tk.Frame(tab)
    input_frame.pack(side=tk.TOP, fill=tk.X)

    tk.Label(input_frame, text='ID').grid(row=0, column=0)
    entry_id = tk.Entry(input_frame)
    entry_id.grid(row=0, column=1)
    
    tk.Label(input_frame, text='Date').grid(row=1, column=0)
    entry_date = tk.Entry(input_frame)
    entry_date.grid(row=1, column=1)
    
    tk.Label(input_frame, text='Details').grid(row=2, column=0)
    entry_details = tk.Entry(input_frame)
    entry_details.grid(row=2, column=1)
    
    tk.Label(input_frame, text='Amount').grid(row=3, column=0)
    entry_amount = tk.Entry(input_frame)
    entry_amount.grid(row=3, column=1)

    tk.Button(input_frame, text='Add Ledger Entry', command=add_ledger_entry).grid(row=4, column=0)
    tk.Button(input_frame, text='Update Ledger Entry', command=update_ledger_entry).grid(row=4, column=1)
    tk.Button(input_frame, text='Delete Ledger Entry', command=delete_ledger_entry).grid(row=4, column=2)

    # Search
    search_frame = tk.Frame(tab)
    search_frame.pack(side=tk.TOP, fill=tk.X)

    tk.Label(search_frame, text='Search').pack(side=tk.LEFT)
    entry_search = tk.Entry(search_frame)
    entry_search.pack(side=tk.LEFT)
    tk.Button(search_frame, text='Search', command=search_ledger_entry).pack(side=tk.LEFT)

    # View All Records button
    view_all_button = tk.Button(tab, text='View All Records', command=refresh_ledger)
    view_all_button.pack(side=tk.BOTTOM, pady=10)

# Bill Tab
def create_bill_tab(tab):
    connection = get_db_connection()
    cursor = connection.cursor()

    def refresh_bills():
        for item in bill_tree.get_children():
            bill_tree.delete(item)
        cursor.execute("SELECT * FROM bill")
        for row in cursor.fetchall():
            bill_tree.insert('', 'end', values=row)

    # Treeview for bills
    bill_tree = ttk.Treeview(tab, columns=('ID', 'Customer ID', 'Date', 'Total Amount'), show='headings')
    bill_tree.heading('ID', text='ID')
    bill_tree.heading('Customer ID', text='Customer ID')
    bill_tree.heading('Date', text='Date')
    bill_tree.heading('Total Amount', text='Total Amount')
    bill_tree.pack(side=tk.BOTTOM, fill='both', expand=True)

    refresh_bills()

    # Add Bill
    def add_bill():
        id = entry_id.get()
        customer_id = entry_customer_id.get()
        date = entry_date.get()
        total_amount = entry_total_amount.get()
        cursor.execute("INSERT INTO bill (id, customer_id, date, total_amount) VALUES (%s, %s, %s, %s)",
                       (id, customer_id, date, total_amount))
        connection.commit()
        refresh_bills()
        messagebox.showinfo("Success", "Bill added successfully")

    # Update Bill
    def update_bill():
        try:
            selected_item = bill_tree.selection()[0]
            values = bill_tree.item(selected_item, 'values')
            id = values[0]
            customer_id = entry_customer_id.get()
            date = entry_date.get()
            total_amount = entry_total_amount.get()
            cursor.execute("UPDATE bill SET customer_id=%s, date=%s, total_amount=%s WHERE id=%s",
                           (customer_id, date, total_amount, id))
            connection.commit()
            refresh_bills()
            messagebox.showinfo("Success", "Bill updated successfully")
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item to update")

    # Delete Bill
    def delete_bill():
        try:
            selected_item = bill_tree.selection()[0]
            values = bill_tree.item(selected_item, 'values')
            id = values[0]
            cursor.execute("DELETE FROM bill WHERE id=%s", (id,))
            connection.commit()
            refresh_bills()
            messagebox.showinfo("Success", "Bill deleted successfully")
        except IndexError:
            messagebox.showwarning("Warning", "Please select an item to delete")

    # Search Bill
    def search_bill():
        search_term = entry_search.get()
        for item in bill_tree.get_children():
            bill_tree.delete(item)
        cursor.execute("SELECT * FROM bill WHERE id LIKE %s OR customer_id LIKE %s", 
                       ('%' + search_term + '%', '%' + search_term + '%'))
        for row in cursor.fetchall():
            bill_tree.insert('', 'end', values=row)

    # Input fields and buttons
    input_frame = tk.Frame(tab)
    input_frame.pack(side=tk.TOP, fill=tk.X)

    tk.Label(input_frame, text='ID').grid(row=0, column=0)
    entry_id = tk.Entry(input_frame)
    entry_id.grid(row=0, column=1)
    
    tk.Label(input_frame, text='Customer ID').grid(row=1, column=0)
    entry_customer_id = tk.Entry(input_frame)
    entry_customer_id.grid(row=1, column=1)
    
    tk.Label(input_frame, text='Date').grid(row=2, column=0)
    entry_date = tk.Entry(input_frame)
    entry_date.grid(row=2, column=1)
    
    tk.Label(input_frame, text='Total Amount').grid(row=3, column=0)
    entry_total_amount = tk.Entry(input_frame)
    entry_total_amount.grid(row=3, column=1)

    tk.Button(input_frame, text='Add Bill', command=add_bill).grid(row=4, column=0)
    tk.Button(input_frame, text='Update Bill', command=update_bill).grid(row=4, column=1)
    tk.Button(input_frame, text='Delete Bill', command=delete_bill).grid(row=4, column=2)

    # Search
    search_frame = tk.Frame(tab)
    search_frame.pack(side=tk.TOP, fill=tk.X)

    tk.Label(search_frame, text='Search').pack(side=tk.LEFT)
    entry_search = tk.Entry(search_frame)
    entry_search.pack(side=tk.LEFT)
    tk.Button(search_frame, text='Search', command=search_bill).pack(side=tk.LEFT)

    # View All Records button
    view_all_button = tk.Button(tab, text='View All Records', command=refresh_bills)
    view_all_button.pack(side=tk.BOTTOM, pady=10)

# Main execution
if __name__ == "__main__":
    initialize_database()
    root = initialize_main_window()
    root.mainloop()
