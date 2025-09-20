users = {
    "Rashid": "Rash",
}

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
            sign_in(attempts)
        else:
            print("Too many failed attempts. Sign-in blocked.")

def change_password():
    username = input("Enter your username: ")
    if username not in users:
        print("User does not exist. Please try again.")
        return
    current_password = input("Enter your current password: ")
    if users[username] == current_password:
        new_password = input("Enter new password: ")
        users[username] = new_password
        print("Password changed successfully!")
    else:
        print("Incorrect current password.")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Register")
        print("2. Sign in")
        print("3. Quit")
        print("4. Change password")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            sign_in()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        elif choice == "4":
            change_password()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
