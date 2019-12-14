def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    return x / y

print("Select operation: ")
print("1 -> Add")
print("2 -> Substract")
print("3 -> Multiply")
print("4 -> Devide")

choise = input("Enter choise(1 - 2 - 3 - 4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choise == '1':
    print(num1,"+",num2,"=", add(num1,num2))
elif choise == '2':
    print(num1,"-",num2,"=", substract(num1,num2))
elif choise == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choise == '4':
    print(num1,"/",num2,"=", devide(num1,num2))
else:
    print("Invalid input.")
