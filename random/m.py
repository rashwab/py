Bank= {100}


def withdrawal(x, y):  
 return x-y

while True: 
 print("""               
 1.View Balance
 2. Withdraw Cash
 3 Exit:""")

 options = int(input("Enter your options:"))

 num = str(input("withdrawal amount: "))
 if options == 1:
   print(Bank)
 elif options == 2:
    print ("sucessfully withdrawn"(num))
 elif  options == 3:
  break
exit()