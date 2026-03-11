from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class creditcard (payment):
    def pay(self):
        print("enter your card number")
class upi (payment):
    def pay(self):
        print("scan the QR")
c=creditcard()
c.pay()
