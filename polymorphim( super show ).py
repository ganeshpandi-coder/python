class display:
    def show(self):
        print("this is parent class")
class demo(display):
    def show(self):
        super().show()
        print("this is a child class")
obj=demo()
obj.show()
