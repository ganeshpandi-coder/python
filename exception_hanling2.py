try:
    a=[1,16,5,15,10]
    print(a[6])
except IndexError:
    print("index is out of range")

    

# key Error #

try:
    a={"name":"ganesh","age":20}
    print(a["mark"])
except KeyError:
    print("key not find in dictionary")

