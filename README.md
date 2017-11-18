# Footballers


### Requirements

* Python 3.5
* `pip install -r requirements.txt`


## Running the project

```sh
django-admin startproject footballers
cd footballers/
python manage.py migrate
# ^ create tables, database
python manage.py createsuperuser  # OPTIONAL test test1234
# ^ optional
python load_initial_data.py
# ^ loads initial data
python manage.py runserver
# ^ runs the server
```


## Updating/Working

```sh
python manage.py makemigrations backend
python manage.py migrate
```
