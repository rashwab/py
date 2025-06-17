import json
from collections import defaultdict
ticket=defaultdict(list)
ticket= {}
def create_ticket():
 while True:
  customer_name=input("Enter customer name: ")
 
  issue_description=input("Enter Issue Description: ")
  t_slot=len (ticket)+1
  ticket[f"tickets{t_slot}"]=customer_name
  ticket[f"name{customer_name}"]=issue_description
  print(ticket)
while True:                
 option = input("""Enter Your Option
               1.Create A Ticket 
               2.View Your Ticket
                Pick one: """)
 if option== "1":
  create_ticket()
 elif option == "2":
  print(ticket)
  
 elif option=="3":
  break
 