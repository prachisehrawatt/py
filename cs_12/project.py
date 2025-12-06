import mysql.connector

# ---------------- CONNECT TO MYSQL ----------------
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="cafe")

cursor = con.cursor()

# ---------------- SHOW MENU ----------------
def show_menu():
    print("\n---- Cafe Menu ----")
    cursor.execute("SELECT item, price FROM menu")
    data = cursor.fetchall()
    
    for row in data:
        print(row[0] + " : ₹" + str(row[1]))
    print("--------------------")


# ---------------- TAKE ORDER ----------------
def take_order():
    show_menu()

    while True:
        item = input("Enter item to order (or 'done'): ").capitalize()

        if item == "Done":
            break

        cursor.execute("SELECT price FROM menu WHERE item=%s", (item,))
        result = cursor.fetchone()

        if result:
            price = result[0]
            cursor.execute("INSERT INTO orders(item, price) VALUES (%s, %s)", (item, price))
            con.commit()
            print("Added: " + item)
        else:
            print("Item not found. Try again.")


# ---------------- VIEW ORDER ----------------
def view_order():
    cursor.execute("SELECT item, price FROM orders")
    data = cursor.fetchall()

    if len(data) == 0:
        print("Your order is empty.")
        return

    print("\n---- Your Order ----")
    for row in data:
        print(row[0] + " - ₹" + str(row[1]))
    print("---------------------")


# ---------------- TOTAL BILL ----------------
def total_bill():
    cursor.execute("SELECT SUM(price) FROM orders")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print("Total Bill: ₹" + str(total))


# ---------------- MAIN MENU ----------------
while True:
    print("\n===== Cafe System =====")
    print("1. View Menu")
    print("2. Place Order")
    print("3. View Your Order")
    print("4. Checkout")
    print("5. Reset Order") 
    print("6. Exit")

    ch = input("Enter choice (1-6): ")

    if ch == "1":
        show_menu()
    elif ch == "2":
        take_order()
    elif ch == "3":
        view_order()
    elif ch == "4":
        view_order()
        total_bill()
        print("Thank you for visiting!")
        break
    elif ch == "5":
        cursor.execute("DELETE FROM orders")
        con.commit()
        print("Order has been reset.")
    elif ch == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")








