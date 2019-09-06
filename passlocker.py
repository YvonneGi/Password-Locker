#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

#######USER########
def create_user(username,password):
    '''
    Function to create a new user acoount
    '''
    new_user = User(username,password)
    return new_user