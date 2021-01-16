# GoodTunes
This is our second trimester project for AP CS Principles. GoodTunes is an aspiring social media platform where users can select songs from a database to create playlists, then share those playlists with others. These songs will be analyzed and be selected in the overview for a "AP CSP Wrapped."

### How to run Goodtunes
You can clone our code and run it on your own machine, or visit 76.88.112.116:3000 the public IP address to access the website. 

# Goals

### ✔️ Completed Goals ✔️
* Create a working flask skeleton including working backend, a base.html with a working navbar, and appropriate .css files
* Build an attractive homepage UI based on our storyboard on canva
* CSV database of 400 most popular songs in different generes with metadata that will help with analysis in the future.
* Create login and signup pages that take in user information and use it to interact with a SQL database
* Build a search page with an attractive UI that is able to search the website for songs

### 📝 Future Goals 📝
* Auto-generated working user dashboard that are created via the SQL database
* "Edit my user" button that leads to a page that edits user information
* Allow users to view and "follow" other users, and have this displayed on the user dashboard
* APCSP Wrapped that analyzes data after multiple users have created accounts

# Big Ticket Items
Note: this information can also be found on our [scrum board](https://github.com/sarahwxie/GoodTunes/projects/1)

### Homepage, Navbar, and styles
Our homepage code can be found [here](templates/home.html), our navbar code can be found [here](templates/nav.html), and our css code can be found [here](static/styles.css).

You can evaluate this big ticket item by visiting our website (see IP above, or clone our code) and clicking through our different pages. 

All four members of our group worked on this big ticket item together. Doing this required collaboration and creativity. 

### Login/Sign Up Pages and User Dashboard
The login and signup pages can be found [here](templates/login.html) and [here](templates/signup.html). The code that leads the user to a new page after signing in can be found in [main.py](main.py). Risa and Nivu worked on this.

Evaluate this big ticket item by 

### Search Page
The UI of the search page was done by Sarah and the page itself can be found [here](templates/search.html). Ida did the initial code that searched through the database of songs in response to user input, and Sarah added to it to create the display. The finished product that allows the user to find songs according to key words can be found in [main.py](main.py). 

Evaluate this big ticket item by searching for a song on our website. Note that we only have 400 songs currently, so you may not find what you are specifically looking for. Instead try a key word or an artist. Right now, it will only show you the first song that the loop finds, but we hope to have this fixed in the future. 

### SQLite Database
Sarah did this idk

# 1/15 Individual + Scrum Master Grading
Ida Mobini: I created the songs database and passed it into main.py so the search function would work. Find my work in [main.py](main.py) and [songs.py](songs.py). Indivual grading 4/5 

Sarah Xie: Scrum Master grading 14/15 

Nivu Rethnakar:
  I worked on and finished on the Login/Sign Up Page relink and created the Profile page that they're now linking to. I also started working on the HTML and CS for the Profile page. Scrum Master grading 15/15 Indivdual grading 

Risa Iwazaki: I worked on starting up the login profile page and the GET POST aspect of the sign up page. I also deployed our web server onto my raspberry pi so we could access the website using the public IP address. Scrum Master grading 15/15 Individual grading 


# Creators
Ida Mobini, Sarah Xie, Risa Iwazaki, Nivedita Rethnakar 
