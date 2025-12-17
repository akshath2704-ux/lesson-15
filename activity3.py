def add(x,y):
    return x+y
def subract(x,y):
    return x-y
def multipy(x,y):
    return x*y
def divide(x,y):
    return x/y
print("please choose an option")
print("a.addition")
print("b.subraction")
print("c.product")
print("d.divide")
choice=input("enter your choice a/b/c/d:")
num1=int(input("enter number 1 :"))
num2=int(input("enter number 2 :"))
if choice=='a':
    print("sum :",add(num1,num2))
elif choice=='b':
    print("difference:",subract(num1,num2))
elif choice=='c':
    print("product ":,multiply(num1,num2))
elif choice=='d':
    print("quotient :",divide(num1,num2))
else:
    print("invalid input choice !!")