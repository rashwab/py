import datetime
# Function to validate member ID
def validate_member_id(member_id):
   return member_id.isdigit() and len(member_id) == 6
# Function to validate Book ISBN
def validate_book_isbn(book_isbn):
   parts = book_isbn.split('-')
   return (
       book_isbn.startswith("978")
       and len(book_isbn) == 17
       and len(parts) == 5
       and all(part.isdigit() for part in parts)
   )
# Function to validate Issue Date
def validate_issue_date(issue_date):
   try:
       datetime.datetime.strptime(issue_date, "%Y-%m-%d")
       return True
   except ValueError:
       return False

# Function to validate Loan Period
def validate_loan_period(loan_period):
   return loan_period.isdigit() and 7 <= int(loan_period) <= 30

# Function to save record to file
def save_to_file(record):
   with open("issued_books.txt", "a") as file:
       file.write(record + "\n")

# Function to read records and display as a table
def read_from_file():
   print("\nIssued Books:")
   try:
       with open("issued_books.txt", "r") as file:
           records = file.readlines()
           if records:
               print("-" * 55)
               print(f"| {'Member ID':<10} | {'Book ISBN':<17} | {'Issue Date':<10} | {'Loan Period':<10} |")
               print("-" * 55)
               for record in records:
                   member_id, book_isbn, issue_date, loan_period = record.strip().split(",")
                   print(f"| {member_id:<10} | {book_isbn:<17} | {issue_date:<10} | {loan_period:<10} |")
               print("-" * 55)
           else:
               print("No records found.")
   except FileNotFoundError:
       print("No records found.")

# Library system main function
def library_system():
   print("Welcome to the Library Management System!")

   while True:
       member_id = input("Enter 6-digit Member ID: ").strip()
       if validate_member_id(member_id):
           break
       print("Invalid Member ID. Try again.")

   while True:
       book_isbn = input("Enter Book ISBN (e.g., 978-3-16-148410-0): ").strip()
       if validate_book_isbn(book_isbn):
           break
       print("Invalid ISBN. Try again.")

   while True:
       issue_date = input("Enter Issue Date (YYYY-MM-DD): ").strip()
       if validate_issue_date(issue_date):
           break
       print("Invalid Date. Try again.")

   while True:
       loan_period = input("Enter Loan Period (7-30 days): ").strip()
       if validate_loan_period(loan_period):
           break
       print("Invalid Loan Period. Try again.")

   record = f"{member_id},{book_isbn},{issue_date},{loan_period}"
   save_to_file(record)
   print("Record saved successfully!")

# Main menu
def main():
   while True:
       print("""\nOptions:
       1. Issue a Book
       2. Display Records 3. Exit""""")
       choice = input("Enter your choice (1-3): ").strip()

       if choice == "1":
           library_system()
       elif choice == "2":
           read_from_file()
       elif choice == "3":
           print("Exiting")
           break
       else:
           print("Invalid choice. Try again.")
if __name__ == "__main__":
   main()