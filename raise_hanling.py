class Bankerror(Exception):
    pass
try:
    amount=int(input("enter a amount"))
    if amount<500:
            raise Bankerror("insufficient balance")
    print(" balance",amount)
except Bankerror as e:
    print(e)

