movie="Life movie","Batman"

seat=["A1","A2,A3", "A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5"]
def view_system():
    view_seats=input("Enter the name of the show:")
    if view_seats == "Life movie":
        print("""Seats for Life movie:["Avilable,"Available,"Booked,Available,"Available]:""")

def Booking_system():
 Booking_seat=input ("Enter your choice:")
 name_show=input("enter The name show:") 
 if name_show== "Life movie":
  book_for_movie=input("enter seat numbe to book for Life movie(A1-C5):")
  if book_for_movie not in seat:
     print("Seat taken or invalid option")
     return book_for_movie
 else:
  print( "for Life movie booked successfully! Ticket price: £10")  
  
 
     
def Viewing_Seats_After_Booking():
 choice_system=input("Enter your choice:")
 Show_name=input("Enter the show name:")   
 if Show_name == "Life movie":
    print("""Seats for Life movie: ['Available', 'Booked', 'Booked', 'Available', 'Available']""")
    
 
Booking_system()
