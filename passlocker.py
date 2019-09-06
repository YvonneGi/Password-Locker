#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

   #######USER########


def create_user(username, password):
        '''
        Function to create a new user account
        '''
        new_user = User(username, password)
        return new_user  # end create_user


def save_user(user):
        '''
        Function to save user
        '''
        user.save_user()  # end save_user


def login_user(username, password):
        '''
        Function that finds a user by username/password and returns the user account
        '''
        return User.login_by_userpass(username, password)  # end login

    #######CREDENTIALS####################


def create_credentials(username, cred_app, cred_username, cred_password):
        '''
        Function to create a new user credentials
        '''
        new_credential = Credentials(
            username, cred_app, cred_username, cred_password)
        return new_credential  # end create_cred


def save_credentials(credential):
        '''
        Function to save credential
        '''
        credential.save_credential()  # end save_cred


def delete_crededential(credential):
        '''
        Function to delete a credential
        '''
        credential.delete_credential()  # end delete cred


def find_credential(username):
        '''
        Function that finds a credential by username and returns the user credential
        '''
        return Credentials.find_by_username(username)  # end find cred


def display_credentials():
        '''
        Function that returns all the saved credentials
        '''
        return Credentials.display_credentials()  # end display cred

    ##########GENERIC################################


def menu():
        '''
        Function to display the Main Menu
        '''
        print("Hello,Welcome to your accounts manager!")
        print('\n')
        print('\n')
        print("             What would you like to do?")
        print('\n')
        print("             1. Sign Up")
        print('\n')
        print("             2. Login")
        print('\n')
        print("             3. Exit")  # end menu


def log_menu():
        '''
        Function to display the menu for a logged in user
        '''

        print("             a. Add Credential")
        print("             b. Search Credential")
        print("             c. Display all Credentials")
        print("             d. Delete Credential")
        print("             e. Logout")  # end log_menu

# def generate_password(pass_length):
#     '''
#     Function to generate a random password with a custom length
#     '''
#     char = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
#     gen_pass = "".join(random.choice(char) for _ in range(pass_length))
#     return gen_pass#end generate_password


############MAIN####################################


def main():
    menu_choice = 0
    while menu_choice != 3:
        menu()
        print("\n               Your Choice: ")
        try:
            menu_choice = int(input("               "))
        except:
            print("Please Make a Valid Choice !")
            print('Press Enter to continue')
            input()

        if menu_choice == 3:
            print('Thanks For Using --passlocker--')
            print('Press Enter Quit')
            input()
            break  # end if menu_choice = 3
          elif menu_choice ==1:
            print ("Create new account")
            print("     "+"="*10)
            print ('\n')
            print("     Username:")
            u_name = input()
            print ('\n')
            print("     Password:")
            p_word = input()
            save_user(create_user(u_name, p_word))  # create and save new user.
            print ('\n')
            print(f" New User {u_name} / Password: {p_word} created")
            print ('Press Enter to continue')
            input()#end if menu_choice = 1
          elif menu_choice == 2:
            print("     Enter Your Username and Password")
            print("     "+"="*10)
            print ('\n')
            print("     Username:")
            u_name = input()
            print ('\n')
            print("     Password:")
            p_word = input()
            logged = log_user(u_name, p_word)
             if logged :
                u_name = logged.username

                session_header(u_name)

                login_choice = ""
                while login_choice != "e":
                    session_header(u_name)

                    log_menu()
                    print ('\n              Your Choice: ')
                    login_choice = input("             ")

                    if login_choice == "a":
                        session_header(u_name)

                        print("       Add Credential")
                        print("     "+"="*20)
                        print ('\n')

   

if __name__ == '__main__':

  main()

##################################################################################
