# Footballers


## Requirements

* Python 3.5
* `pip install -r requirements.txt`


## Features

Apart from the minimum features mentioned in the requirements, this application contains the following extra features.

1. Filter players by name
2. Player details opens on row click
3. Player detail shows all stats
4. Player details shows player's photo. It shows a placeholder where picture is missing.
5. Custom About page that links to my portfolio.


## Running the project


```sh
# clone or download the project and get the terminal to its folder

# install deps
pip install -r requirements.txt

# switch to the project
cd footballers/

# create tables, database
python manage.py migrate

# optional
python manage.py createsuperuser  # OPTIONAL test test1234

# load initial data
python load_initial_data.py

# run the server
python manage.py runserver
# go to localhost:8000 and enjoy!
```


## Updating / Saving DB Changes

```sh
python manage.py makemigrations backend
python manage.py migrate
```


## Running Tests

```sh
python manage.py test
# or
python manage.py test backend
python manage.py test frontend
```
