#!/usr/bin/env Python3 ^^
# Contact Book, Python!
# Things Required In Contact Book: Name, Phone, Address

import sys
import os
import time

########################################
# Global List's Used In This Program!###
global ContactBook_Name
ContactBook_Name = []
global ContactBook_Phone_Number
ContactBook_Phone_Number = []
global ContactBook_Address
ContactBook_Address = []


#########################################
#  Global List's Used In This Program!  #
#########################################

def main():
    Contact_Book()


def Contact_Book():
    Clear_Screen()
    print("\t\t\t\tWelcome To Contact Book - 'An Open Source Python Application "
          "To Store Different Kinds Of Contact!'")
    print("""
      ______                                    ______              _     
     / _____)           _               _      (____  \            | |    
    | /      ___  ____ | |_  ____  ____| |_     ____)  ) ___   ___ | |  _ 
    | |     / _ \|  _ \|  _)/ _  |/ ___)  _)   |  __  ( / _ \ / _ \| | / )
    | \____| |_| | | | | |_( ( | ( (___| |__   | |__)  ) |_| | |_| | |< ( 
     \______)___/|_| |_|\___)_||_|\____)\___)  |______/ \___/ \___/|_| \_)  v1 - Steven """)

    print("\n\n")
    print("\t\t\t\t\t\t\t\t\tMain Menu")

    print("1. Add A Contact!")
    print("2. Remove A Contact!")
    print("3. Edit A Contact!")
    print("4. Save Contacts!")
    print("5. Print All Contacts!")
    print("6. Exit!")
    try:
        usr_choice = int(input("Enter your choice: "))
    except ValueError:
        Save_All_Contacts()
    if (usr_choice == 1):
        Add_A_Contact()
    elif (usr_choice == 2):
        Remove_A_Contact()
    elif (usr_choice == 3):
        Edit_A_Contact()
    elif (usr_choice == 4):
        Save_All_Contacts()
    elif (usr_choice == 5):
        Only_Print_All_Contacts()
    elif (usr_choice == 6):
        sys.exit(0)
    else:
        print("Error! Occurred!")


def Add_A_Contact():
    ContactBook_Name.append(input("Enter the Name Of The Person, Who's Contact You Want To Save: "))
    # To Get The Name of the person, Temp variable :)
    Clear_Screen()

    Current_Value = len(ContactBook_Name) - 1
    ContactBook_Address.append(input("Hit Enter To Leave The Address Field Blank!\nEnter The Address Of '{}': ".format(
        ContactBook_Name[Current_Value])))

    Clear_Screen()

    ContactBook_Phone_Number.append(input("Enter The Phone Number Of '{}': ".format(ContactBook_Name[Current_Value])))
    print("The Name Of The Person: {}\nAddress: {}\nPhone Number: {}".format(ContactBook_Name[Current_Value]
                                                                             , ContactBook_Address[Current_Value],
                                                                             ContactBook_Phone_Number[Current_Value]))

    print("Saved Successfully! '{}' in your Contact's!\n"
          "Note:: This is not saved in your computer yet but "
          "just in this program,\nAs soon as you close this application. "
          "The data will be removed"
          "\nIn order to save your data, Please goto main menu and select the option 3,"
          "'Save Contacts'\n".format(ContactBook_Name[Current_Value]))

    print("1. To Add More Contact's")
    print("2. To Goto Main Menu")

    def trying():
        try:
            usr_choice = int(input("Enter your choice: "))
        except ValueError:
            print("ValueError! Going back to main menu")
            trying()
            main()
        if (usr_choice == 1):
            Add_A_Contact()
        elif (usr_choice == 2):
            main()
        else:
            print("Error!")
            print("Please Choose 1 or 2 according to your choice!")
            trying()

    trying()


def Remove_A_Contact():
    Clear_Screen()
    print("\t\t\tRemove Contact's!")
    print("All of your contact's")

    Print_All_Contacts()
    Delete_Contact2()


