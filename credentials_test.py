import unittest  # Importing the unittest module
from credentials import Credentials  # Importing the User class


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("YvonneGi", "Twitter", "Gi", "giii")  # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.username, "YvonneGi")
        self.assertEqual(self.new_credential.cred_app, "Twitter")
        self.assertEqual(self.new_credential.cred_username, "Gi")
        self.assertEqual(self.new_credential.cred_password, "giii")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credentials() # saving the new contact
        self.assertEqual(len(Credentials.cred_list),1)


if __name__ == '__main__':
    unittest.main()
