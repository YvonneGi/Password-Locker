#!/usr/bin/env python3.6
import pyperclip
import random
from user import User
from credentials import Credentials
def create_account(user_name,password):
    '''
    Function to create a new account
    '''
    new_user = User(user_name,password)
    return new_user
def save_user(user):
    '''
    Function to save account
    '''
    user.save_user()
def verify_user(username,password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = User.login_by_userpass(username,password)
    return checking_user
# def generate_password():
#     '''
#     Function to generate a password automatically
#     '''
#     gen_pass = Credentials.generate_password()
#     return gen_pass

def create_credential(username,cred_app,cred_username,cred_password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(username,cred_app,cred_username,cred_password)
    return new_credential    
def save_credential(credentials):
    '''
    Function to save credential
    '''
    credentials.save_credentials()
def find_credential(username):
    '''
    Function that finds a credential by username and returns the user credential
    '''
    return Credentials.find_by_username(username)
def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()
def delete_credential(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credential()
def copy_username(username):
    '''
    Function to copy a credentials details to the clipboard
    '''
    return Credentials.copy_username(username)
def main():
                print("Hello Welcome to your Password_locker.")
                print('\n')

                # while True:
                print("Use these short codes : ca - create a new account, lo -login,ex -exit")

                short_code = input().lower()

                if short_code == 'ca':
                                        print("New Account")
                                        print("+"*60)

                                        print ("Username....")
                                        user_name = input()

                                        print("Password ...")
                                        password = input()
                                        
                                        save_user(create_account(user_name,password)) # create and save new account.
                                        print ('\n')
                                        print(f"New account {user_name} {password} created")
                                        print ('\n')

                elif short_code == 'lo':

                                                print('To login, enter your account details : ')
                                                print("+"*60)
                                                user_name = input('Enter your Username - ')
                                                password = str(input('Enter your password - '))
                                                user_exist = verify_user(user_name,password)
                                                if user_exist == user_name:
                                                        print(" ")
                                                        print(f'Welcome {user_name}. Please choose an option to continue.')
                                                                                                
                while True:
                                print("Use these short codes : cc - create a credential,dc-display credential,dl-delete credential,cp-copy credential,ex -exit")

                                short_code = input().lower()

                                if short_code == 'cc':
                                        print("Enter your credential details:")
                                        print("+"*60)

                                        print ("User-name....")
                                        username = input()

                                        print ("Enter the App-name:")
                                        cred_app = input()

                                        print("Enter your account Username:")
                                        cred_username = input()
                                                                        
                                        print("-"*60)
                                        print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
                                        psw_choice = input('Enter an option: ').lower()
                                        print("-"*60)
                                        if psw_choice == 'ep':
                                                print(" ")
                                                cred_password = input('Enter your password: ')
                                                save_credential(create_credential(username,cred_app,cred_username,cred_password)) # create and save new credential.
                                                print (' ')
                                                print(f"New credential {username}  {cred_app}   {cred_username}   {cred_password} created")
                                                print ('\n')
                                        elif psw_choice == 'gp':
                                                s="abcdefghijklmnopqrstuvwxyz0123456789"
                                                cred_password=''.join(random.choice(s) for _ in range(8))
                                               
                                        
                                                save_credential(create_credential(username,cred_app,cred_username,cred_password)) # create and save new credential.
                                                print (' ')
                                                print(f"New credential {username}  {cred_app}   {cred_username}   {cred_password} created")
                                                print ('\n')
                                elif short_code == 'dc':
                                        if display_credentials():
                                                print("Here is a list of all your credentials:")
                                                print('\n')
                                                for credential in display_credentials():
                                                        print(f"{credential.username} {credential.cred_app} {credential.cred_username}  {credential.cred_password}")
                                                        print('\n')
                                        else:
                                                        print('\n')
                                                        print("You dont seem to have any credentials saved yet")
                                                        print('\n')
                                elif short_code == 'dl':
                                                print("       Delete Credential")
                                                print("     "+"="*20)
                                                print('\n')

                                                cred_app = input("Enter App Name:")
                                                found_credential = find_credential(username)
                                                if found_credential:
                                                        print(f"Here are the credentials for {found_credential.cred_app}:")
                                                        print(f"User Account: {found_credential.cred_username}")
                                                        print(f"Password: {found_credential.cred_password}")
                                                if input("Are you sure you want to delete it? (Y/N)").lower() == "Y":
                                                                delete_credential(found_credential)
                                                                # print()
                                                                input(f"Credential for {found_credential.cred_app} deleted.")
                                                                print("Press Enter to continue")
                                                else:
                                                                print(f"Credential Not Found for {cred_app}!")
                                                                print("Press Enter to continue")
                                                                input()  # end choice = d (Delete Credential)
                                elif short_code == 'cp':
                                                username = input('Enter the username for the credential to copy: ')
                                                copy_username(username)
                                                                        
                                                # else:
                                                #         print('Oops! Wrong option entered. Try again.')


                                elif short_code == "ex":
                                        print("Bye .......")
                                        break
                                             
                                else:
                                                print("I really didn't get that. Please use the short codes")



                                        
                               
if __name__ == '__main__':

    main()