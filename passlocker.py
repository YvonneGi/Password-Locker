import pyperclip
from user import User
from credentials import Credentials
######USER######
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

    ########CREDENTIALS##################
def create_credentials(username, cred_app, cred_username, cred_password):
    '''
    Function to create a new user credentials
    '''
    new_credential = Credentials(username, cred_app, cred_username, cred_password)
    return new_credential  # end create_cred
def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()  # end save_cred
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
def delete_crededential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()  # end delete cred
# def generate_password():
# 		'''
# 		Function to generate a password automatically
# 		'''
# 		gen_pass = Credentials.generate_password()
# 		return gen_pass
################MAIN###############
def main():
  print(' ')
  print("Hello,Welcome to your Password  Locker.")
  while True:
      print("Use these short codes : ca - create a new account, lo - login,ex -exit ")
      short_code = input('Enter a choice: ').lower()
		if short_code=='ex':
		  break
		    elif short_code == 'ca':
					print("-"*60)
					print(' ')
					print('To create a new account:')
          username = input('Enter your Username - ').strip()
					password = input('Enter your Password - ').strip()
          save_user(create_user(Username,password))
          print(" ")
					print(f'New Account Created for: {username} using password: {password}')
            elif short_code == 'li':
							print("+"*60)
							print(' ')
							print('To login, enter your account details:')
							user_name = input('Enter your Username - ').strip()
							password = str(input('Enter your password - '))
							user_exists = login_user(username,password)
								if user_exists == user_name:
									print(" ")
									print(f'Welcome {user_name}. Please choose an option to continue.')
									print(' ')
  while True:
			print("+"*60)
			print('Navigation codes: \n cc-Create a Credential \n sc-search credential\n dc-Display Credentials \n dl-delete credential \n copy-Copy Password \n ex-Exit')
			short_code = input('Enter a choice: ').lower().strip()
			print("-"*60)
			if short_code == 'ex':
				print(" ")
				print(f'Goodbye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						App_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
          # cred_password = input('Enter your account\'s password - ').strip()
  	while True:
			print(' ')
			print("-"*60)
			print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
			psw_choice = input('Enter an option: ').lower().strip()
			print("-"*60)
				if psw_choice == 'ep':
					print(" ")
					password = input('Enter your password: ').strip()
					break
						elif psw_choice == 'gp':
							password = generate_password()
							break
						elif psw_choice == 'ex':
							break
						else:
							print('Oops! Wrong option entered. Try again.')
						  save_credential(create_credential(user_name,app_name,account_name,password)
              print(' ')
						  print(f'Credential Created: App Name: {app_name} - Account Name: {account_name} - Password: {password}')
						  print(' ')
					 	elif short_code == 'dc':
							print(' ')
							if display_credentials(user_name):
								print('Here is a list of all your credentials')
								print(' ')
							for credential in display_credentials(user_name):
								print(f'App Name: {credential.app_name} - Account Name: {credential.account_name} - Password: {credential.password}')
								print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
              print(' ')
						elif short_code == 'copy':
							print(' ')
							chosen_site = input('Enter the site name for the credential password to copy: ')
							copy_credential(chosen_site)
							print('')
						else:
							print('Oops! Wrong option entered. Try again.')

			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		else:
			print("+"*60)
			print(' ')
			print('Oops! Wrong option entered. Try again.')


if __name__ == '__main__':
	main()

####################################################################################   
				











