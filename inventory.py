from tkinter import Frame, Label, Entry, Button, Toplevel, ttk
from ui_components import create_button

def inventory_buttons(frame, mycsr, conn):
    categories = ["Cooking Essentials", "Household Supplies", "Stationery", "Snacks", "Beauty Products", "Drinks"]
    
    x, y = 100, 150
    for category in categories:
        create_button(frame, x, y, category, "cyan", "black", lambda cat=category: cook(frame, mycsr, conn, cat))
        y += 60  # Adjust y position for next button


def cook(frame, mycsr, conn, category):
    f2 = Frame(frame)
    f2.place(x=0, y=0, width=1600, height=900)
    f2.configure(bg="beige")

    # Function to return to the previous screen
    def go_back():
        f2.destroy()

    # Back button to return to the previous screen
    back_button = Button(f2, width=21, height=2, text="<--",
                         border=0, fg='cyan', bg='black',
                         activeforeground='black', activebackground='cyan',
                         command=go_back)
    back_button.place(x=0, y=0)

    # Title for the 'cook' section
    title = Label(f2, text=category.upper(), fg="black", bg="beige", font="Gabriola 45 bold")
    title.place(x=600, y=50)

    def add_item():
        add_frame = Toplevel(f2)
        add_frame.title(f"Add {category}")
        add_frame.geometry("400x300")

        Label(add_frame, text="Item Code:").pack()
        item_code_entry = Entry(add_frame)
        item_code_entry.pack()

        Label(add_frame, text="Item Name:").pack()
        item_name_entry = Entry(add_frame)
        item_name_entry.pack()

        Label(add_frame, text="Cost Price:").pack()
        cost_price_entry = Entry(add_frame)
        cost_price_entry.pack()

        Label(add_frame, text="Selling Price:").pack()
        selling_price_entry = Entry(add_frame)
        selling_price_entry.pack()

        Label(add_frame, text="Quantity:").pack()
        quantity_entry = Entry(add_frame)
        quantity_entry.pack()

        Label(add_frame, text="Expiry Date:").pack()
        expiry_date_entry = Entry(add_frame)
        expiry_date_entry.pack()

        def save_item():
            item_code = item_code_entry.get()
            item_name = item_name_entry.get()
            cost_price = int(cost_price_entry.get())
            selling_price = int(selling_price_entry.get())
            quantity = int(quantity_entry.get())
            expiry_date = expiry_date_entry.get()

            table_name = f"inv_{category.lower().replace(' ', '_')}"
            
            mycsr.execute(f"""
                INSERT INTO {table_name} (item_code, item_name, cost_price, selling_price, quantity, expiry_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (item_code, item_name, cost_price, selling_price, quantity, expiry_date))
            conn.commit()
            add_frame.destroy()

        Button(add_frame, text="Save", command=save_item).pack()

    add_button = Button(f2, text="Add Item", command=add_item, width=20, height=2, bg='green', fg='white')
    add_button.place(x=600, y=150)

    # Function to delete items
    def delete_item():
        delete_frame = Toplevel(f2)
        delete_frame.title(f"Delete {category}")
        delete_frame.geometry("300x200")

        Label(delete_frame, text="Enter Item Code to Delete:").pack()
        item_code_entry = Entry(delete_frame)
        item_code_entry.pack()

        def remove_item():
            item_code = item_code_entry.get()
            table_name = f"inv_{category.lower().replace(' ', '_')}"
            mycsr.execute(f"DELETE FROM {table_name} WHERE item_code = %s", (item_code,))
            conn.commit()
            delete_frame.destroy()
            display_items()  # Refresh the items display

        Button(delete_frame, text="Delete", command=remove_item).pack()


    delete_button = Button(f2, text="Delete Item", command=delete_item, width=20, height=2, bg='red', fg='white')
    delete_button.place(x=600, y=250)


    def display_items():
        for widget in f2.winfo_children():
            widget.destroy()

        # Recreate the back button on the display items screen
        back_button = Button(f2, width=21, height=2, text="<--",
                            border=0, fg='cyan', bg='black',
                            activeforeground='black', activebackground='cyan',
                            command=go_back)
        back_button.place(x=0, y=0)

        columns = ('Item Code', 'Item Name', 'Cost Price', 'Selling Price', 'Quantity', 'Expiry Date')
        table = ttk.Treeview(f2, columns=columns, show='headings')
        
        # Define column headings and widths
        column_widths = [120, 200, 120, 120, 120, 150]  # Adjust these values as needed
        for col, width in zip(columns, column_widths):
            table.heading(col, text=col)
            table.column(col, width=width)

        # Get frame width and height
        frame_width = f2.winfo_width()
        frame_height = f2.winfo_height()
        
        # Calculate table position to center it
        table_width = sum(column_widths) + 20  # Adding some padding
        table_height = 600
        x = (frame_width - table_width) // 2
        y = (frame_height - table_height) // 2
        
        # Place table in the center of the frame
        table.place(x=x, y=y, width=table_width, height=table_height)

        # Fetch items from the database and display them in the table
        table_name = f"inv_{category.lower().replace(' ', '_')}"
        mycsr.execute(f"SELECT * FROM {table_name}")
        rows = mycsr.fetchall()
        for row in rows:
            table.insert('', 'end', values=row)



    display_button = Button(f2, text="Display Items", command=display_items, width=20, height=2, bg='blue', fg='white')
    display_button.place(x=600, y=200)



