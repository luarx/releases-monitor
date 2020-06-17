# releases-monitor
Releases monitor allows you to **monitor version updates** of each Github project in which you are interested.

## Docker images
https://hub.docker.com/r/raulio/releases-monitor/

## Index of contents

- [Installation](#installation)
- [Sync releases version](#sync-releases-version)
- [Django settings](#django-settings)

Installation
------------

For the next steps, a Linux/MacOs operating system is required. Windows is currently not tested/supported.

### Install Docker and Docker Compose
* First, install docker: https://docs.docker.com/engine/installation/.
* Then, install docker compose: https://docs.docker.com/compose/install/
* Clone the repository and change your working directory:

```
git clone https://github.com/luarx/releases-monitor.git
cd releases-monitor
```

### Build containers
The application is made up of several container images that are linked together using docker-compose. Before running the application, build the images:

`docker-compose build --force-rm`

### Run application
Start the releses-monitor server simply by bringing up the set of containers:

`sudo docker-compose up`

You can access it on http://localhost:8000 and the admin is on http://localhost:8000/admin

You will need to have the following ports open on your machine for this to work:
- 8000: NGINX serving a Django administrative app

### Create a Django user
Enter the Web container's command line with the following command:

```
docker-compose exec web sh
```

Once inside, create a super user in order to access the monitor/admin interface.

```
python manage.py migrate
python manage.py createsuperuser
```

You may exit the web container shell with:

```
exit
```

Sync releases version
------------

Enter the Web container's command line with the following command:

```
docker-compose exec web sh
```

Once inside, sync releases version with this command:

```
python manage.py syncreleasesversion
```

You may exit the web container shell with:

```
exit
```

Notify available updates
------------

Enter the Web container's command line with the following command:

```
docker-compose exec web sh
```

Once inside, sync releases version with this command:

```
python manage.py notifyavailableupdates
```

You may exit the web container shell with:

```
exit
```

Django Settings
---------------

releses-monitor comes with a default settings file that you can edit directly or using ENVIRONMENT VARIABLES.

##### ALLOWED_HOSTS
Specify the list of allowed hosts to connect to releses-monitor:

`ALLOWED_HOSTS = ['127.0.0.1', 'localhost']`

##### DEBUG MODE
Specify debug mode:

`DEBUG = True`

##### SECRET KEY
Specify project secret key. You must do it!:

`SECRET_KEY = [SECRET_KEY]`
