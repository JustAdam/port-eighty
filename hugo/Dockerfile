FROM ubuntu:14.04

MAINTAINER JustAdam <adambell7@gmail.com>

ADD hugo /usr/bin/hugo

# Ouput files
RUN mkdir /hugo

VOLUME ["/content"]

EXPOSE 1313

CMD ["/usr/bin/hugo", "server", "--watch", "--appendPort=false", "--disableLiveReload=true", "--source=/content", "--destination=/hugo"]