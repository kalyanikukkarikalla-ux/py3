from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash.")

p1 = CreditCardPayment()
p2 = UpiPayment()
p3 = CashPayment()

p1.pay(1500)
p2.pay(750)
p3.pay(300)