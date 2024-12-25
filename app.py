import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to check medicine availability
def check_availability():
    medicine_name = medicine_entry.get()
    
    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="pharmacy_db"
    )
    
    cursor = connection.cursor()

    # Query to check if medicine is available
    query = "SELECT medicine_id, name, price, discounted_price, quantity FROM medicines WHERE name = %s AND availability = 1"
    cursor.execute(query, (medicine_name,))
    medicine = cursor.fetchone()

    if medicine:
        # If medicine is available, display its details
        result_text.set(f"Medicine: {medicine[1]}\nPrice: {medicine[2]}\nDiscounted Price: {medicine[3]}\nQuantity: {medicine[4]}")
    else:
        # If not available, check for alternatives
        check_alternatives(cursor, medicine_name)

    connection.close()

# Function to check alternatives if medicine is unavailable
def check_alternatives(cursor, medicine_name):
    query = "SELECT medicine_id FROM medicines WHERE name = %s"
    cursor.execute(query, (medicine_name,))
    org_medicine = cursor.fetchone()

    if org_medicine:
        org_medicine_id = org_medicine[0]
        query = """SELECT m.name, m.discounted_price, m.quantity 
                   FROM alternatives a
                   JOIN medicines m ON a.alt_medicine_id = m.medicine_id
                   WHERE a.org_medicine_id = %s"""
        cursor.execute(query, (org_medicine_id,))
        alternatives = cursor.fetchall()

        if alternatives:
            result_text.set(f"No stock of {medicine_name}. Showing alternatives:\n")
            for alt in alternatives:
                result_text.set(result_text.get() + f"\nAlternative: {alt[0]}, Discounted Price: {alt[1]}, Quantity: {alt[2]}")
        else:
            messagebox.showinfo("Result", "No alternatives available")
    else:
        messagebox.showinfo("Result", f"Medicine {medicine_name} not found.")

# Function to handle billing
def add_to_bill():
    medicine_name = bill_medicine_entry.get()
    quantity = int(bill_quantity_entry.get())

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="pharmacy_db"
    )
    
    cursor = connection.cursor()

    # Query to get the discounted price and current quantity
    query = "SELECT discounted_price, quantity FROM medicines WHERE name = %s"
    cursor.execute(query, (medicine_name,))
    medicine = cursor.fetchone()

    if medicine:
        discounted_price, available_quantity = medicine

        if quantity <= available_quantity:
            total_cost = discounted_price * quantity
            total_bill_text.set(f"Total Bill for {quantity} of {medicine_name}: {total_cost:.2f}")

            # Update the quantity in the database
            new_quantity = available_quantity - quantity
            update_query = "UPDATE medicines SET quantity = %s WHERE name = %s"
            cursor.execute(update_query, (new_quantity, medicine_name))
            connection.commit()
            messagebox.showinfo("Success", f"{quantity} of {medicine_name} purchased successfully!")
        else:
            messagebox.showwarning("Quantity Error", "Requested quantity exceeds available stock.")
    else:
        messagebox.showinfo("Result", f"Medicine {medicine_name} not found.")
    
    connection.close()

# Create main window
root = tk.Tk()
root.title("Pharmacy Availability Checker")

# Set the size of the window
root.geometry("800x600")

# Create input field for checking medicine availability
medicine_label = tk.Label(root, text="Enter Medicine Name:")
medicine_label.pack(pady=5)

medicine_entry = tk.Entry(root, width=50)
medicine_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Availability", command=check_availability, width=20)
check_button.pack(pady=10)

# Create result section
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.pack(pady=10)

# Billing section
billing_label = tk.Label(root, text="Billing Section", font=("Arial", 16))
billing_label.pack(pady=10)

bill_medicine_label = tk.Label(root, text="Enter Medicine Name for Billing:")
bill_medicine_label.pack(pady=5)

bill_medicine_entry = tk.Entry(root, width=50)
bill_medicine_entry.pack(pady=5)

bill_quantity_label = tk.Label(root, text="Enter Quantity:")
bill_quantity_label.pack(pady=5)

bill_quantity_entry = tk.Entry(root, width=10)
bill_quantity_entry.pack(pady=5)

# Add to bill button
add_bill_button = tk.Button(root, text="Add to Bill", command=add_to_bill, width=20)
add_bill_button.pack(pady=10)

# Display total bill
total_bill_text = tk.StringVar()
total_bill_label = tk.Label(root, textvariable=total_bill_text, justify="left")
total_bill_label.pack(pady=10)

# Run the application
root.mainloop()
