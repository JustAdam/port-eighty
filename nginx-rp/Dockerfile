FROM ubuntu:14.04

MAINTAINER JustAdam <adambell7@gmail.com>

RUN apt-get update && \
    apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx"]