#Calculator

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mul(x, y):
  return x * y

def div(x, y):
  if y == 0:
    return "Error: Division by zero!"
  return x / y
def mod (x, y):
  return x % y

def expo (x ,y):
  return x ** y

def fdiv (x,y):
  return x // y



name = input("Enter a name: ")
print(f"Welcome, {name}")

while True:
  
  print("""Calculator
1. Add
2. Subtract
3. Multiply 
4. Divide
5.Modulus
6.Exponentiation
7.Floor division              
8. Exit""")
  
  choice = int(input("Enter your calculation (1/2/3/4/5/6/7/8): "))

  if choice in (1, 2, 3, 4, 5, 6, 7, 8):
    num1 = float(input("first number: "))
    num2 = float(input("second number: "))

    if choice == 1:
      print("Answer:", add(num1, num2))
    elif choice == 2:
      print("Answer:", sub(num1, num2))
    elif choice == 3:
      print("Answer:", mul(num1, num2))
    elif choice == 4:
      print("Answer:", div(num1, num2))
    elif choice == 5:
      print("Answer:", mod(num1, num2))
    elif choice == 6:
      print("Answer:", expo(num1, num2))
    elif choice == 7:
      print("Answer:", fdiv(num1, num2))
    elif choice == 8:
      
      print("Exiting the calculator")
      break
  else:
    print("Invalid choice")