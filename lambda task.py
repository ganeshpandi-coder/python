a=[1,2,3,4,2,6,3,9,2,5,7,1]
n=lambda x:list(set(x))
print(n(a))

# palindrome

a = lambda s: s == s[::-1]

print(a("madam"))   
print(a("racecar")) 
print(a("hello"))   

# list filtering odd or even number

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(filter(lambda x: x % 2 == 0, n))
b = list(filter(lambda x: x % 2 != 0, n))
print("even number is :",a)
print("odd number is :",b)

# prime number in range

