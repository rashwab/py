#feedback function to keep the rating feed back in 
def feedback():
 feedback_system =input("please enter your feedback")#Feedback input to see what the user entered 
 if len(feedback_system.split())>10: #Checking the length to check if the feedback has more than 10 charecters
   print ("Error the feedback contains more than 10 words") #printing out the error message if the feedback has more than 10 words
 else:
   print("contine ")
   rating_system=input("please enter your rating")#Rating input to see what rating the user entered
 if len(rating_system)>2: #this checks if the number entered is more than 2 digits  
  print("Error the rating contains more than 2 numbers ")#If the number entered is more than 2 digits it prints this message
  print ("rating is from 1-10") 
 else:
  print("continue")
  postive_text_analaysis="excelent"#This sets aconstant for the word excelent 
 if postive_text_analaysis in feedback: #This checks if the word excelent is in the feedback 
   print (postive_text_analaysis,"positice feedback found!") #If the word is found it will print that message out
 else:
      print (postive_text_analaysis, "not in feedback") #Prints this message if the word is not found in feedback
      negative_text_analysis="bad" # the word "Bad" is a constant
 if negative_text_analysis in feedback:# checks if  the word bad is in feedback  
   print ("negatie feedback found")
 else:
   print (postive_text_analaysis is"not in feedback")#prints the message if bad is found in feedback.

feedback()