import unittest
from services import user



class TestUser(unittest.TestCase):

    def test_toggle_off(self):
        action= user.User(self)
        result = action.toggle_off()
        self.assertEqual(result, 'Thanks for analyzing! Come back again!')
        
    def test_toggle_off_2(self):
        action = user.User(self)
        result = action.toggle_off()
        self.assertNotEqual(result, '')

    def test_toggle_off_3(self):
        action = user.User(self)
        result = action.toggle_off()
        self.assertNotEqual(result, True or False)
    
    def test_toggle_off_4(self):
        action = user.User(self)
        result = action.toggle_off()
        self.assertNotEqual(result, 100) 

    def test_user_operation(self):
        action = user.User(self)
        result = action.user_operation()
        self.assertNotEqual(result, '')

   
    def test_user_operation2(self):
        action = user.User(self)
        result = action.user_operation()
        self.assertIsInstance(result, str) 


    
        



if __name__ == "__main__":
    unittest.main()