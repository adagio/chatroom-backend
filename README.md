Chatroom
===================================

This repository contains the API codebase of the Chatroom developed with Django Channels and React. This is based on part of a post, that you can read [here](https://revs.runtime-revolution.com/a-simple-real-time-chat-with-django-channels-and-react-b73edc3a79f2). You can check there how to get up and running.

## ✨ Language and Framework

- Python 3.7.3
- Django 2.0

## Redis

Use docker-compose.yml. Then load with _docker up_

https://gist.github.com/adagio/56fbc68bafa7bbc06444a8f46ec08f35

## Postgres

Use docker-compose.yml. Then load with _docker up_

https://gist.github.com/adagio/76a2c54bddb229029df5bd3eb8feea92

## API Application

# Activate your venv

```pip install -r requirements.txt```


# Could be necessary to run makemigrations

```python manage.py makemigrations```

# Update the database

```python manage.py migrate```

# Run the application

```python manage.py runserver 0:8000```
