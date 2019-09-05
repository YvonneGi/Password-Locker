class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty contact list

    def __init__(self,username,password):
        self.username = username
        self.password = password
         #end init cred