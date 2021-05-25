## Necessary libraries

python 3.7.5
channels==3.0.1
channels-redis==2.4.2
Django==3.1.4
mysqlclient==2.0.3

## Installation

Database files are in /database

Configure those variables in ```settings.py```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '', # Your DB name
        'USER': '', # Your mysql local username
        'PASSWORD': '', # Your mysql local password
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET FOREIGN_KEY_CHECKS = 0;',
        }
    }
}

EMAIL_HOST_USER = '' # Your preferred email address
EMAIL_HOST_PASSWORD = '' # Password
```

## Run

```bash
env\scripts\activate
python manage.py runserver
```


```
