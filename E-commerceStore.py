import csv

PRODUCTS_FILE = 'products.csv'
CUSTOMERS_FILE = 'customers.csv'
ORDERS_FILE = 'orders.csv'
REVIEWS_FILE = 'reviews.csv'
ADMIN_USER = 'admin'
ADMIN_PASS = 'password'

def authenticate():
    print("Welcome to the E-commerce Store Management System")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    
    if username == ADMIN_USER and password == ADMIN_PASS:
        print("Authentication successful!")
    else:
        print("Authentication failed! Exiting.")
        exit()

def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Quantity Available: "))
    
    with open(PRODUCTS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product_id, name, price, quantity])
    print(f"Product '{name}' added successfully.")

def view_products():
    try:
        with open(PRODUCTS_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\n{:<10} {:<30} {:<10} {:<10}".format('ID', 'Name', 'Price', 'Quantity'))
            print("=" * 60)
            for row in reader:
                print("{:<10} {:<30} ₹{:<10} {:<10}".format(row[0], row[1], row[2], row[3]))
            print("=" * 60)
    except FileNotFoundError:
        print("Products file not found.")

def update_product():
    product_id = input("Enter Product ID to update: ")
    updated = False
    products = []

    try:
        with open(PRODUCTS_FILE, mode='r') as file:
            reader = csv.reader(file)
            products = list(reader)

        for row in products:
            if row[0] == product_id:
                row[1] = input(f"Enter new name (current: {row[1]}): ") or row[1]
                row[2] = float(input(f"Enter new price (current: ₹{row[2]}): ") or row[2])
                row[3] = int(input(f"Enter new quantity (current: {row[3]}): ") or row[3])
                updated = True

        with open(PRODUCTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(products)

        if updated:
            print("Product updated successfully.")
        else:
            print("Product ID not found.")
    except FileNotFoundError:
        print("Products file not found.")

def delete_product():
    product_id = input("Enter Product ID to delete: ")
    products = []

    try:
        with open(PRODUCTS_FILE, mode='r') as file:
            reader = csv.reader(file)
            products = list(reader)

        products = [row for row in products if row[0] != product_id]

        with open(PRODUCTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(products)

        print("Product deleted successfully.")
    except FileNotFoundError:
        print("Products file not found.")

def add_customer():
    customer_id = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    contact = input("Enter Contact Number: ")
    
    with open(CUSTOMERS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([customer_id, name, contact])
    print(f"Customer '{name}' added successfully.")

def view_customers():
    try:
        with open(CUSTOMERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\n{:<10} {:<30} {:<15}".format('ID', 'Name', 'Contact'))
            print("=" * 60)
            for row in reader:
                print("{:<10} {:<30} {:<15}".format(row[0], row[1], row[2]))
            print("=" * 60)
    except FileNotFoundError:
        print("Customers file not found.")

def update_customer():
    customer_id = input("Enter Customer ID to update: ")
    updated = False
    customers = []

    try:
        with open(CUSTOMERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            customers = list(reader)

        for row in customers:
            if row[0] == customer_id:
                row[1] = input(f"Enter new name (current: {row[1]}): ") or row[1]
                row[2] = input(f"Enter new contact (current: {row[2]}): ") or row[2]
                updated = True

        with open(CUSTOMERS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(customers)

        if updated:
            print("Customer updated successfully.")
        else:
            print("Customer ID not found.")
    except FileNotFoundError:
        print("Customers file not found.")

def delete_customer():
    customer_id = input("Enter Customer ID to delete: ")
    customers = []

    try:
        with open(CUSTOMERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            customers = list(reader)

        customers = [row for row in customers if row[0] != customer_id]

        with open(CUSTOMERS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(customers)

        print("Customer deleted successfully.")
    except FileNotFoundError:
        print("Customers file not found.")

def place_order():
    order_id = input("Enter Order ID: ")
    customer_id = input("Enter Customer ID: ")
    product_id = input("Enter Product ID: ")
    quantity = int(input("Enter Quantity: "))

    with open(ORDERS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([order_id, customer_id, product_id, quantity])
    print(f"Order {order_id} placed successfully.")

def view_orders():
    try:
        with open(ORDERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\n{:<10} {:<15} {:<10} {:<10}".format('Order ID', 'Customer ID', 'Product ID', 'Quantity'))
            print("=" * 60)
            for row in reader:
                print("{:<10} {:<15} {:<10} {:<10}".format(row[0], row[1], row[2], row[3]))
            print("=" * 60)
    except FileNotFoundError:
        print("Orders file not found.")

def update_order():
    order_id = input("Enter Order ID to update: ")
    updated = False
    orders = []

    try:
        with open(ORDERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            orders = list(reader)

        for row in orders:
            if row[0] == order_id:
                row[2] = input(f"Enter new product ID (current: {row[2]}): ") or row[2]
                row[3] = int(input(f"Enter new quantity (current: {row[3]}): ") or row[3])
                updated = True

        with open(ORDERS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(orders)

        if updated:
            print("Order updated successfully.")
        else:
            print("Order ID not found.")
    except FileNotFoundError:
        print("Orders file not found.")

def delete_order():
    order_id = input("Enter Order ID to delete: ")
    orders = []

    try:
        with open(ORDERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            orders = list(reader)

        orders = [row for row in orders if row[0] != order_id]

        with open(ORDERS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(orders)

        print("Order deleted successfully.")
    except FileNotFoundError:
        print("Orders file not found.")

def add_review():
    review_id = input("Enter Review ID: ")
    product_id = input("Enter Product ID: ")
    customer_id = input("Enter Customer ID: ")
    rating = int(input("Enter Rating (1-5): "))
    comment = input("Enter Comment: ")

    with open(REVIEWS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([review_id, product_id, customer_id, rating, comment])
    print("Review added successfully.")

def view_reviews():
    try:
        with open(REVIEWS_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\n{:<10} {:<10} {:<15} {:<10} {:<30}".format('Review ID', 'Product ID', 'Customer ID', 'Rating', 'Comment'))
            print("=" * 100)
            for row in reader:
                print("{:<10} {:<10} {:<15} {:<10} {:<30}".format(row[0], row[1], row[2], row[3], row[4]))
            print("=" * 100)
    except FileNotFoundError:
        print("Reviews file not found.")

def update_review():
    review_id = input("Enter Review ID to update: ")
    updated = False
    reviews = []

    try:
        with open(REVIEWS_FILE, mode='r') as file:
            reader = csv.reader(file)
            reviews = list(reader)

        for row in reviews:
            if row[0] == review_id:
                row[1] = input(f"Enter new product ID (current: {row[1]}): ") or row[1]
                row[2] = input(f"Enter new customer ID (current: {row[2]}): ") or row[2]
                row[3] = int(input(f"Enter new rating (current: {row[3]}): ") or row[3])
                row[4] = input(f"Enter new comment (current: {row[4]}): ") or row[4]
                updated = True

        with open(REVIEWS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reviews)

        if updated:
            print("Review updated successfully.")
        else:
            print("Review ID not found.")
    except FileNotFoundError:
        print("Reviews file not found.")

def delete_review():
    review_id = input("Enter Review ID to delete: ")
    reviews = []

    try:
        with open(REVIEWS_FILE, mode='r') as file:
            reader = csv.reader(file)
            reviews = list(reader)

        reviews = [row for row in reviews if row[0] != review_id]

        with open(REVIEWS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reviews)

        print("Review deleted successfully.")
    except FileNotFoundError:
        print("Reviews file not found.")

def main():
    authenticate()
    
    while True:
        print("\nE-commerce Store Management System")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Add Customer")
        print("6. View Customers")
        print("7. Update Customer")
        print("8. Delete Customer")
        print("9. Place Order")
        print("10. View Orders")
        print("11. Update Order")
        print("12. Delete Order")
        print("13. Add Review")
        print("14. View Reviews")
        print("15. Update Review")
        print("16. Delete Review")
        print("17. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            add_customer()
        elif choice == '6':
            view_customers()
        elif choice == '7':
            update_customer()
        elif choice == '8':
            delete_customer()
        elif choice == '9':
            place_order()
        elif choice == '10':
            view_orders()
        elif choice == '11':
            update_order()
        elif choice == '12':
            delete_order()
        elif choice == '13':
            add_review()
        elif choice == '14':
            view_reviews()
        elif choice == '15':
            update_review()
        elif choice == '16':
            delete_review()
        elif choice == '17':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
