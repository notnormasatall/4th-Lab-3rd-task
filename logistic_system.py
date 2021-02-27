'''
Creates a basic logistic system that helps the user to make and track an order.
'''
from random import randint


class Item:
    '''
    Creates an item with values (name, price).
    '''

    def __init__(self, name: str, price: float):
        '''
        Creates an item.
        '''
        self.name = name
        self.price = price

    def __str__(self):
        '''
        Returns a basic info about item as a sentence.
        '''
        return f'{self.name} costs {self.price} $.'


class Location:
    '''
    Combines city and postoffice info into one location.
    '''

    def __init__(self, city: str, postoffice: int):
        '''
        Combines city and postoffice info into one location.
        '''
        self.city = city
        self.postoffice = postoffice


class Vehicle:
    '''
    Creates a vehicle with a default .isAvailable value (True).
    '''

    def __init__(self, vehicleNo: int):
        '''
        Creates a vehicle with a default .isAvailable value (True).
        '''
        self.vehicleNo = vehicleNo
        self.isAvailable = True


class Order:
    '''
    Creates an order and assigns a basic info to it (vehicle, location, price).
    '''

    def __init__(self, user_name, city, postoffice, items):
        '''
        Creates an order object.
        '''
        self.orderId = randint(99999999, 999999999)
        self.location = Location(city, postoffice)
        self.items = items

    def assignVehicle(self, vehicle: Vehicle):
        '''
        Assigns a vehicle to an order.
        '''
        if vehicle.isAvailable == True:
            self.vehicle = vehicle
            vehicle.isAvailable = False

    def calculate_amount(self):
        '''
        Returns a sum of all item's prices.
        '''
        return sum(item.price for item in self.items)

    def __str__(self):
        '''
        Returns an ID of an order as a sentence.
        '''
        return f'Your order number is {self.orderId}.'


class LogisticSystem:
    '''
    Manipulates, places and tracks multiple orders.
    '''

    def __init__(self, vehicles):
        '''
        Creates a list of objects and a list of vehicles.
        '''
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order):
        '''
        If there's an vehicle availablem places an order
        (adds to the orders list).
        '''
        if any([elem.isAvailable for elem in self.vehicles]) == True:
            for vehicle in self.vehicles:
                if vehicle.isAvailable == True:
                    order.assignVehicle(vehicle)
                    self.orders.append(order)
                    break
        else:
            print('There is no available vehicle to deliver an order.')

    def trackOrder(self, id_num):
        '''
        Finds an order by an entered ID.
        '''
        for order in self.orders:

            if id_num == order.orderId:
                return f'Your order #{id_num} is sent to {order.location.city}, \
{order.location.postoffice}. Total price: {Order.calculate_amount(order)} UAH.'

        return 'No such order.'
