# ---------------------------------------------------------------------------- #
#
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Matthew Lord,2023.02.22,Created file on my local computer
# Matthew Lord,2023.02.23,Created ToDoFile.txt
# Matthew Lord,2023.02.23,Completed script code including controls to limit user
#     input for the menu and priority options
#
# ---------------------------------------------------------------------------- #


# DATA ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection

# END DATA ------------------------------------------------------------------ #


# PROCESSING  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"task": task.strip(), "priority": priority.strip()}
            list_of_rows.append(row)
        file.close()

        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows
        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want to add more data to:
        :return: (list) of dictionary rows
        """
        row = {"task": str(task).strip(), "priority": str(priority).strip()}
        # add the new task/priority pair to the list of table rows
        list_of_rows.append(row)

        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from a list of dictionary rows
        :param task: (string) with name of task:
        :param list_of_rows: (list) you want to remove data from:
        :return: (list) of dictionary rows
        """
        # function variables
        counter = 0
        dic_row = {}

        # set counter to check when looping through the full table/list
        counter = 1
        # loop through each row in the list
        for item in list_of_rows:
            # get the row of text and assign it to a variable
            dic_row = item
            # check if user entry is NOT found in the table
            if dic_row["task"] != task:
                # if the entry is NOT found and we have reached the end of our table/list
                if counter >= len(list_of_rows):
                    # inform the user that the task they entered is not in the table/list
                    print("\nThe item", task, "has not been found in the table.")
                    print()  # Add an extra line for looks
            # check if user entry is found in the table
            elif dic_row["task"] == task:
                # remove the item from the table/list
                list_of_rows.remove(item)
                # inform the user that the item has been removed
                print("\nThe item", task, "has been removed from the list.")
                print()  # Add an extra line for looks
                break  # continue to the while loop what task is found and deleted from table/list
            # increase the counter
            counter += 1

        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want saved to file:
        :return: (list) of dictionary rows
        """
        # open the file to save the data to
        file_obj = open(file_name, "w")
        # format the lstTable row by row
        for row in list_of_rows:
            dic_row = row  # assign the row to a dictionary
            # save the data, formatted as CSV
            file_obj.write(dic_row["task"] + "," + dic_row["priority"] + "\n")
        file_obj.close()  # close the file
        print("Data Saved!")
        print()  # Add an extra line for looks

        return list_of_rows

# END PROCESSING  ----------------------------------------------------------- #


# PRESENTATION (INPUT/OUTPUT)  ---------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = "0"
        choices = ["1", "2", "3", "4"]
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
            if choice not in choices:
                print("Please only select menu option 1 - 4...")
        print()  # Add an extra line for looks

        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")

        # print table header
        print("TASK (PRIORITY)")

        # print each row of data in the table/list
        for row in list_of_rows:
            print(row["task"] + " (" + row["priority"] + ")")

        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list
        :return: (string, string) with task and priority
        """
        # create list of priorities
        priorities = ["high", "middle", "low"]
        # engage user for a new task
        task = str(input("Please enter a new task: "))
        # engage user for the priority of the new task
        priority = ""
        # limit options for priority
        while priority != "high" and priority != "middle" and priority != "low":
            # get user input
            priority = str(input("Please enter a priority for the new task (high, middle, low): ")).strip()
            # make lower case
            priority = priority.lower()
            # check if user input is within selectable options
            if priority not in priorities:
                # remind user of options
                print("Please only select high, middle, or low...")
        print()  # Add an extra line for looks

        return task, priority

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list
        :return: (string) with task
        """
        # engage user for task to remove from table/list
        task = str(input("Enter a task to remove: "))

        return task

# END PRESENTATION (INPUT/OUTPUT)  ------------------------------------------ #


# MAIN BODY OF SCRIPT  ------------------------------------------------------ #
# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file( file_name = file_name_str, list_of_rows = table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows = table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        # ask user for new task/priority data
        task, priority = IO.input_new_task_and_priority()
        # add new task and priority to the table/list
        table_lst = Processor.add_data_to_list(task = task, priority = priority, list_of_rows = table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        table_lst = Processor.remove_data_from_list(task = task, list_of_rows = table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor.write_data_to_file(file_name = file_name_str, list_of_rows = table_lst)
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        # query user if they would like to save the file prior to exiting
        to_exit = input("Would you like to save the file before exiting the program 'y' or 'n'?: ")
        # if user selects yes
        if to_exit.lower().strip() == "y":
            # save to file
            table_lst = Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
            print("Goodbye!")
        else:
            print("Goodbye!")
        break  # by exiting loop

# END MAIN BODY OF SCRIPT  -------------------------------------------------- #
