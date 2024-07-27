from tkinter import Tk, Frame, Label, Button, ttk, Scrollbar
from ui_components import create_button, create_entry, create_label
from mysql_conn import create_connection, create_database_if_not_exists, create_tables_if_not_exists
from inventory import inventory_buttons
from turtle import back, bgcolor, clear
import mysql.connector as c


def main_window(root):
    groceryStore = create_label(root, "GROCERY STORE", 625, 87, fg="black", bg="beige", font="Gabriola 45 bold")
    
    global entry1, entry2
    entry1 = create_entry(root, 800, 300)
    create_label(root, "Enter Grocery Store Name:", 600, 300)
    
    entry2 = create_entry(root, 800, 350, show="*")
    create_label(root, "Enter your Database Password:", 600, 350)
    
    access_button = create_button(root, 800, 400, "Access", "cyan", "black", access)
    
    return groceryStore, entry1, entry2, access_button


def access():
    E2 = entry2.get()
    conn = create_connection(E2)
    
    if conn:

        mycsr = conn.cursor()
        # Create database and tables if they do not exist
        create_database_if_not_exists(conn, "grocery_store")
        create_tables_if_not_exists(conn)
        
        # Create a new frame for further operations
        f0 = Frame()
        f0.place(x=0, y=0, width=1600, height=900)
        f0.configure(bg="beige")
        
        # Create a back button to return to the main window
        back_button = create_button(f0, 0, 0, "<--", 'cyan', 'black', lambda: f0.destroy(), width=21, height=2)
        
        # Add more components or logic for the new frame
        # For example, you might want to add buttons for different inventory categories
        # Example: create_inventory_buttons(f0, conn)
        inventory_buttons(f0, mycsr, conn)
    else:
        # Handle connection failure
        error_label = Label(root, text="Failed to connect to the database.", fg="red", bg="beige", font="Times")
        error_label.place(x=800, y=450)



root = Tk()
root.geometry("1600x900")
main_window(root)
root.mainloop()