docker-gen container
====================

Runs [docker-gen](https://github.com/jwilder/docker-gen) stand alone inside a container. 

## Build a docker-gen binary

```
$ git clone git@github.com:jwilder/docker-gen.git
$ cd docker-gen
$ DGTAG=$(git describe --tags --abbrev=0 | sed 's/^v//' | sed 's/\+.*$$//')
$ go build -ldflags "-s -X main.Version $DGTAG" -o ../docker-gen
$ cd ..
$ rm -rf docker-gen/
```

## Build the Docker image

```
$ docker build -t justadam/docker-gen:$DGTAG .
```