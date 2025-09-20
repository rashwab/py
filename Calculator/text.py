
users = {}
def register():
   username = input("Enter a username: ")
   if username in users:
       print("Username already taken. Please enter another name.")
       register()  
   else:
       password = input("Enter a password: ")
       users[username] = password
       print("Registration successful!")

def sign_in(attempts=0):
   username = input("Enter your username: ")
   if username not in users:
       print("Username does not exist. Please register or try again.")
       return  
   
   password = input("Enter your password: ")

   if users[username] == password:
       print("Sign-in successful!")
   else:
       print("Incorrect password.")
       attempts += 1
       if attempts < 3:
           print(f"Attempt {attempts} of 3.")
           sign_in(attempts)  # Recursive call for the next attempt
       else:
           print("Too many failed attempts. Sign-in blocked.")

def main():
   while True:
       print("\nChoose an option:")
       print("R. Register")
       print("L. Sign in")
       print("x. Quit")
       choice = input("Enter your choice: ")
       
       if choice == 'R':
           register()
       elif choice == 'L':
           sign_in()
       elif choice == 'x':
           print("Exiting program. Goodbye!")
           break
       else:
           print("Invalid option. Please try again.")


if __name__ == "__main__":

   main()
