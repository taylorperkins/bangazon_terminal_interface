"""
Terminal Interface configuration for the initial database structure in the database
"""
import sqlite3

def CreateDatabase(database='bangazon.db'):
    """
        Creates bangazon.db file in root for intial database structure which includes tables of Customer, Products, PaymentType, Order, ProductOrder.

        Arguments:
            N/A

        Returns:
            N/A

        Author:
            Adam Myers
            Talbot Lawrence
        """
    with sqlite3.connect(database) as conn:
        c = conn.cursor()
        customer_table_needs_inserts = True
        product_table_needs_inserts = True

        try:
            c.execute("""create table Customer (
                customer_Id integer not null primary key autoincrement,
                name text,
                address text,
                city text,
                state text,
                postal_code text,
                phone_number text)""")

        except sqlite3.OperationalError:
            customer_table_needs_inserts = False

        if customer_table_needs_inserts:
            c.execute("insert into Customer values (null, 'Adam', '123 Code Ave', 'CodeVille', 'WyCoding', '8675309', '1234245243')")
            c.execute("insert into Customer values (null, 'Talbot', '123 Boring Street', 'BoreVille', 'WyBoring', '000000-000', '12312312334')")
            c.execute("insert into Customer values (null, 'Taylor', '123 Accident Road', 'CrunchVille', 'WyTireScreeching', '911...', '90909090')")
        else:
            pass

        try:
            c.execute("""create table Product (
                product_Id integer not null primary key autoincrement,
                price integer,
                title text)""")

        except sqlite3.OperationalError:
            product_table_needs_inserts = False

        if product_table_needs_inserts:
            c.execute("insert into Product values (null, 2.99, 'Apples')")
            c.execute("insert into Product values (null, 4.34, 'Average Desktop Pen')")
            c.execute("insert into Product values (null, 9.12, 'Potato Hats')")
            c.execute("insert into Product values (null, 8.54, 'Alien Insects')")
            c.execute("insert into Product values (null, 134.82, 'Talbot Windows 10')")
            c.execute("insert into Product values (null, 502.14, '1HP Shoe Shiner')")
            c.execute("insert into Product values (null, 0.12, 'Cheap Joke')")
        else:
            pass

        try:
            c.execute("""create table PaymentType (
                payment_type_Id integer not null primary key autoincrement,
                customer_Id integer not null,
                account_number integer,
                name text,
                foreign key (customer_Id) references Customer(customer_Id))""")
        except sqlite3.OperationalError:
            pass

        try:
            c.execute("""create table Orders (
                order_Id integer not null primary key autoincrement,
                customer_Id integer not null,
                payment_type_Id integer,
                foreign key (customer_Id) references Customer(customer_Id))""")
        except sqlite3.OperationalError:
            pass

        try:
            c.execute("""create table ProductOrder (
                product_order_Id integer not null primary key autoincrement,
                order_Id integer not null,
                product_Id integer not null,
                foreign key (order_Id) references Orders(order_Id),
                foreign key (product_Id) references Product(product_Id))""")
        except sqlite3.OperationalError:
            pass

        conn.commit()

"""
Below is for developmental purposes only. To allow for creation of the database prior to having a setup function run when the menu appears.
"""
if __name__ == "__main__":
    CreateDatabase(database='../bangazon.db')

