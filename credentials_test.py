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


#### test cases for mupltiple saves here####
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our cred_list
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials(
            "YvonneGi", "Twitter", "Gi", "giii")  
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.cred_list), 2)# end of save multiple method

######### test for delete method###
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials(
            "YvonneGi", "Twitter", "Gi", "giii")  
        test_credentials.save_credentials()

        self.new_credential.delete_credentials()  # Deleting a credential object
        self.assertEqual(len(Credentials.cred_list), 1)

###############search method to search for stored credentials####
    def test_find_credential_by_username(self):
        '''
        test to check if we can find a credential by username and display information
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("YvonneGi","Twitter","Gi","giii") 
        test_credential.save_credentials()

        found_credential = Credentials.find_by_username("YvonneGi")

        self.assertEqual(found_credential.cred_app,test_credential.cred_app)
        self.assertEqual(found_credential.cred_username,test_credential.cred_username)
        self.assertEqual(found_credential.cred_password,test_credential.cred_password)#end of find method


#######display_credential method to display all credentials####
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.cred_list)###display credentials


if __name__ == '__main__':
    unittest.main()