def Delete_Contact2():
    # Remove function, In order to loop through, if user enters something else rather then number's!
    try:
        Index_Number = int(input("Enter the index number of the contact which you want to delete: "))
    except ValueError:
        print("Value Error! Try again!")

    if (Index_Number > len(ContactBook_Name)):
        print("Sorry, This Contact Doesn't Exits!")

    else:
        print("Do you really want to delete {}'s contact ?".format(ContactBook_Name[Index_Number]))
        choice = input("Enter your choice (y/n): ")

        if (choice == "y" or choice == "Y"):
            Clear_Screen()
            # If User Really Want's To Delete The Data
            print("Deleting {}'s Contact........".format(ContactBook_Name[Index_Number]))
            time.sleep(1)
            print("Deleted {}'s Contact Successfully!".format(ContactBook_Name[Index_Number]))

            # Using Temporary Names of the names that are contained in the list, So we can easily delete them :D
            temp_contactbook_name = ContactBook_Name[Index_Number]
            temp_contactbook_phone = ContactBook_Phone_Number[Index_Number]
            temp_contactbook_address = ContactBook_Address[Index_Number]

            # Deleting The Contact which user asked us to delete :D
            ContactBook_Name.remove(temp_contactbook_name)
            ContactBook_Phone_Number.remove(temp_contactbook_phone)
            ContactBook_Address.remove(temp_contactbook_address)
            Choice_Loop()


        elif (choice == "n" or choice == "N"):
            print("Deleting Aborted!")
            print("Going back to main menu ")
            main()

# The Code after finishing the deleting operation !
def Choice_Loop():
    print("Do you want to delete more contacts y/n? ")
    delete_more = input("Enter your choice: ")
    if (delete_more == "Y" or delete_more == "y"):
        Remove_A_Contact()
    elif (delete_more == "n" or delete_more == "N"):
        main()
    else:
        print("Please choose y for Yes, n for No!")
        Choice_Loop()


def Edit_A_Contact():
    Clear_Screen()
    print("Edit A Contact!")
    Print_All_Contacts()

    try:
        Index_Number = int(input("Enter the index number of the contact which you want to edit: "))

    except ValueError:

        print("Value Error! Try again!")
        Edit_A_Contact()

    print("So you want edit {}'s contact".format(ContactBook_Name[Index_Number]))
    print("Name: '{}'".format(ContactBook_Name[Index_Number]))
    print("Address: '{}'".format(ContactBook_Address[Index_Number]))
    print("PhoneNumber: {}".format(ContactBook_Phone_Number[Index_Number]))
    print("\nWhat do you want to edit ? ")
    print("1. Edit Name")
    print("2. Edit Address")
    print("3. Edit Phone Number")
    print("4. Back To Main_Menu")

    user_edit = int(input("Enter your choice: "))
    if (user_edit == 1):
        temp_name_change = input("Enter the new name for {}: ".format(ContactBook_Name[Index_Number]))
        ContactBook_Name[Index_Number] = temp_name_change
        print("Succesfully changed the name ! ")
        print("The Name after changing: ", ContactBook_Name[Index_Number])
        print("Do you want to change more records y/n? ")
        change_more = input("Enter your choice: ")
        if (change_more == "y" or change_more == "Y"):
            Edit_A_Contact()
        elif (change_more == "n" or change_more == "n"):
            main()

    if (user_edit == 2):
        temp_name_change = input("Enter the new address for {}: ".format(ContactBook_Name[Index_Number]))
        ContactBook_Address[Index_Number] = temp_name_change
        print("Succesfully changed the address ! ")
        print("The Address after changing: ", ContactBook_Address[Index_Number])
        print("Do you want to change more records y/n? ")
        change_more = input("Enter your choice: ")
        if (change_more == "y" or change_more == "Y"):
            Edit_A_Contact()
        elif (change_more == "n" or change_more == "n"):
            main()
    if (user_edit == 3):
        temp_name_change = input("Enter the new name for {}: ".format(ContactBook_Name[Index_Number]))
        ContactBook_Phone_Number[Index_Number] = temp_name_change
        print("Succesfully changed the phone number ! ")
        print("The PhoneNumber after changing: ", ContactBook_Phone_Number[Index_Number])
        print("Do you want to change more records y/n? ")
        change_more = input("Enter your choice: ")
        if (change_more == "y" or change_more == "Y"):
            Edit_A_Contact()
        elif (change_more == "n" or change_more == "n"):
            main()

    if (user_edit == 4):
        main()


