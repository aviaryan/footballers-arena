# Footballers


### Requirements

* Python 3.5
* `pip install -r requirements.txt`


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

# loads initial data
python load_initial_data.py

# runs the server
python manage.py runserver
```


## Updating/Working

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
