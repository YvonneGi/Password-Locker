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
        self.new_credentials = Credentials(
            "YvonneGi", "Twitter", "Gi", "giii")  # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.username, "YvonneGi")
        self.assertEqual(self.new_credentials.cred_app, "Twitter")
        self.assertEqual(self.new_credentials.cred_username, "Gi")
        self.assertEqual(self.new_credentials.cred_password, "giii")


if __name__ == '__main__':
    unittest.main()
