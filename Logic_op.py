a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
def compare(a,b):
    if(a>b or b<a):
        print(a," is greater then ", b)
    if(b>a or a<b):
        print(b," is greater then", a)
    if(not(a>b and  b>a)):
        print(a,"is = ",b)
compare(a,b)
