# nuxt-flask-todo-sample
This is a Todo application with Nuxt on the client side and Flask on the server side

> todo_application

## Build Setup

```zsh
# install dependencies
$ yarn install
$ yarn dev
$ pipenv install
$ pipenv run start

# create tables of sqlite
$ pipenv run init
$ pipenv run migrate
$ pipenv run upgrade

# build for production and launch server
$ yarn build
$ yar start

