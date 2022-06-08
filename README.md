# **Paavo-Secure**

## **Video Demo:** <URL HERE>

## **General description:**

This web app was made as a part of the final project of the CS50x,
a MOOC by Harvard.

The app was developed using Python with Flask on the backend and HTML, JS and CSS on
the frontend. JQuery was also used on several JS functions.More in detail about 
different Python modules and database implementations further down.

The main functionalities of the app are the account system, password generating,
password cracking and password saving. As the index page suggests in the form of a 
disclaimer, the emphasis was on the functionalities over the UI/UX. Other disclaimer 
would be that this project was a solo effort so expectations may not be set too high.

### **Blueprints**

There are two blueprints to make the app a bit more structured.

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
All templates use Jinja for extending and also for passing information from the backend to
the frontend. 