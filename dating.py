class User:
    """A class representing a dating app user profile
    Attributes:
        user_ID (int): unique ID for back-end data handling
        accepted_matches (set of user IDs):
        rejected_matches (set of user IDs)
        pending_matches (set of user IDs): list of requested matches
        new_matches (boolean): indicates new matches upon login
        name (string): user's full name
        age (int): user's age
        location (string): user's address
        gender (string): user's gender
        preference (set of strings): set of
        age_range (bottom int/top int)
        hobbies (list of strings)
    """
    
    def distance_from_match(self, match):
        """Calculates the distance between this user and the match's location
        
        Args:
            match (User): potential match
            
        Returns:
            float: distance between this user and the match's location
        """
        
    
    def age_match(self, match):
        """Checks if matched user fits within the preferred age_range
        
        Args:
            match (User): potential match
            
        Returns:
            boolean: True if match is within preferred age range, False if not
        """
    
    def confirm_match(self, match):
        """Prompts user to accept or reject a match
        
        Args:
            match (User): potential match
            
        Returns:
            str: on-screen prompt reflecting user's decision
            
        Side effects:
            moves match.user_ID from pending_matches to either accepted_matches or 
            rejected_matches, sets match's new_match attribute to 
            True if accepted
        """
        
    def request_match(self, match):
        """Sends another user a request for a match
        
        Args:
            match (User): potential match
            
        Returns:
            str: on-screen prompt reflecting success of request
            
        Side effects:
            on-screen prompt reflecting success of request
        """
        
        
def view_user(user):
    """View the demographic information of a single user
    
    Args:
        user (User): user profile to view
        
    Side efects:
        prints user's demographic attributes to console
    """
    
def search_keyword(keyword):
    """Searches user profiles for attributes containing keyword input
    
    Args:
        keyword (str): search term
        
    Returns:
        list of Users: users containing demographic information matching the
            keyword search
    """
    
def login():
    """Sets the current user
    
    Returns: 
        User: current user

    Side effects:
        prompts user input for username and password, changes global variable 
        for current user
    """
    
def logout():
    """Clears the current user
    
    Side effects:
        clears the global variable for current user
        
if __name__ == '__main__':
     test_app = User
     test_app.distance_from_match("Match")
     test_app.age_match(True)
     test_app.confirm_match()
     test_app.request_match()
     test_app.view_user(user)
     test_app.search_keyword(keyword)
     test_app.login()
     test_app.logout()

    
