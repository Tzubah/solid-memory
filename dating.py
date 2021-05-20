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
        username (str): account username
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
    
    def __init__(self,u_name, pwd, f_name, l_name, age, loc, gender, pref, hob):
        self.accepted_matches = set()
        self.rejected_matches = set()
        self.pending_matches = set()
        self.new_matches = False
        
        self.username = u_name
        self.password = pwd
        self.first_name = f_name.title()
        self.last_name = l_name.title()
        self.age = age
        self.gender = gender.upper()
        self.location = loc
        self.preference = pref.upper()
        self.hobbies = [h.capitalize() for h in hob]
        
        
    def __str__(self):
        # Formats hobbies to be printed line by line
        hob_list = ", ".join(self.hobbies)
        #for hob in self.hobbies:
        #    hob_list += "\t" + hob + "\n"
        
        return (f"\n\n{self.username}\n" + 
                f"Name: {self.get_name()}\t" + 
                f"Age: {self.age}\t Gender: {self.gender}\t" + 
                f"Preference: {self.preference}\nLikes: {hob_list}\n\n")
        
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
        if match is True:
            match = new_match
        else:
            match = (input("Accept or Reject: "))
        if match.username = self.accepted_matches: 
            print("Match accepted")
        else:
            print("Match rejected")
        
    def request_match(self, match):
        """Sends another user a request for a match
        
        Args:
            match (User): potential match
            
        Returns:
            str: on-screen prompt reflecting success of request
            
        Side effects:
            on-screen prompt reflecting success of request
        """
        if self.username = match.pending_matches:
            request_match
        else:
            print("Request Sent")
            
class Database():
    """A class representing the collection of Users in the dating app
    Attributes:
        users (dict of Users): username keys with User values
        df (DataFrame): stores and saves user profile information for future use
    """
    def __init__(self, filepath=None):
        self.users = dict()
        self.df = pd.DataFrame({'Username':[],
                                'Password': [],
                                'First_Name': [],
                                'Last_Name': [],
                                'Age': [],
                                'Street_Address': [],
                                'City': [],
                                'State': [],
                                'Zipcode': [],
                                'Gender': [],
                                'Preference': [],
                                'Hobbies': []}
                               )#.set_index('Username', drop=False)
        #print(self.df)
        if (filepath):
            #existing = pd.read_csv(filepath, sep=",")\
            #    .set_index('Username', drop=True)
            existing = pd.read_csv(filepath, sep=",")\
                .drop_duplicates('Username')
            #print(existing)
            #existing.drop_duplicates('Username', inplace=True)
            self.df = pd.concat([self.df, existing])
            
        for index, u in self.df.iterrows():
            if self.users.get(u.Username) == None:
                hob = u.Hobbies.strip().split("; ")
                loc = (f"{u.Street_Address.title()}, {u.City.title()}" + 
                       f", {u.State.upper()}, {u.Zipcode}")
                self.add_user(u.Username.strip(), u.Password, 
                              u.First_Name.strip().title(), 
                              u.Last_Name.strip().title(),
                              int(u.Age), loc, u.Gender.strip().upper(), 
                              u.Preference.strip().upper(), hob)
            
        """ if (filepath):
            with open(filepath, "r", encoding="utf-8") as csv:
                for line in csv:
                    u = line.strip().split(",")
                    
                    # Prevents duplicate usernames
                    if self.users.get(u[0]) == None:
                        hob = u[11].strip().split("; ")
                        loc = f"{u[5]}, {u[6]}, {u[7]} {u[8]}"
                        self.add_user(u[0],u[1],u[2],u[3],u[4],
                                      loc,u[9],u[10],hob) """                   
        
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
        new_user = User(u_name,pwd,f_name,l_name,age,loc,gender,pref,hob)
        self.users[u_name] = new_user
        return new_user
    
    def update_df(self, username):
        """Updates DataFrame with new user information
        
        Args:
            username (str): username of User to update in Dataframe
            
        Side effects:
            see above
        """
        user = self.users[username]
        loc = user.location.split(", ")
        hobbies = "; ".join(user.hobbies)
        
        new_row = pd.Series(
            {'Username': username,
                'Password': user.password,
                'First_Name': user.first_name,
                'Last_Name': user.last_name,
                'Age': user.age,
                'Street_Address': loc[0],
                'City': loc[1],
                'State': loc[2],
                'Zipcode': loc[3],
                'Gender': user.gender,
                'Preference': user.preference,
                'Hobbies': hobbies}
        )
        if username not in self.df['Username'].values:
            self.df = self.df.append(new_row, ignore_index=True)
        else:
            self.df[self.df["Username"] == username] = new_row
            """self.df[self.df["Username"] == username] = pd.Series(
                {'Username': username,
                'Password': user.password,
                'First_Name': user.first_name,
                'Last_Name': user.last_name,
                'Age': user.age,
                'Street_Address': loc[0],
                'City': loc[1],
                'State': loc[2],
                'Zipcode': loc[3],
                'Gender': user.gender,
                'Preference': user.preference,
                'Hobbies': hobbies}
        )"""
        """u_df = pd.DataFrame({'Username': [username],
                'Password': user.password,
                'First_Name': user.first_name,
                'Last_Name': user.last_name,
                'Age': user.age,
                'Street_Address': loc[0],
                'City': loc[1],
                'State': loc[2],
                'Zipcode': loc[3],
                'Gender': user.gender,
                'Preference': user.preference,
                'Hobbies': hobbies})
        self.df = pd.concat([self.df, u_df])"""
              
        
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
    print("Enter '!back' at any time to return to the menu")
    print("\nCreate a new username and a password with 6 or more characters, " +
          "and at least one uppercase letter, number, "
          "and special character\n")
    
    u_name_expr = r"""^\S+$"""
    while True:
        i = input("Username: ")
        if i == "!back":
            return None
        
        u_name_input = re.search(u_name_expr, i)
        if (u_name_input):
            u_name = u_name_input[0]
            if (db.users.get(u_name) != None):
                print("That username already exists!")
            else: break
        else: print("Invalid username")
    
    while True:
        pwd = input("Password: ")
        if pwd == "!back":
            return None
        # ***NEEDS TO CHECK FOR PASSWORD REQUIREMENTS (maybe regex)***
        # else:
        break
    
    # PROMPT AND CHECK FOR PROPER DEMOGRAPHIC INFO, INCLUDING
    # INPUT FOR HOBBIES ONE AT A TIME
    
    # Name
    name_input = input("\nEnter your first and last name: ").split(" ")
    if name_input[-1].strip() == "!back":
        return None
    l_name = name_input.pop().title()
    f_name = " ".join(name_input).title()
    
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
        i = input("\nAddress: ")
        if i == "!back":
            return None
        
        loc_input = re.search(loc_expr, i)
        if (loc_input):
            loc = (loc_input.group("address").title() + ", " + 
                    loc_input.group("city").title() + ", " + 
                    loc_input.group("state").upper() + ", " +
                    loc_input.group("zipcode"))
            break
        else:
            print("Invalid address format")
            
    # Age/Date of Birth
    dob_expr = r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})"
    print("\nEnter your date of birth as MM/DD/YYYY")
    while True:
        i = input("\nDate of Birth: ")
        if i == "!back":
            return None
        
        dob_input = re.search(dob_expr, i)
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
    # gender = "M"
    while True:
        gender=input("\nEnter your gender (M/F): ").strip().upper()
        if gender == "!BACK":
            return None
        if gender=='M' or gender=='F':
            break
        print("Invalid input. Choose between M/F")
    
    # Preference - SOMEONE DO THIS
    #pref = "F"
    while 1:
        pref=input("\nEnter your partner preference (M/F/B):").strip().upper()
        if pref == "!BACK":
            return None
        if pref=='M' or pref=='F' or pref=='B':
            break
        print("Invalid input. Choose between M/F/B")
    
    # Hobbies - SOMEONE DO THIS
    hob_input = input("\nEnter some of your hobbies, separated by semi-colons (e.g. Bowling; Guitar; etc...)\n")
    hob = hob_input.strip().split("; ")
    if hob[-1] == "!back":
        return None
    
    new_user = db.add_user(u_name,pwd,f_name,l_name,age,loc,gender,pref,hob)
    db.update_df(u_name)
    print("\nYour account has been created!\n")
    return new_user
    
    

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
    print("\nEnter your login credentials, or '!back' to return to the menu")
    while (db.users.get(username) == None):
        username = input("Enter username: ")
        if username == "!back":
            return None
        if (db.users.get(username) == None):
            print("Username not found\n")
    user = db.users[username]        
    
    while (password != user.password):
        password = input("Enter password: ")
        if password == "!back":
            return None
        if (password != user.password):
            print("Incorrect password")
    
    return user
    
    
