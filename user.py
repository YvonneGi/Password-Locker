class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty contact list

    def __init__(self,username,password):
        self.username = username
        self.password = password  #end init cred
       

##### save method to save new object##### 
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
#####search for a user in stored users#####
    @classmethod
    def login_by_userpass(cls, username, password):
        '''
        Method that takes in a username/password and authenticates the user matching.
        Args:
            username_search: User name to authenticate.
            password_search: His password.
        Returns :
            Account of person that matches the username/password.
        '''

        for user in cls.user_list:
            if user.username == username and user.password == password:
                return user