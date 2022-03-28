# Importing the random numbers and add multiply and subtract
import random

#Defining the gen number
def genNumber (maxNum):
    return random.randint(0,maxNum)


# Using definition to make easy mode
def easy():
     print(" \n            Easy Mode             ")

     # Creating variables
     name=input("Enter your name: ")
     Qu=int(input("Enter the no of questions: "))
     Co=0
     In=0
     num1=0
     num2=0
     Uans=0
     ans=0

     # Using for to range the numbers to maximum of 10
     print("########################################################")
     print("########################################################")
     questions=[ ]
     for i in range(1,Qu+1):
          q = str(genNumber(10)) + " + " + str(genNumber(10))
          answer = int(input(q+ " = "))
          questions.append((q,answer))
     # Using for to give the answer and the question after typing the answer by the user
     print("#########################################################")
     print("#########################################################")
     for q,a in questions:
          correct_answer = eval(q)
          if correct_answer ==a:
               print(q,"=",a,"Correct")
               Co+=1
          else:
               print(q,"=",a,"Incorrect", "Correct answer","[",correct_answer,"]")
               In+=1
     print("------------------------------------------------------------------------------------------------")
     print("------------------------------------------------------------------------------------------------")
      #Programming to show the Game Results the name, the correct and wrong answers plus the final
     Per=int((Co/Qu)*100)
     print("*************************************************************")
     print("           GAMERESULTS               ")
     print("\n Your name is", name)
     print("\n Questions answered is",Co)
     print("\n Question not answered is",In)
     print("\n Final score is",Co)
     print("\n Your percentage is", Per)
     print("**************************************************************")

     import mysql.connector

     # open database connection with a dictionery

     conDict = {'host' : 'localhost', 'database' : 'dl_game', 'user' : 'root', 'password' : ''}

     db = mysql.connector.connect(**conDict)

     # Prepare a cursor object using cursor() method
     cursor = db.cursor()

     # Execute SQL query using execute() method.
     mySQLText = "INSERT INTO customgame (Name, Correct, total_questions, Percentage, Mode) VALUES (%s, %s, %s, %s,'Easy')"
     val=(name, Co, Qu, Per)
     cursor.execute(mySQLText,val)

     db.commit()

     print(cursor.rowcount, "record added")

     db.close()

# Using definition to make medium mode
def medium():
     print("\n            Medium Mode                         ")

     # Creating variables
     name=input("Enter your name: ")
     Qu=int(input("Enter the no of questions: "))
     Co=0
     In=0
     num1=0
     num2=0
     Uans=0
     ans=0
     B= ["+", "-"]

     # Using for to range the numbers to maximum of 50
     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
     questions=[ ]
     for i in range(1,Qu+1):
          D=random.choice(B)
          q= str(genNumber(50))+ D + str(genNumber(50))
          answer= int(input(q+ "="))
          questions.append((q,answer))
     # Using for to give the answer and the question after typing the answer by the user
     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
     for q,a in questions:
          correct_answer = eval(q)
          if correct_answer ==a:
               print(q,"=",a,"Correct")
               Co+=1
          else:
               print(q,"=",a,"Incorrect", "Correct answer","[",correct_answer,"]")
               In+=1
     print("------------------------------------------------------------------------------------------------")
     print("------------------------------------------------------------------------------------------------")
      #Programming to show the Game Results the name, the correct and wrong answers plus the final
     Per=int((Co/Qu)*100)
     print("*************************************************************")
     print("           GAMERESULTS               ")
     print("\n Your name is", name)
     print("\n Questions answered is",Co)
     print("\n Question not answered is",In)
     print("\n Final score is",Co)
     print("\n Your percentage is", Per)
     print("**************************************************************")

     import mysql.connector

     # open database connection with a dictionery

     conDict = {'host' : 'localhost', 'database' : 'dl_game', 'user' : 'root', 'password' : ''}

     db = mysql.connector.connect(**conDict)

     # Prepare a cursor object using cursor() method
     cursor = db.cursor()

     # Execute SQL query using execute() method.
     mySQLText = "INSERT INTO customgame (Name, Correct, total_questions, Percentage, Mode) VALUES (%s, %s, %s, %s,'Medium')"
     val=(name, Co, Qu, Per)
     cursor.execute(mySQLText,val)

     db.commit()

     print(cursor.rowcount, "record added")

     db.close()

# Using definition to make medium mode
def hard():
     print("\n            Hard Mode                         ")

     # Creating variables
     name=input("Enter your name: ")
     Qu=int(input("Enter the no of questions: "))
     Co=0
     In=0
     num1=0
     num2=0
     Uans=0
     ans=0
     B= ["+", "-","*"]

     # Using for to range the numbers to maximum of 50
     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
     questions=[ ]
     for i in range(1,Qu+1):
          D=random.choice(B)
          q= str(genNumber(50))+ D + str(genNumber(50))
          answer= int(input(q+ "="))
          questions.append((q,answer))    
    #Using for to give the answer and the question after typing the answer by the user
     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
     for q,a in questions:
          correct_answer = eval(q)
          if correct_answer ==a:
               print(q,"=",a,"Correct")
               Co+=1
          else:
               print(q,"=",a,"Incorrect", "Correct answer","[",correct_answer,"]")
               In+=1
     print("------------------------------------------------------------------------------------------------")
     print("------------------------------------------------------------------------------------------------")
      #Programming to show the Game Results the name, the correct and wrong answers plus the final
     Per=int((Co/Qu)*100)
     print("*************************************************************")
     print("           GAMERESULTS               ")
     print("\n Your name is", name)
     print("\n Questions answered is",Co)
     print("\n Question not answered is",In)
     print("\n Final score is",Co)
     print("\n Your percentage is", Per)
     print("**************************************************************")

     import mysql.connector

     # open database connection with a dictionery

     conDict = {'host' : 'localhost', 'database' : 'dl_game', 'user' : 'root', 'password' : ''}

     db = mysql.connector.connect(**conDict)

     # Prepare a cursor object using cursor() method
     cursor = db.cursor()

     # Execute SQL query using execute() method.
     mySQLText = "INSERT INTO customgame (Name, Correct, total_questions, Percentage, Mode) VALUES (%s, %s, %s, %s,'Hard')"
     val=(name, Co, Qu, Per)
     cursor.execute(mySQLText,val)

     db.commit()

     print(cursor.rowcount, "record added")

     db.close()



     











          
