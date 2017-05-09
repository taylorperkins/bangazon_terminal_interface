import sys
from src.customer import Customer
from src.order import Order
from src.payment_type import PaymentType
from src.product import Product
from src.product_order import ProductOrder


"""
Terminal Interface configuration for the terminal interface for the user interaction.
"""
class BangazonControl(Customer, Order, PaymentType, Product, ProductOrder):
    """
    This class is to handle interactions with the user from the terminal

    Methods:
        create_customer: used to create a dict() of the information pertaining to the customer.

    Author:
        Adam Myers
    """

    def create_customer(self, name, address, state, city, postal_code):
        """
        This method creates a dictionary that contains information about the customer and returns that dictionary.

        Arguments:
            name (String): Name of the customer.
            address (String): Address of the customer.
            state (String): State of which the customer lives.
            city (String): City the customer lives in.
            postal_code (String): Postal code that the customer lives in.

        Returns:
            new_customer (Dictionary): containing attributes of name, address, state, city, postal_code

        Author:
            Adam Myers
        """
        new_customer = { 'name': name, 'address' : address, 'state': state, 'city': city, 'postal_code': postal_code }
        return new_customer

    def set_active_customer(self, active_customer):
        """Summary

        Args:
            active_customer (Int): Index of active customer from list of all customers

        Returns:
            TYPE: Description
        """
        self.active_customer = active_customer

    def choose_active_customer(self):
        return 1

    def create_payment_type(self, customer_id, name, account_number):
        """
        This method creates a dictionary that contains information about the payment types and returns that dictionary.

        Arguments:
            name (String): Name of the payment type.
            account_number (Int): Account Number.

        Returns:
            new_payment_type (Dictionary): containing attributes of name and account_number

        Author:
            wocaldwell
        """
        new_payment_type = {'customer_id': customer_id, 'name': name, 'account_number': account_number}
        return new_payment_type

    def save_all_customers(self):
        pass

    def save_all_products(self):
        self.products = [(1, 12.99, 'ball')]

    def add_product_to_order(self, index_of_product):
        if self.active_customer:
            self.active_order = self.make_order_active(self.active_customer)
        pass

    def get_sum_of_products_for_current_order(self, active_order_id):
        pass

    def update_payment_type_for_order(self, active_order_id, payment_type_id):
        pass

    def display_main_menu():
        """
        Displays the main menu when bangazon_control.py is run in the cli and directs to other features based on user input.

        Arguments:
            n/a

        Returns:
            n/a

        Author:
            wocaldwell
        """
        print('*********************************************************')
        print('**  Welcome to Bangazon! Command Line Ordering System  **')
        print('*********************************************************')
        print('1. Create a customer account\n2. Choose active customer\n3. Create a payment option\n4. Add product to shopping cart\n5. Complete an order\n6. See product popularity\n7. Leave Bangazon!')
        selection = input('> ')
        if selection == '1':
            pass
        if selection == '2':
            pass
        if selection == '3':
            pass
        if selection == '4':
            pass
        if selection == '5':
            pass
        if selection == '6':
            pass
        if selection == '7':
            sys.exit()
        BangazonControl.display_main_menu()


if __name__ == '__main__':
    BangazonControl.display_main_menu()












