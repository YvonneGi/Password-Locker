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
        self.new_credential = Credentials(
            "YvonneGi", "Twitter", "Gi", "giii")  # create user object
        # end of setUp

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.cred_list = []  # end of tearDown

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.username, "YvonneGi")
        self.assertEqual(self.new_credential.cred_app, "Twitter")
        self.assertEqual(self.new_credential.cred_username, "Gi")
        self.assertEqual(self.new_credential.cred_password,
                         "giii")  # end test_init

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credentials()  # save new credential
        self.assertEqual(len(Credentials.cred_list), 1)  # end test_save_cred


#  test cases for mupltiple saves here####


    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our cred_list
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials(
            "YvonneGi", "Twitter", "Gi", "giii")  # new credential
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.cred_list), 2)

######### test for delete method###
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials(
            "YvonneGi", "Twitter", "Gi", "giii")  # new credential
        test_credentials.save_credentials()

        self.new_credential.delete_credentials()  # Deleting a credential object
        self.assertEqual(len(Credentials.cred_list), 1)

#######search_credential method to search for the saved credentials####
   


if __name__ == '__main__':
    unittest.main()
