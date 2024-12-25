# Pharmacy Management Mini Project

## Overview
The **Pharmacy Management System** is a GUI-based application developed using Python (`Tkinter`) and MySQL, designed to streamline the management of pharmacy operations. The project allows users to:
- Check the availability of medicines.
- View discounted prices based on offers.
- Suggest alternatives for unavailable medicines.
- Handle billing processes efficiently.
- Update and manage the pharmacy database with triggers and relationships.

## Features
### Medicine Availability
- Check the availability of a specific medicine.
- Display details including price, discounted price, and available stock quantity.

### Alternatives
- Suggest alternative medicines when a specific medicine is out of stock.

### Billing System
- Calculate the total cost for a purchase based on the selected medicine and quantity.
- Automatically update the stock after a purchase.

### Database Management
- **Triggers:** Automatically calculate discounted prices when new medicines with offers are added.
- **Relational Database:** Use tables for medicines, suppliers, and alternatives with appropriate relationships.

## Tech Stack
- **Frontend:** Python (`Tkinter`)
- **Backend:** MySQL
- **Database Tools:** MySQL Workbench (or any MySQL client)

## Installation and Setup
### Prerequisites
- Python 3.x
- MySQL Server
- Required Python Libraries:
  - `mysql-connector-python`
  - `tkinter` (comes pre-installed with Python)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/its-kshitij4444/Pharmacy-Management-Mini-Project.git
   cd Pharmacy-Management-Mini-Project
2. **Set Up the Database**
   - Open `pharmacy_backend.sql` in MySQL Workbench or your preferred MySQL client.
   - Execute the script to create the database, tables, and triggers, and populate sample data.

3. **Install Python Dependencies**
   ```bash
   pip install mysql-connector-python

4. **Run the Application**
   ```bash
   python app.py

