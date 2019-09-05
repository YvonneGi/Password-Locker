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

  ########search account by its credentials###
   
