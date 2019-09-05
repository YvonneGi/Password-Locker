class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty contact list

    def __init__(self,username,password):

      # docstring removed for simplicity

        self.username = username
        self.password = password