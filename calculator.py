def addition():
    a=int(input("Enter the first number :"))
    b=int(input("Enter the second number :"))
    print(a+b)
def substraction():
    x=int(input("Enter the first number :"))
    y=int(input("Enter the second number :"))
    print(x-y)
def multiplication():
    r=int(input("Enter the first number :"))
    s=int(input("Enter the second number :"))
    print(r*s)
def division():
    c=int(input("Enter the first number :"))
    d=int(input("Enter the second number :"))
    print(c//d)
    c=input("do you want to continue")
    for c in range(1):
        if c=="YESyesy":
            continue
        else:
            break
addition()
substraction()
multiplication()
division()
