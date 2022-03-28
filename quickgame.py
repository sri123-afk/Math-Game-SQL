# Importing random in order to mix the numbers given to the user
import random

# Defining the gen number
def genNumber (maxNum):
    return random.randint(0,maxNum)

# Defining and using the random to give different numbers
def Quickgame():
    print("\n                             Quick Game                 ")

    # Creating variables
    name=input("Enter your name: ")
    Co=0
    In=0
    num1=0
    num2=0
    Uans=0
    ans=0


    # Using for to range the numbers to maximum of 5
    questions=[ ]
    for i in range(5):
        q = str(genNumber(10)) + " + " + str(genNumber(10))
        answer = int(input(q+ " = "))
        questions.append((q,answer))
    # Using IF condtion to show whether the answer is correct or wrong
    print("---------------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------")
    # Using for to give the answer and the question after typing the answer by the user
    print("              Quick Results                                                ")
    for q,a in questions:
        correct_answer = eval (q)
        if correct_answer == a:
            print(q,"=",a,"Correct")
            Co+=1
        else:
            print(q,"=",a,"Incorrect", "Correct answer","[",correct_answer,"]")
            In+=1
    print("------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
     #Programming to show the Game Results the name, the correct and wrong answers plus the final
    Per=int((Co/5)*100)
    print("*************************************************************")
    print("           GAMERESULTS               ")
    print("\n Your name is", name)
    print("\n Questions answered is",Co)
    print("\n Question not answered is",In)
    print("\n Final score out of 5 is",Co)
    print("\n Your percentage is", Per)
    print("**************************************************************")

    import mysql.connector

    # open database connection with a dictionery

    conDict = {'host' : 'localhost', 'database' : 'dl_game', 'user' : 'root', 'password' : ''}

    db = mysql.connector.connect(**conDict)

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query using execute() method.
    mySQLText = "INSERT INTO quickgame (Name, Correct, total_questions, Percentage) VALUES (%s, %s, 5, %s)"
    val=(name, Co, Per )
    cursor.execute(mySQLText,val)

    
    db.commit()

    print(cursor.rowcount, "record added")

    db.close()






