# DjangoAPI for codecorgi.co

## Requirements

### Using Docker

Install docker and docker-compose and run the command

```
docker-compose up
```

This will start the containers and link them

### Launching locally:

Install postgres and run it.

Create a virtual environment using python3, like:

```
mkvirtualenv corgi -p /usr/local/bin/python3.6
```

Add the following env variables, with the correct values.

```
export DJANGO_SECRET_KEY=
export DJANGO_DEBUG=
export DB_POSTGRES_DATABASE_NAME=corgi_development
export DB_POSTGRES_USERNAME=
export DB_POSTGRES_PASSWORD=
export DB_POSTGRES_HOSTNAME=localhost
export DB_POSTGRES_PORT=5432

export API_SERVICES_URL=http://localhost:8000/services/api/
export FRONTEND_APP_URL=http://localhost:3000/
```
