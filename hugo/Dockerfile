FROM ubuntu:14.04

MAINTAINER JustAdam <adambell7@gmail.com>

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean

ADD hugo /usr/bin/hugo

# Ouput files
RUN mkdir /hugo

VOLUME ["/content"]

EXPOSE 1313

CMD ["/usr/bin/hugo", "server", "--watch", "--appendPort=false", "--disableLiveReload=true", "--source=/content", "--destination=/hugo"]