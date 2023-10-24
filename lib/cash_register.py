#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_price = 0

    def apply_discount(self):
        if self.discount:
            self.total = self.total * (1 - self.discount / 100)
            print(f'After the discount, the total comes to ${int(self.total)}.')
        else:
            print('There is no discount to apply.')


    def add_item(self, title, price, quant=1):
        self.total = self.total + (price * quant)
        for num in range(0, quant):
          self.items.append(title)
        self.last_price = (price * quant)
    
    def void_last_transaction(self):
        self.items.pop(-1)
        self.total = self.total - self.last_price