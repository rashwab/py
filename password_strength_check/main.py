while True:
   password = input("Enter password ('exit' to quit): ")
   if password.lower() == "exit":
       try: print("\nPassword History:\n" + open("password_history.txt").read())
       except FileNotFoundError: print("\nNo history found.")
       break
   strength = "Weak" if len(password) <= 3 else "Medium" if len(password) <= 8 else "Strong"
   to_improve = "Use at least 8 characters with symbols or numbers." if strength == "Weak" else "Add symbols or numbers." if strength == "Medium" else None
   print(f"Strength: {strength}")
   if to_improve: print(f"Suggestion: {to_improve}")
   with open("password_history.txt", "a") as f: f.write(f"{password}: {strength}\n")