#def logout():
#    """Clears the current user
#    
#    Side effects:
#        clears the global variable for current user
#    """
    
def view_profile(db, user):
    """Screen for user to view, edit, and delete their profile
    """
    #while True:
    #    u_command = ""

def view_pending(user):
    """Goes through user's pending matches to accept/reject
    
    Side effects:
        prints prompts and user profiles to console
    """
    
def view_matches(user):
    """Goes through user's accepted matches
    """
    
def browse_users(user):
    """Goes through non-matched users who match user's preference, sorted by
        distance
    """

def main(user_list=None):
    """Runs the dating app program
    """
    db = Database(user_list)
    curr_user = None
    
    # Welcome screen - login, register, or exit
    while True:
        u_command = ""
        while curr_user == None:
            print("\n\n\n---WELCOME TO THE INST326 CONSOLE DATING APP!---")
            print("\n'login' - log in to your account" + 
                        "\n'register' - create a new account" + 
                        "\n'quit' - exits program")
            
            while (u_command not in ['login','register','quit'] 
                   or curr_user == None):

                
                u_command = input().strip().lower()
                if u_command == 'login':
                    curr_user = login(db)
                    break
                if u_command == 'register':
                    curr_user = create_profile(db)
                    break
                if u_command == 'quit':
                    db.df.to_csv('updated_users.csv', index=False)
                    return
            
            u_command = ""
            if curr_user:
                print(f"\n\nWelcome, {curr_user.get_name()}!" + 
                    ("You have new matches" if curr_user.new_matches else ""))
        
        # Main Menu - search, logout, exit
        print("\n---MAIN MENU---" +
              "\n'profile' - view your profile" +
              "\n'matches' - view your accepted matches" +
              "\n'browse' - browse users" +
              "\n'logout' - log out of your account" +
              "\n'quit' - exits program")
        
        # THIS LOOP WILL INCLUDE ALL POSSIBLE USER COMMANDS FROM MAIN MENU
        while (u_command not in ['profile', 'logout', 'quit']):
            u_command = input().strip().lower()
            if u_command == 'profile':
                view_user(curr_user)
                continue
            if u_command == 'logout':
                curr_user = None
                db.df.to_csv('updated_users.csv', index=False)
                print('\nYou have been logged out successfully. Thank you!\n\n'
                      + '------------------------------------------')
                break
            if u_command == 'quit':
                db.df.to_csv('updated_users.csv', index=False)
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

    
