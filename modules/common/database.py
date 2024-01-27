import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'C:\Users\maryf\Desktop\QA-auto-2023\become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connect successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record 
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        print(query)
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_field_by_id(self, field, product_id):
        query = f"SELECT {field} FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_products(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id},'{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date\
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record 
    
    def updade_product_description_by_id(self, product_id, description):
        query = f"UPDATE products SET description = '{description}' WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_users(self, user_id, name, address, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES ({user_id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def get_users_field_by_id(self, field, user_id):
        query = f"SELECT {field} FROM customers WHERE id = {user_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_user_address(self, user_id, address):
        query = f"UPDATE customers SET address = '{address}' WHERE id = {user_id}"  
        self.cursor.execute(query)
        self.connection.commit()

    def delete_user_by_id(self, user_id):
        query = f"DELETE FROM customers WHERE id = {user_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_product_with_duplication(self, product_id, name):
        query = f"INSERT INTO products (id, name) \
            VALUES ({product_id},'{name}')"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_user_with_duplication(self, user_id, name):
        query = f"INSERT INTO customers (id, name) \
            VALUES ({user_id},'{name}')"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_order(self, order_id, user_id, product_id):
        query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id) \
                VALUES ({order_id}, {user_id}, {product_id})"
        self.cursor.execute(query)
        self.connection.commit()

    def update_order(self, order_id, product_id):
        query = f"UPDATE orders SET product_id = {product_id} WHERE id = {order_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_order(self, order_id):
        query = f"DELETE FROM orders WHERE id = {order_id}"
        self.cursor.connection(query)
        self.connection.commit()