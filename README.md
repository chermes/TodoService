# TodoService

## Introduction

### Features

### A Developers Perspective

What does it take to get the simple ToDo application into a productive state?
Besides its usefulness, this is a also a journey how to do that.

## Installation

### Used Parts (Reference)

* Python
  * fastapi
* MongoDB
* Vue.js
  * axios
  * Bulma CSS (buefy)
  * Font Awesome Icons
* Docker
  * docker-compose

### Tested Operating Systems

* Ubuntu
* Rasperry Pi 4 (Ubuntu Server) with installed Mongo DB instance.

### Requirements

* docker
* docker-compose

### Using Dockerhub

### Build your own containers

Development environment:
`sh build_dev.sh`
This creates images with tag `:development`.

Staging environment:
`sh build_stag.sh`
This creates images with tag `:staging`.

Production environment:
`sh build_prod.sh`
This creates images with tag `:latest`.

## Development Rules

* Development environment: Implement new changes / features to branch "develop".
* Staging environment: pull-request from branch "develop" to "staging".
* Production environment: pull-request from branch "staging" to "main".

Bug fixes can be applied on any environment, depending on the severity.

## Running the ToDo Service

### Deployment Diagram

![Deployment Diagram](./images/deployment_diagram.png)

### Deployment: Production

`docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d`

OR (shorthand)

`sh run_prod.sh`

* WebUI: [http://localhost:8080](http://localhost:8080)
* API: [http://localhost:9080](http://localhost:9080/docs)

### Deployment: Staging

`docker-compose -f docker-compose.yml -f docker-compose.stag.yml up -d`

OR (shorthand)

`sh run_stag.sh`

* WebUI: [http://localhost:8081](http://localhost:8081)
* API: [http://localhost:9081](http://localhost:9081/docs)

### Deployment: Development

`docker-compose -f docker-compose.yml -f docker-compose.dev.yml up`

OR (shorthand)

`sh run_dev.sh`

* WebUI: [http://localhost:8082](http://localhost:8082)
* API: [http://localhost:9082](http://localhost:9082/docs)

## ToDo (hah!)

* Implement UI and backend functionality
  * edit / modify item
  * colorize items based on priority
  * add search input
  * condense the "done" list (more compact cards...)
  * show number of items per user (stats)
* sort items by
  * backlog: prio (descending) + change date (ascending)
  * in progress: change date (ascending)
  * done: change date (descending)
* add api module versioning
* create and add ToDo logo
* create and add ToDo favicon
* support different languages (how does the babel stuff work?)
* migrate this ToDo list to the development environment :)
* How to do tests within Vue.js?
* How to do (automatic) MongoDB schema migration?
* Fill README.md with description and screenshots
* Once a minimal functionality is established, create a development branch and
  protect the "main" from direct pushes
* add icons (e.g. from Font Awesome)
* add "about" dialog
