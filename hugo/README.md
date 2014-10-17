hugo container
==============

Runs [hugo](https://github.com/spf13/hugo) as a web server inside a Docker container.

## First get a copy of hugo

```
$ wget https://github.com/spf13/hugo/releases/download/v0.12/hugo_0.12_linux_amd64.tar.gz
$ tar -xvf hugo_0.12_linux_amd64.tar.gz 
$ mv hugo_0.12_linux_amd64/hugo_0.12_linux_amd64 hugo
$ rm -rf hugo_*
```

Hugo's working diretory is a volume.  Everything hugo expects should go in there; but hugo is configured to write the actual files into the container's filesystem.

## Build the docker image

```
$ docker build -t justadam/hugo:0.12 .
```

## TODO

- check what config options can be specified via env varibles