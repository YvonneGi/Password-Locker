import pyperclip
class Credentials:
    """
    Class that generates new instances of users
    """

    cred_list = []  # Empty user user_list

    def __init__(self, username, cred_app, cred_username, cred_password):
        """
        __init__ method that helps us define properties for our objects.
        """
        self.username = username
        self.cred_app = cred_app
        self.cred_username = cred_username
        self.cred_password = cred_password  # end init cred

    ##### save method to save new object#####

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into cred_list
        '''

        Credentials.cred_list.append(self)

  ###### delete method to delete credentials when needed####

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credential from the cred_list
        '''

        Credentials.cred_list.remove(self)
    # def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
	# 	'''
	# 	Function to generate an 8 character password for a credential
	# 	'''
	# 	gen_pass=''.join(random.choice(char) for _ in range(size))
	# 	return gen_pass

  #####search for a credential in stored credentials#####
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a credential that matches that username.
        Args:
            Username: username to search for
        Returns :
            Credential of person that matches the username.
        '''
        for credential in cls.cred_list:
            if credential.username == username:
                return credential

  ########Display account by its credentials###
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credintials list
        '''
        return cls.cred_list

    @classmethod
    def copy_username(cls,username):
        credential_found = Credentials.find_by_username(username)
        pyperclip.copy(credential_found.username)

###############################################################################
