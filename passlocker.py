#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
def create_account(user_name,password):
    '''
    Function to create a new account
    '''
    new_user = User(user_name,password)
    return new_user
def save_accounts(user):
    '''
    Function to save account
    '''
    user.save_user()
# def login_account(user_name,password):
#     '''
#     Function that finds a account by username and password
#     '''
#     return User.login_by_userpass(user_name,password)
def verify_user(username,password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = Credentials.check_user(username,password)
    return checking_user
def generate_password():
    '''
    Function to generate a password automatically
    '''
    gen_pass = Credentials.generate_password()
    return gen_pass

def create_credential(username,app_name,cred_username,cred_password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(username,app_name,cred_username,cred_password)
    return new_credential    
def save_credentials(credentials):
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
def del_credential(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credential()
def main():
    print("Hello Welcome to your Password_locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : ca - create a new account, lo -login,ex -exit")

                    short_code = input().lower()

                    if short_code == 'ca':
                            print("New Account")
                            print("+"*60)

                            print ("Username....")
                            user_name = input()

                            print("Password ...")
                            password = input()
                            
                            save_accounts(create_account(user_name,password)) # create and save new account.
                            print ('\n')
                            print(f"New account {user_name} {password} created")
                            print ('\n')

                    elif short_code == 'lo':

		            print('To login, enter your account details:')
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
                            app_name = input()

                            print("Enter your account Username:")
                            cred_username = input()

    while True:
					                
			    print("-"*60)
			    print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
			    psw_choice = input('Enter an option: ').lower()
			    print("-"*60)
			    if psw_choice == 'ep':
				    print(" ")
				    password = input('Enter your password: ')
					break
			    elif psw_choice == 'gp':
				    password = generate_password()
					break
			    elif psw_choice == 'ex':
					break
			    else:
				    print('Oops! Wrong option entered. Try again.')
                                    save_credentials(create_credential(username,app_name,cred_username,cred_password)) # create and save new credential.
                                    print ('\n')
                                    print(f"New credential {username} {app_name} {cred_username} {cred_password} created")
                                    print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your credentials")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"{credential.username} {credential.cred_app} {credential.cred_username}{credential.cred_password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')
                   elif short_code == 'dl':
                           print("       Delete Credential")
                           print("     "+"="*20)
                           print('\n')

                           app_name = input("Enter App Name:")
                           found_credential = find_credential(u_name)
                    if found_credential:
                        print(f"Here are the credentials for {found_credential.cred_app}:")
                        print(f"User Account: {found_credential.cred_username}")
                        print(f"Password: {found_credential.cred_password}")
                                if input("Are you sure you want to delete it? (Y/N)").upper() == "Y":
                                        delete_credential(found_credential)
                                        print()
                                        print("Press Enter to continue")
                                        input(f"Credentials for {found_credential.cred_app} deleted.")
                                else:
                                        print(f"Credentials Not Found for {app_name}!")
                                        print("Press Enter to continue")
                                        input()  # end choice = d (Delete Credential)
                  elif short_code == 'cp':
                          chosen_site = input('Enter the site name for the credential password to copy: ')
			  copy_credential(chosen_site)
						
			else:
				print('Oops! Wrong option entered. Try again.')

			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		        else:
			        print("-"*60)
			        print('Oops! Wrong option entered. Try again.')


                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

  main()