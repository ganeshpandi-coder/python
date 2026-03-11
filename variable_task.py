#================
# loval variable
#================
def demo():
    x=10
    print(x)
demo()
#==============
# global vvariable
#==============
x=50
def show():
    print(x)
show()
print()
#=============
# non local varable
#=============
def demo():
    x=15
    def inner():
        
