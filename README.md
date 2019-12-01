# CSTeam70-AtlantaMovieDatabase


yeet


To Create SQL users run these commands:

mysql> CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

mysql> GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';

Running the Web App
---

1. If you don't already have them, install Python 3 and pip.
2. Clone this repository to your computer. 
4. Create a virtual environment to contain this project.  The way you do this will vary depending on your operating system:
   
   a. Windows: Run `py -3 -m venv venv`
   
   b. Mac: Run `python3 -m venv venv`
5. Activate the virtual environment.  Run the appropriate command for your OS:
   
   a. Windows: Run `venv\Scripts\activate`
   
   b. Mac: Run `. venv/bin/activate`
6. Look for a `(venv)` at the beginning of each new line in your terminal.  This means you're
in your virtual environment.
7. Run `pip install -r requirements.txt` to install the dependencies.
8. Copy the `.env.example` file to `.env` and add the required values by following the directions
in the files.
9. Run `chema.sql` and `data.sql` to setup and add starter data to the database.
10. Start the webserver by running `flask run` inside the virtual environment.
11. You can access the application at [127.0.0.1:5000](127.0.0.1:5000) or [localhost:5000](localhost:5000).
12. Sign in with the following credentials, or create your own account