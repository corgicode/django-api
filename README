# codecorgi

Checkout our progress on [![Waffle.io](https://badge.waffle.io/corgicode/django-api.svg?columns=all)](https://waffle.io/corgicode/django-api)

[![Build Status](https://circleci.com/gh/corgicode/django-api.svg?style=shield)](https://circleci.com/gh/corgicode/django-api)

 Codecorgi is a visual portfolio for front-end developers to showcase their
 code and experience. Codecorgi's vision is to help employ the workforce by
 providing developers continuous training and project experience. Our company
 believes that junior developers have a difficulty landing their first
 programming career.

# Contributing

Todo :(

Follow our [code of conduct on github](https://github.com/corgicode/frontend-react/blob/dev/CODE_OF_CONDUCT.md).

## Installing

We're using docker and docker-compose to start the application.

Install Docker.

```bash
http://www.docker.com/products/docker#/mac
```

I used this tutorial to help me get the hang of things. I recommend it for getting started.

```bash
https://prakhar.me/docker-curriculum/
```

Grab the repo:

```bash
git clone git@github.com:corgicode/django-api.git
```

Then start the containers:

```bash
docker-compose up
```

It will take a long time running the first time while downloading all the
dependencies, but the future times it will be super quick.

Run `docker-compose down` when you're not working to save resources in your machine,
and `docker-compose restart` if you need to restart the application.

Now you can visit your local version going to `http://localhost:9000`.

The watcher should restart the application everytime a file changes in the backend,
but if you notice that is not happening, run the restart command manually.

If the application can't be accessed an error might have occurred, to look at the logs
run the command `docker-compose logs -f --tail=10 web`.

## Env variables

The four following variables are needed to run the application.

```
GITHUB_CLIENT_ID
GITHUB_CLIENT_SECRET
GITHUB_CALLBACK_URL
GITHUB_APP_NAME
ADMIN_API_KEY
BASE_URL
MAILCHIMP_LIST_ID
MAILCHIMP_API_KEY
```

The github ones are pretty self explanatory, register an application [here](https://github.com/settings/applications/new),
is used for authentication and to get some information about the users.

The Admin api key is a key that can be included in the request headers to allow for admin access, temp solution.

Base url is mostly used to redirect to routes in the front end.

## Migrations (Seed data)

Make an admin request to `docker-compose run web python3 manage.py migrate` to run the migrations.

## Developing


### PyLint

Linting will help identify:

- formatting discrepancy
- non-adherence to coding standards and conventions
- pinpointing possible logical errors in your program

Running a Lint program over your source code, helps to ensure that source code
is legible, readable, less polluted and easy to maintain.

### Git Flow

Git flow is a branching model and a plugin for git that
helps you manage your branches easier, that way we don't
overstep in each other codes, all the contributions should go through pull requests,
so git flow will help you manage your workflow easier.

First you need to install and activate git flow, to install on mac use
[homebrew](https://brew.sh/):

```bash
brew install git-flow
```

Then run `git flow init` on the root of the project to set up your git flow configuration.

To start a new feature, like to close a ticket or add some code, run the command, where
NAME is a short description of the issue or the ticket number from gitlab. For example
`git flow feature start adding-users`.

Commit often, and push to your branch, and when you're ready create a merge request on gitlab.
An admin will approve the request and merge your code into develop, and create new releases.

For now that's all you need to know, you can find more information about git flow
[here](http://nvie.com/posts/a-successful-git-branching-model/).

Detailed installation instructions [here](https://github.com/nvie/gitflow/wiki/Installation).

## Dependencies

The following are tools, packages or technologies used.

### Django

Django makes it easier to build better Web apps more quickly and with less code.

[Homepage](https://www.djangoproject.com/).

I recommend following a short django tutorial before jumping into the code,
to help you understand what requiring is, middleware, routes, etc.

This [one in their documentation](https://www.djangoproject.com/start/)
seems complete enough, but feel free to use whatever one you prefer.

### JSON Api

[JSON Api](http://jsonapi.org/) is an specification for building APIs in JSON.
By following shared conventions, you can increase productivity, take advantage of
generalized tooling, and focus on what matters: your application

### Postgres

### Redis

Redis is a fast, open source, in-memory key-value data structure store.

Writing to Redis is a lot faster than writing to Mongo or other data stores,
the data can be set with an expiration date and it doesn't offer the same reliability.
Making it perfect for caching data. Every time we run a long operation we can store
the result of that operation in the redis database, and the next time that same result
is needed we can fetch it from redis instead of running the operation again, that will
make the users happier and save resources on the server.

[What is redis](https://aws.amazon.com/elasticache/what-is-redis/).

[Try a demon of redis online](http://try.redis.io/).
