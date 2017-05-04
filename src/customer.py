# .

class Customer(object):
    """docstring for Customer"""

    def __init__(self, name, street_address, city, state, postal_code, phone_number):
        self.__name = name
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__postal_code = postal_code
        self.__phone_number = phone_number

    @property
    def name(self):
        return self.__name

    @property
    def street_address(self):
        return self.__street_address

    @property
    def city(self):
        return self.__city

    @property
    def state(self):
        return self.__state

    @property
    def postal_code(self):
        return self.__postal_code

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def id(self):
        return self.__id  

    def save(self):
        self.__id = 1


# @street_address.setter
# def street_address(self, street_address):
#   self.__street_address = street_address

