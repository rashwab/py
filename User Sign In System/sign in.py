from ast import main
import sys
accounts = {
"Rashid":"Lawal"
}
print ("welcome to the shooters hill login system")
def Register(): 
  Username=input("Enter a username")
  if Username in accounts:
    print("username already taken")
    exit()
  else:
   Password=input("Enter a password")
  print("account successfully made")
  def Signin():
   Username=input("enter username")
  if Username in accounts:
    print("user is correct")

    password=input("enter password")
  else: 
    print ("invalid user") 
    exit()
  if accounts [Username]:[password] 
  print("successfull..")
main()
options=input("""Choose An option
     1. register
      2. login
     3.quit:""")
if __name__ =="__main__":
  main()
if options == "1":
  Register()
elif options == "2":
  Signin()
else: 
  exit()
  
 
 