def Save_All_Contacts():
    Clear_Screen()
    print("Save Contact's!")
    print("These are your contact's!")
    Print_All_Contacts()

    print("Do you really wanna save your contact's ?")
    user_choice = input("Enter your choice: ")
    if (user_choice == "Y" or user_choice == "y"):
        pass
    elif (user_choice == "N" or user_choice == "n"):
        print("Operation Aborted !")
        print("Going Back To Main Menu!")
        main()



    # The Code to Change Directory To The Desktop!
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    os.chdir(desktop)

    # We will try to create a directory, If directory already exits this os.mkdir will makes issues, Therefore to
    # Ignore It we will use try/except :D

    try:
        os.mkdir('Contact Book - Open Source Contact Book!')
    except FileExistsError:
        pass
    print(os.getcwd())
    os.chdir('Contact Book - Open Source Contact Book!')
    size_of_list = len(ContactBook_Name)

    save = open("Contacts_Saved.txt", 'w+')

    save.write("""
          ______                                    ______              _     
         / _____)           _               _      (____  \            | |    
        | /      ___  ____ | |_  ____  ____| |_     ____)  ) ___   ___ | |  _ 
        | |     / _ \|  _ \|  _)/ _  |/ ___)  _)   |  __  ( / _ \ / _ \| | / )
        | \____| |_| | | | | |_( ( | ( (___| |__   | |__)  ) |_| | |_| | |< ( 
         \______)___/|_| |_|\___)_||_|\____)\___)  |______/ \___/ \___/|_| \_)  v1 - Steven \n\n""")

    save.write("============================================================================="
               "==============================================================================="
               "=====================")
    for x in range(size_of_list):
        if (x == 0):
            save.write("\n")
            save.write("Name: {}\n".format(ContactBook_Name[x]))
            save.write("Address: {}\n".format(ContactBook_Phone_Number[x]))
            save.write("Contact: {}\n".format(ContactBook_Address[x]))
            save.write("==========================================================================="
                   "==========================================================================="
                   "=================\n")
        else:
            save.write("Name: {}\n".format(ContactBook_Name[x]))
            save.write("Address: {}\n".format(ContactBook_Phone_Number[x]))
            save.write("Contact: {}\n".format(ContactBook_Address[x]))
            save.write("==========================================================================="
                       "==========================================================================="
                       "=================\n")

    save.close()

    # The Code after saving the contact's

    print("Successfully Saved All The Contact's!")
    print("Your Contact Is Saved Here: {}".format(os.getcwd()))
    time.sleep(2)
    main()


def Clear_Screen():  # Function Used To Clear Screen In Windows Os, Note: Will Not Work In Linux XD!
    os.system('cls')


def Print_All_Contacts(): # This method will only be used to print all the contacts!
    if (len(ContactBook_Name) > 0):
        for x in range(len(ContactBook_Name)):
            print("==========================================================================================")
            print("Index Number Of Contact: {}".format(x))
            print("Name: {}\nAddress: {}\nPhone Number: {}".format(ContactBook_Name[x], ContactBook_Address[x],
                                                                   ContactBook_Phone_Number[x]))
            print("===========================================================================================\n")

    else:
        print("Sorry, You Don't Have Any Contacts Saved Yet!")
        time.sleep(2)
        main()

def Only_Print_All_Contacts():
    if (len(ContactBook_Name) > 0):
        for x in range(len(ContactBook_Name)):
            print("==========================================================================================")
            print("Index Number Of Contact: {}".format(x))
            print("Name: {}\nAddress: {}\nPhone Number: {}".format(ContactBook_Name[x], ContactBook_Address[x],
                                                                   ContactBook_Phone_Number[x]))
            print("===========================================================================================\n")

    else:
        print("Sorry, You Don't Have Any Contacts Saved Yet!")
        time.sleep(2)
        main()
    def Loop():
        print("Do you want to goto main menu ? ")
        print("1. Main Menu")
        print("2. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error! Please select 1 to Goto Main Menu or 2 To Exit The Application!")
            Loop()

        if (choice == 1):
            time.sleep(1)
            print("Going To Main Menu..........")
            time.sleep(1)
            main()

        elif (choice == 2):
            print("Exiting..................")
            time.sleep(1)
            sys.exit(0) # Exit's the application

    Loop()
main()