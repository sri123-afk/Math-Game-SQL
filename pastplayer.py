import mysql.connector

def result():
       conDict = {'host':'localhost','user':'root' , 'database':"dl_game" ,'password':''}
       db=mysql.connector.connect(**conDict)
# prepare a cursor object using cursor() method
       cursor = db.cursor()

# execute SQL query using execute() method.
       cursor.execute("SELECT * FROM quickgame")

# Fetch results using fetchall() method.
       data = cursor.fetchall()
       print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
       print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
       print("Quickgame Results")

       print(":Name        : Correct      : Total questions     : Percentage    : ")

       for item in data:
           print(2*" ",item[0],(15," "),item[1],(10," "),
                  item[2],(22," "),item[3],(24," "))
       print("Rows recorded = ",len(data));
       
       print("[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
       print("[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")

# Disconnect from server
       db.close()



       conDict = {'host':'localhost','user':'root' , 'database':"dl_game" ,'password':''}
       db=mysql.connector.connect(**conDict)
# prepare a cursor object using cursor() method
       cursor = db.cursor()

# execute SQL query using execute() method.
       cursor.execute("SELECT * FROM customgame")

# Fetch results using fetchall() method.
       data = cursor.fetchall()
       print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
       print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
       print("Customgame Results")

       print(":        Name       :         Correct       :       Total questions       :       Percentage        : ")

       for item in data:
              print(item)
       print("Rows recorded = ",len(data));
       
       print("[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
       print("[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")

# Disconnect from server
       db.close()
       





