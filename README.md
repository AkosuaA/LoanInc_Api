# LoanInc Api

API for accessing agent & customer information at Loan Inc

## What you need

- [Python](https://www.python.org/): This project uses `Python v 3.6.2`

- [Postgres](https://www.postgresql.org/): You can grab the latest version of postgres by downloading it directly on the website.

NB: Be sure to have these installed before continuing with the setup


## Project Setup

Clone this repository on your computer with the following command: `git clone https://github.com/d-attuah/LoanInc_Api.git`

### Direct Setup

1. Setup your virtual environment
1. Within your virtual environment, run `pip install -r requirements.txt` to grab all the dependencies and setup the project.
2. Create a database called `loan_inc` to use as your local database.
3. In the config.py file modify SQLALCHEMY_DATABASE_URI to match your local postgres configuration values.
4. Run `flask db upgrade` to initialize your database.
5. Run `flask db_seed` to insert data into your database
6. Run `flask run` to start the application on [http://localhost:5000](http://localhost:5000).
