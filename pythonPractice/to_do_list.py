# TO DO list 
start_flag = True 
to_do_list = []

def add_task(to_do_list):
    print("Add your task ")
    task_input = str(input("To Do :-> "))
    to_do_list.append(task_input) 

def view_task(to_do_list):
    if not to_do_list:
        print("To Do List is empty ....")
    else: 
        for i, task in enumerate(to_do_list , start = 1 ):
            print(f"{i}, Task : {task}")

def remove_task(to_do_list,user_remove_input):
    user_remove_input = user_remove_input-1
    try:
        to_do_list.pop(user_remove_input)
    except IndexError:
        print("Index not Found....")
    
def ask_continue(exit_action):
    if exit_action.upper() == 'Y':
        return True 
    else:
        return False



while(start_flag):
    print("""
    Select the Operations which you want to perform in the To Do List 
    1. add_task
    2. view_task
    3. remove_task
    4. exit 
    """)
    try:
        user_input = int(input("User Input := "))
    except ValueError: 
        print("Select Integer Only......")
        continue
    
    if(user_input==1 or user_input==2 or user_input == 3 or user_input == 4):
        if(user_input == 1):
            add_task(to_do_list)
            print("Do you want to perform more Operation [Y/N]")
            action_user = str(input("Select Your Option := "))
            start_flag = ask_continue(exit_action=action_user)

        elif(user_input==2):
            view_task(to_do_list)
            print("Do you want to perform more Operation [Y/N]")
            action_user = str(input("Select Your Option : = "))
            start_flag = ask_continue(exit_action=action_user)
        elif(user_input ==3):
            user_remove_input = int(input("Which Task you want to remvoe from the TO_DO := "))
            remove_task(to_do_list, user_remove_input)
            print("Do you want to perform more Operation [Y/N]")
            action_user = str(input("Select Your Option : = "))
            start_flag = ask_continue(exit_action=action_user)
        elif(user_input ==4):
            start_flag = False
    else:
        print("Please select the right input...")


    



    

    




    

    




