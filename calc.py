def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y != 0:
        return x / y
    return "Error!"
def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        choice = input("Enter choice (1,2,3,4): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice=='1':
            print(f"{num1}+{num2} = {add(num1, num2)}")
        elif choice=='2':
            print(f"{num1}-{num2} = {subt(num1, num2)}")
        elif choice=='3':
            print(f"{num1}*{num2} = {mul(num1, num2)}")
        elif choice=='4':
            print(f"{num1}/{num2} = {div(num1, num2)}")
        else:
            print("Invalid choice!")
        next_calculation = input("Do you want to continue?: ")
        if next_calculation.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
