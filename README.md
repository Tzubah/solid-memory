# <a id='header'></a> INST326-Dating Application

*New Repository for INST326 Group 4*

**Members:** Josue Hernandez, Victor Ifeacho, Jian Soriano, Thomas Zubah

---
## <a id='readme'></a>I. README

* Title of your project
    - Dating Application
* Description of your project
    - This is a simple dating application to be run in your computer terminal using local files.
       
   
* Link to User Manual
   - [II. Files](#files)
      - Describes the files contained in this repository 
   
* Link to Developer Manual
   - [III. User Manual](#usermanual)
      - Explains how to use the application

---
## <a id='files'></a>II. Files

### `dating.py`
   - This is the main Python file used to run the dating application.
### `users.csv`
   - This file is a baseline database of profile information for users of the
   dating app. Any other csv can be used if it is formatted the same.
   #### Columns:
      - "Username"
      - "Password"
      - "First_Name"
      - "Last_Name"
      - "Age"
      - "Street_Address"
      - "City"
      - "State"
      - "Zipcode"
      - "Gender"
      - "Preferences"
      - "Hobbies
### `updated_users.csv`
    - This file is an updated version of the `users.csv` file that contains any 
    changes made during a session. The file is automatically created/updated 
    after successfully logging out or exiting the program.
---
## <a id='usermanual'></a>III. User Manual

### How to run the program from the command line
   - `python dating.py` to run the program from scratch without an existing 
   userbase
   - `python dating.py -u users.csv` to run the program using our baseline 
   database of users
   - `python dating.py -u ___.csv` to run the program using any other csv that 
   follows the format described in the [Files](#files) section above

### How to use the program
   - 

### How to run any tests you have written for your software
   - 
   
### A clear set of expectations around known bugs and a road-map for future development.