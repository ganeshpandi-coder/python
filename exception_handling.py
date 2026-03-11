try:
 a=int(input("enter a number"))
 b=int(input("enter b number"))
 result=a/b
 print(result)
except IndexError:
    print("cannnot divide by zero")
except ValueError:
    print("please enter numbers only")
