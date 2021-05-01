from argparse import ArgumentParser
import sys
import pandas as pd
import re
from geopy.geocoders import Nominatim
import datetime

class User:
    """A class representing a dating app user profile
    Attributes:
        accepted_matches (set of usernames):
        rejected_matches (set of usernames)
        pending_matches (set of usernames): list of requested matches
        new_matches (boolean): indicates new matches upon login
        first_name (str): user's first name
        last_name (str): user's last name
        date_of_birth (Date): user's birthday
        age (int): user's age
        location (string): user's address
        gender (string): user's gender
        preference (set of strings): set of
        age_range (bottom int/top int)
        hobbies (list of strings)
    """
    
    def __init__(self, f_name, l_name, age, loc, gender, pref, hob):
        self.accepted_matches = set()
        self.rejected_matches = set()
        self.pending_matches = set()
        self.new_matches = False
        
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.gender = gender
        self.location = loc
        self.preference = pref
        #self.age_range = age_range
        self.hobbies = hob
        
    def __str__(self):
        # Formats hobbies to be printed line by line
        hob_list = ""
        for hob in hobbies:
            hob_list += "\t" + hob + "\n"
        
        print(f"\n\nName: {self.first_name + ' ' + self.last_name}\t" + 
              f"Age: {self.age}\t Gender: {self.gender}\t" + 
              f"Preference: {self.preference}\nLikes:\n{hob_list}\n\n")
        
    def get_name(self):
        """Gets user's first and last name
        
        Returns:
            str: user's first and last name
        """
        return f"{self.first_name} {self.last_name}"
        
    
    def distance_from_match(self, match):
        """Calculates the distance between this user and the match's location
        
        Args:
            match (User): potential match
            
        Returns:
            float: distance between this user and the match's location
        """
        
    
    #def age_match(self, match):
    #    """Checks if matched user fits within the preferred age_range
    #    
    #    Args:
    #        match (User): potential match
    #        
    #    Returns:
    #        boolean: True if match is within preferred age range, False if not
    #    """
    
    def confirm_match(self, match):
        """Prompts user to accept or reject a match
        
        Args:
            match (User): potential match
            
        Returns:
            str: on-screen prompt reflecting user's decision
            
        Side effects:
            moves match.user_ID from pending_matches to either accepted_matches 
            or rejected_matches, sets match's new_match attribute to 
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
        
class Database():
    """A class representing the collection of Users in the dating app
    Attributes:
        users (dict of tuples): username keys with tuple values of (password, 
            User)
    """
    def __init__(self, filepath=None):
        self.users = dict()
        if (filepath):
            with open(filepath, "r", encoding="utf-8") as csv:
                for line in csv:
                    u = line.strip().split(",")
                    
                    # Prevents duplicate usernames
                    if self.users.get(u[0]) == None:
                        hob = u[11].strip().split("; ")
                        loc = f"{u[5]}, {u[6]}, {u[7]} {u[8]}"
                        self.add_user(u[0],u[1],u[2],u[3],u[4],
                                      loc,u[9],u[10],hob)                   
        
    def add_user(self,u_name,pwd,f_name,l_name,age,loc,gender,pref,hob):
        """Processes demographic information to add user to database
        
        Args:
            u_name (str): account username
            pwd (str): account password
            f_name (str): user first name
            l_name (str): user last name
            age (int): user age
            loc (str): user location
            gender (str): user gender
            pref (str): user sexual preference
            hob (list of str): user hobbies
        
        Returns:
            User: newly created User object
        
        Side effects:
            creates new User object and adds to database
        """
        new_user = User(f_name,l_name,age,loc,gender,pref,hob)
        self.users[u_name] = (pwd, new_user)
        return new_user
              
        
def create_profile(db):
    """Prompts the user to fill in demographic information for a new account
    
    Args:
        db (Database): database that stores Users and login information
    
    Returns:
        User: newly created User object
    
    Side effects:
        prints profile creation prompts to console
    """
    print("\n---REGISTRATION---")
    print("\nCreate a new username and a password with 6 or more characters, " +
          "and at least one uppercase letter, number, "
          "and special character\n")
    
    while True:
        u_name = input("Username: ")
        if (db.users.get(u_name) != None):
            print("That username already exists!")
        else: break
    
    while True:
        pwd = input("Password: ")
        # ***NEEDS TO CHECK FOR PASSWORD REQUIREMENTS (maybe regex)***
        # else:
        break
    
    # PROMPT AND CHECK FOR PROPER DEMOGRAPHIC INFO, INCLUDING
    # INPUT FOR HOBBIES ONE AT A TIME
    
    # Name
    name_input = input("\nEnter your first and last name: ").split(" ")
    l_name = name_input.pop()
    f_name = " ".join(name_input)
    
    # Location/Address
    loc_expr = r"""(?xm)
                    (?P<address>\d{1,5}\s[^,\n]+) # address 1
                    ,\s(?P<city>[A-Za-z'\s]+) # city
                    ,\s(?P<state>[A-Z]{2}|[A-Za-z\s]+) # state
                    ,?\s(?P<zipcode>\d{5}) # zipcode
                    """
    print("\nEnter your address as the following fields separated by commas:\n\t" +
          "Street Address, City, State, Zipcode")
    while True:
        loc_input = re.search(loc_expr, input("\nAddress: "))
        if (loc_input):
            loc = (loc_input.group("address") + ", " + 
                    loc_input.group("city") + ", " + 
                    loc_input.group("state") +
                    loc_input.group("zipcode"))
            break
        else:
            print("Invalid address format")
            
    # Age/Date of Birth
    dob_expr = r"(?P<month>\d{2})/(?P<day>\d{2})/(?P<year>\d{4})"
    print("\nEnter your date of birth as MM/DD/YYYY")
    while True:
        dob_input = re.search(dob_expr, input("\nDate of Birth: "))
        if (dob_input):
            try: 
                dob = datetime.date(int(dob_input.group("year")), 
                                    int(dob_input.group("month")),
                                    int(dob_input.group("day")))
                break
            except ValueError:
                print("Invalid date")
        else:
            print("Invalid date")
    age = (datetime.date.today() - dob).days // 365
    
    # Gender - SOMEONE DO THIS
    gender = "M"
    
    # Preference - SOMEONE DO THIS
    pref = "F"
    
    # Hobbies - SOMEONE DO THIS
    hob = []
    
    return db.add_user(u_name,pwd,f_name,l_name,age,loc,gender,pref,hob)
    
    

def view_user(user):
    """View the demographic information of a single user
    
    Args:
        user (User): user profile to view
        
    Side efects:
        prints user's demographic attributes to console
    """
    print(user)
    
def search_keyword(keyword):
    """Searches user profiles for attributes containing keyword input
    
    Args:
        keyword (str): search term
        
    Returns:
        list of Users: users containing demographic information matching the
            keyword search
    """
    
def login(db):
    """Sets the current user
    Args:
        db ()
    
    Returns: 
        User: current user

    Side effects:
        prompts user input for username and password, changes global variable 
        for current user
    """
    username = ""
    password = ""
    print("\n---LOGIN---")
    while (db.users.get(username) == None):
        username = input("Enter username: ")
        if (db.users.get(username) == None):
            print("Username not found\n")
    user = db.users[username]        
    
    while (password != user[0]):
        password = input("Enter password: ")
        if (password != user[0]):
            print("Incorrect password")
    
    return user[-1]
    
    
def logout():
    """Clears the current user
    
    Side effects:
        clears the global variable for current user
    """
    
def main(user_list=None):
    """Runs the dating app program
    """
    db = Database(user_list)
    curr_user = None
    u_command = ""
    
    # Welcome screen - login, register, or exit
    print("\n\n\n---WELCOME TO THE INST326 CONSOLE DATING APP!---")
    while (u_command not in ['login','register','quit']):
        print("\n'login' - log in to your account" + 
                "\n'register' - create a new account" + 
                "\n'quit' - exits program")
        
        u_command = input().lower()
        if u_command == 'login':
            curr_user = login(db)
            break
        if u_command == 'register':
            curr_user = create_profile(db)
            break
        if u_command == 'quit':
            return
    
    u_command = ""
    print(f"\n\nWelcome, {curr_user.get_name()}!" + 
          ("You have new matches" if curr_user.new_matches else ""))
    print("\n'quit' - exits program")
    
    # Main Menu - search, logout, exit
    # THIS LOOP WILL INCLUDE ALL POSSIBLE USER COMMANDS FROM MAIN MENU
    while (u_command not in ['quit']):
        u_command = input().lower()
        if u_command == 'quit':
            return
    
def parse_args(arglist):
    """Parse command-line arguments.
    
    Expect one optional argument, a path to a comma-delimited file containing
    user profile information to establish existing data. 
   
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("-u", "--user_list", help="optional comma-delimited"
                        " file containing user profile information to establish"
                        " existing data")
    
    return parser.parse_args(arglist)  

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args.user_list)
     
     #test_app = User
     #test_app.distance_from_match("Match")
     #test_app.age_match(True)
     #test_app.confirm_match()
     #test_app.request_match()
     #test_app.view_user(user)
     #test_app.search_keyword(keyword)
     #test_app.login()
     #test_app.logout()"""

    
