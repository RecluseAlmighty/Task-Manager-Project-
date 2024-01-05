#=====importing libraries===========
from datetime import date

#====Login Section====

def login(): # Defining login function..
    username = input("Please enter your username: ") # Initializing username and password variables
    password = input("Please enter your password: ")

    for line in open("user.txt","r").readlines(): # Reading through each line
        logins_info = [x.strip() for x in line.split(', ')] # and splitting the lines by ', ' and saving each word in variable 'logins_info' with the '\n'
        #logins_info = line.replace("\n","").split(', ')
        if username == logins_info[0] and password == logins_info[1]: # Checking that the inputted username and password match the first two words in file
            print("\nYou have successfully logged in!\n")
            return username # Returning the username from the function to be used in the rest of the program
    else:
        print("\nIncorrect login details. Please try again.\n")
        return login() # Else send user back to begin of login function process


def user_register(): # Defining user registration function..
            
        print("\nYour username should be a minimum of 4 characters and a maximum of 15 characters.")
        username = input("Please enter your desired username: " ) # Requesting username..
            
        for line in open("user.txt","r").readlines(): # Reading through text file
            logins_info = [x.strip() for x in line.split(', ')] # Splitting into words..
        if len(username) < 15 and len(username) > 3 and username != logins_info: # Creating parameters that inputted username must fulfil
            with open("user.txt","a") as f: # If fulfilled then write username to text file
                f.write("\n")
                f.write(username)
                f.write(", ")
                print(f"Hi there {username}!")
        if len(username) > 15 or len(username) <= 3 or username == logins_info: # If parameters are not met..
            print("Your username is invalid or taken. Try again..")
            return user_register() # Then return user to beginning of user registration process


def password_register(): # Defining password registration function..

        special_symbol =['$', '@', '#', '%', '!', '£', '*', '&', '?'] # Creating variable for special symbols

        print("\nYour password may not be longer than 20 characters or shorter than 10 characters.\nIt must also contain at least one capital letter, one number and one special character.")
        password = input("\nPlease enter your desired password: ") # Requesting password..
                
        while len(password) < 20 and len(password) > 10 and password.isupper and password.isdigit and any(char in special_symbol for char in password): # Creating parameters that inputted password must fulfil
            password_confirm = input("\nPlease confirm your desired password: ") # If password fulfills parameters then request password confirmation
            if password_confirm == password: # If passwords match write password to text file
                with open("user.txt","a") as s:
                    s.write(password)
                    print(f"\nYou are now registered! Your password is {password}\n")
                    break
                    #exit()

            if password_confirm != password: # If passwords do not match then return user to begining of password registration process
                print("Your confirmation password does not match your initial desired password. Try again..\n")
                continue
                
        if len(password) > 20 or len(password) < 10 or not password.isupper or not password.isdigit or not any(char in special_symbol for char in password):
            print("Your password is invalid. Try again..\n")
            return password_register() # If passwords does not meet parameters then return user to begining of password registration process


def add_task(): # Defining add task function..

        username_ref = input("\nPlease enter the username of whom the task will be assigned to: ") # Requesting username task will be assigned to

        for line in open("user.txt","r").readlines(): # Reading through text file
            logins_info = [x.strip() for x in line.split(', ')] # Splitting into words..
            if username_ref == logins_info[0]: # If the username is a registered user then continue recieving task information
                task_title = input(f"\nPlease provide the title of the task for {username_ref}: ")
                task_description = input(f"\nPlease give a description for the task {task_title}: ")
                
                if username_ref != logins_info[0]:
                    print(f"\n{username_ref} does not exist. Please try again..")
                    return add_task() # If the username is not a registered user then return user to beginning of process

        while True:
                try:
                    d1, m1, y1 = (int(x) for x in input(f"\nPlease provide the due date for {task_title} (YYYY/MM/DD): ").split('/')) # Recieving 'due date' of task and formatting to date function
                    due_date = date(d1, m1, y1)

                    d2, m2, y2 = (int(x) for x in input(f"\nPlease provide todays date (YYYY/MM/DD): ").split('/')) # Recieving 'todays date' of task and formatting to date function
                    todays_date = date(d2, m2, y2)

                    if due_date > todays_date : # If due date is after the current date then write the task information inputs to the text file
                        with open("tasks.txt","a") as t:
                            t.write("\n")
                            t.write(username_ref)
                            t.write(", ")
                            t.write(task_title)
                            t.write(", ")
                            t.write(task_description)
                            t.write(", ")
                            t.write(str(due_date).replace("-","/"))
                            t.write(", ")
                            t.write(str(todays_date).replace("-","/"))
                            t.write(", ")
                            t.write("No")
                            print(f"The task for {username_ref} was successfully added to the database!")
                            break

                    if due_date <= todays_date : 
                        print("\nThis due date has already expired. Try again..\n")
                        return add_task() # If due date is the same as or before the current date then return user to beginning of add task function
                                
                except Exception :
                    print("That is not a valid date. Try again..")


def read_task(): # Defining read task function..

        for line in open("tasks.txt","r").readlines(): # Reading through text file
            task_info = line.split(', ') # Splitting into words..
            print(f"\nTask : \t {task_info[1]}") # Printing task and user information..
            print(f"\nAssigned to : \t {task_info[0]}")
            print(f"\nDate Assigned : \t {task_info[3]}")
            print(f"\nDue Date : \t {task_info[4]}")
            print(f"\nTask Complete? : \t {task_info[5]}")
            print(f"\nTask Description : \t {task_info[2]}")
            print(f"\nUse taskManager.py to assign each team member with appropriate tasks\n")
            
            
def read_user_tasks(): # Defining read user tasks function..

        for line in open("user.txt","r").readlines(): # Reading through text file
            logins_info = line.split(', ') # Splitting into words..
            if username == logins_info[0]: # If the username is a registered user then..
                for line in open("tasks.txt","r").readlines():
                    task_info = line.split(', ')
                    if username == task_info[0]: # Output task information if the line starts if the username is the one taken from the login function
                        print(f"\nTask : \t {task_info[1]}")
                        print(f"\nDate Assigned : \t {task_info[3]}")
                        print(f"\nDue Date : \t {task_info[4]}")
                        print(f"\nTask Complete? : \t {task_info[5]}")
                        print(f"\nTask Description : \t {task_info[2]}")
                        print(f"\nUse taskManager.py to assign each team member with appropriate tasks\n")


def display_stats(): # Defining display stats function..

        with open("user.txt","r") as k: # Opening the user text file 
            user_counter = len(k.readlines()) # 'user_counter' contains the number of lines in 'user' text file
            print(f"\nTotal number of users : \t {user_counter}") # Output number of users
        with open("tasks.txt","r") as n:
            task_counter = len(n.readlines()) # 'task_counter' contains the number of lines in 'task' text file
            print(f"\nTotal number of tasks : \t {task_counter}\n") # Output number of tasks
            

print("Welcome to the Task Manager! Log in so we can get started..\n")           
username = login()
                       
while True:
    if username == "admin": # If 'username' is 'admin' then..
        # Present the menu to the user and 
        # make sure that the user input is converted to lower case.
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    d - display statistics                 
    e - exit
    : ''').lower()
        
    if username != "admin": # If 'username' is not 'admin' then..
        # Present the menu to the user and 
        # make sure that the user input is converted to lower case.
        menu = input('''Select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()


    if menu == 'r':
                    
        user_register()

        password_register()
        

    elif menu == 'a':
        
        add_task()
        

    elif menu == 'va':
            
        read_task()


    elif menu == 'vm':
        
        read_user_tasks()


    elif menu == 'd':

        display_stats()


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")