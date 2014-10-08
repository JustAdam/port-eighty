What is port-eighty?
====================

Nginx working as a reverse proxy (as a Docker container) for Docker containers serving web content.  Nginx's configuration file is generated each time a relevant container is stopped or started.  This allows services to be upgraded, maintained etc. without any downtime.

Quick start
===========

* Install [fig](http://fig.sh)
* You'll probably want to edit the hugo section in fig.yml
* `$ fig up -d`

Manual startup
==============

Build the following containers (follow each link for instructions):

* [docker-gen](docker-gen)
* [nginx-rp](nginx-rp)
* [hugo](hugo)

### Create a volume-only container

`$ docker run -d --name rp-data -v $(pwd)/templates:/etc/docker-gen/ -v $(pwd)/sites-enabled/:/etc/nginx/sites-enabled/:rw justadam/docker-gen:0.3.4 echo "Volume container"`

### Start docker-gen

`$ docker run -d --name docker-gen -v /var/run/docker.sock:/docker.sock -e DOCKER_HOST=unix:///docker.sock --volumes-from rp-data justadam/docker-gen:0.3.4`

### Start nginx 

`$ docker run -d -p 80:80 --name nginx-rp --volumes-from rp-data justadam/nginx-rp`

This gives us a nginx with a reverse proxy configuration (this file can be found at [docker-gen/templates/nginx.conf](docker-gen/templates/nginx.conf).  The file will be updated by docker-gen each time a container stop or starts.

Now we need a container to serve some content; this could be anything (apache, nginx, your own webserver), but we will be using a static content site generator named hugo, which also comes with its own webserver.
Each container which is to sit behind the reverse proxy needs to set an environment variable called VHOST, which is the URL it will be serving content on.

### Start hugo

`$ docker run -d --name hugo -e VHOST=www.before.no -v $(pwd):/content justadam/hugo:0.12`