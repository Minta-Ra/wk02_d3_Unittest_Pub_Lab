class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.collection_of_drinks = []


    def add_drink(self, drink):
        self.collection_of_drinks.append(drink)

    def count_drinks(self):
        return len(self.collection_of_drinks)

    def serve_drink(self, customer, drink):
        if self.collection_of_drinks.count(drink) == 0:
            return
        self.collection_of_drinks.remove(drink)
        customer.buy_a_drink(drink)
        self.till += drink.price