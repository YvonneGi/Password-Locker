class Credentials:
    """
    Class that generates new instances of users
    """

    cred_list = []  #Empty user user_list

    def __init__(self, username, cred_app, cred_username, cred_password):
        """
        __init__ method that helps us define properties for our objects.
        """
        self.username = username
        self.cred_app = cred_app
        self.cred_username = cred_username
        self.cred_password = cred_password
    #end init cred