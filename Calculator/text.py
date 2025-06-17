#storage for all the users that register using a dictonary 
users = {}

#Allows you to register your account if so then you can sign in
def register():
   username = input("Enter a username: ")
   #Choose the username you want the system will always ask you for a username 
   # Check if user is already taken
   if username in users:
       print("Username already taken. Please enter another name.")
       register()  
   else:
       password = input("Enter a password: ")
       #Like the username enter a password
       users[username] = password
       #adds it to the storage to allow you to log in
       print("Registration successful!")

#Defines the sign in attempts
def sign_in(attempts=0):
   username = input("Enter your username: ")
   #Makes you enter your user that you registered
   if username not in users:
       print("Username does not exist. Please register or try again.")
       return  # Exit if the username is not found
   
   password = input("Enter your password: ")
   
   # Password Check
   if users[username] == password:
       print("Sign-in successful!")
       #If the password and the username is correct sign the user in.
   else:
       print("Incorrect password.")
       #If it is incorrect give a message saying that the password is incorrect and take aways an attempt
       attempts += 1
       #Adds the amount of attempts from 0-1
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