

class User:

    def __init__(self,name):
        self.name = name

    def toggle_off(self):
        return ('Thanks for analyzing! Come back again!')

    def user_operation(self):
        user_action = input('Would you like to scrape a website (y/n)?: ').lower()

        while user_action != 'y' and user_action != 'n':
            user_action = input('''
            Wrong! input please enter y or n

            Would you like to scrape a website (y/n)?: 
            ''').lower()
            user_action = user_action

        if user_action == 'y':
            website = input('Enter a website to analyze: ')
            return website
            
        else:
            return False




