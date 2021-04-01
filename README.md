# This is a boilerplate app to get a django docker app up and running quickly.

## This bare bones app just has:
1. Django Web Server
2. Postgres DB


### Start the project by

```
docker-compose -f docker-compose.local.yml run web django-admin startproject {name_of_project} app
```

### Add this to the settings file for the postgres db
```
import os

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE"),
        "NAME": os.environ.get("SQL_DATABASE"),
        "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "HOST": os.environ.get("SQL_HOST"),
        "PORT": os.environ.get("SQL_PORT"),
    }
}
```

### create apps
```
docker-compose -f docker-compose.local.yml run web django-admin startapp {name_of_app} app
```

### Prod settings
```
STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```
