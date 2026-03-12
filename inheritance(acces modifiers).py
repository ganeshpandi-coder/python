class parent:
    def __init__(self):
        self._age=24
class child(parent):
    def show(self):
        print(self._age)
obj=child()
obj.show()

