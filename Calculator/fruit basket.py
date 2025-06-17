import sys
Basket= {}
items= {
    "Orange": "£1",
    "Apple" : "£2"}

def budg():
 budgett =input("what is your budget?:")
def quan():
 Quantity =input("how many do you want to purchase?:")
Options=input("""
               1. Budget
               2. item price
               3. item quantity 
               """)
if Options == "1":
  budg()
elif Options =="2":
   print (items)
   if Options == "3":
     print(Basket)
   else: 
     exit() 
    