#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

#######USER########
def create_user(username, password):
      '''
      Function to create a new user account
      '''
      new_user = User(username, password)
      return new_user#end create_user

def save_user(user):
      '''
      Function to save user
      '''
      user.save_user()#end save_user

def login_user(username, password):
      '''
      Function that finds a user by username/password and returns the user account
      '''
      return User.login_by_userpass(username, password)#end login

#######CREDENTIALS####################
def create_credentials(username, cred_app, cred_username, cred_password):
      '''
      Function to create a new user credentials
      '''
      new_credential = Credentials(username, cred_app, cred_username, cred_password)
      return new_credential#end create_cred

def save_credentials(credential):
      '''
      Function to save credential
      '''
      credential.save_credential()#end save_cred

def delete_crededential(credential):
      '''
      Function to delete a credential
      '''
      credential.delete_credential()#end delete cred

def find_credential(username):
    '''
    Function that finds a credential by username and returns the user credential
    '''
    return Credentials.find_by_username(username)#end find cred

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()#end display cred

##########GENERIC################################

