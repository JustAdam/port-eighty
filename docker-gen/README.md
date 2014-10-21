docker-gen container
====================

Runs [docker-gen](https://github.com/jwilder/docker-gen) stand alone inside a container. 

## Build a docker-gen binary

* requires *Go*

```
$ go get -d github.com/jwilder/docker-gen
$ cd /path/to/src/github.com/jwilder/docker-gen
$ DGTAG=$(git describe --tags --abbrev=0 | sed 's/^v//' | sed 's/\+.*$$//')
$ go build -ldflags "-s -X main.Version $DGTAG" -o docker-gen-bin
$ cd /path/to/port-eighty/docker-gen
$ mv /path/to/src/github.com/jwilder/docker-gen/docker-gen-bin docker-gen
```

## Build the Docker image

```
$ docker build -t justadam/docker-gen:$DGTAG .
```
