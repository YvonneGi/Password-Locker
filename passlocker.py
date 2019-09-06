#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

#######USER########
def create_user(username, password):
      '''
      Function to create a new user account
      '''
      new_user = User(username, password)
      return new_user

def save_user(user):
      '''
      Function to save user
      '''
      user.save_user()

def login_user(username, password):
      '''
      Function that finds a user by username/password and returns the user account
      '''
      return User.login_by_userpass(username, password)

#######CREDENTIALS####################
def create_credentials(username, cred_app, cred_username, cred_password):
      '''
      Function to create a new user credentials
      '''
      new_credential = Credentials(username, cred_app, cred_username, cred_password)
      return new_credential

def save_credentials(credential):
      '''
      Function to save credential
      '''
      credential.save_credential()
