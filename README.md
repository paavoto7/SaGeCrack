# **SaGeCrack**

## **General description:**

This web app was made as a part of the final project of the CS50x,
a MOOC by Harvard.

The main functionalities of the app are the account system, password generating,
password cracking and password saving. As the index page suggests in the form of a 
disclaimer, the emphasis was on the functionalities over the UI/UX. Other disclaimer 
would be that this project was a solo effort so expectations shouldn't be set too high.

The app was developed using Python with Flask on the backend and HTML, JS and CSS on
the frontend. JQuery was also used on several JS functions. More in detail about 
different Python modules and database implementations further down.

Everything in this project is made by the owner of this repo and nothing has been copied from 
other projects. I can't deny using examples on the more harder things but even then nothing is 
copied neither directly nor indirectly.

### **Features**

##### **Password generator**

Password generator takes password length as user input and and it has a dropdown
menu of three character choices for the password to be created from. It is implemented
with Javascript to reduce the stress on the server side. The user can then copy the password
to their clipboard or save it. The save button redirects to the save page and automatically
fills the password input with it.

##### **Password cracker**

Password cracker takes as input the password and the type of the password.
User then presses crack-button and waits for the cracking to be made. It displays
the password then and the time took to crack it. Too long passwords aren't suggested
as there are no max-lenght or max-time restrictions set.

##### **Password saving**

Password saving has two functionalities, saving and searching. Saving takes a service,
username and password as input and stores them into a database called passwords. Searching
takes as input the service and displays all the user saved passwords and usernames under that 
service name. It may display multiple rows depending what the user has saved. Originally the 
search had a list that displayed only the service name and by clicking a result it would 
display the password and username or ask for more information. The interface was really bad
for the user so I decided to abandon it and make it simpler.


### **__init__.py**

This file is for the app creation and the registration of the blueprints.

### **Blueprints**

There are two [blueprints](https://flask.palletsprojects.com/en/2.1.x/tutorial/views/) to make the app a bit more structured. 

#### **pages.py**

Pages.py contains all the routes except the ones that handle credidentials. It is called 
pages simply because its main job is to render templates. Explaining all of them would 
be a waste of time as most of them are self-explanatory and I've added several comments 
on top of that. 

#### **auth.py**

Auth.py is the other blueprint file that contains all the routes that handle with 
credidentials. Its three functions are also very self-explanatory with comments. The 
after request route is essential for the security of the user as it disables caching in 
the browser so pressing back button don't show the page where you were logged in.

#### **Account system and database.py**

The app has the ability for a user to register an account, log in a session and log 
out of the session. These are made possible by Flask, Flask-Session, SQLite and 
SQLAlchemy.  
I created a seperate file from other python files that containsall the database functions.
Be it negligence or time management, but the initial database creating code is
missing so that is left to the manager of the app. The database implementation was 
done with SQLite and the data is stored using SQLAlchemy. Using SQLAlchemy was 
probably useless as no ORM functionalities are used. The functions respectively handle 
the storing and extracting of data.  
Here is an example of a function:
```
def login(name, passw):
    with engine.connect() as conn:
        result = conn.execute("SELECT * FROM users WHERE
        username=?", (name,)).fetchone()
        if not result:
            return False
        if len(result) != 3 or not
        check_password_hash(result["password"], passw):
            return False
        else:
            return result["id"]
```

#### **functions.py**

The functions file is like the database file with the difference being that is has 
nothing to do with database. It is only a so called helper file as it only contains 
functions for others to call. It contains the cracker function and the login required.
The function typpe, which is stupidly named, is only a helper for the cracker. 
The generator is commented because it originally was a backend function. It is much 
simpler in Python but I decided to reduce the unnecessary load on the server.
The cracker is still in the backend mainly because I couldn't find a neat way to do
it with JS. I also wanted to play around with jQuery and AJAX.

### **Templates**

Going too much in detail with the templates would be a waste of time also as their names 
tell what they are. Layout.html is the layout file what every other template extends. It 
has all the stuff that stays the same throughout the templates.  
All templates use Jinja for extending and also for displaying information gotten from the backend.

### **Static files**

Static files include all the javascript files and the styles.css file. Javascript files are named 
such way that its easy to understand what they do. Some of them use jQuery which comes from 
Googles CDN so that the user would already have it cached in their browsers memory. Choosing to
use jQuery was made in order to ease up on the redundancy of the DOM manipulation.

#### **styles.css**

Almost all of the styling is in the styles.css file. The file isn't very well organised and has 
some redundancy. The reason for those is that this project is essentially a learning experience. 
Even if I'd never hardcode them again I still believe it's good to understand whats going under
the hood so to speak. All templates were developed to be responsive using media queries.

### **.gitignore**

Gitignore contains the files and directories created by Flask and the database where everything
is stored.