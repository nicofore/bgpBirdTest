FROM ubuntu:latest

WORKDIR /root

RUN apt-get update && apt-get install -qy git autoconf libtool gawk make \
flex bison libncurses-dev libreadline6-dev iproute2

RUN apt-get install -qy flex

RUN apt-get install -qy python3

RUN apt-get install -qy pip

RUN pip install netaddr

RUN pip install netifaces

RUN git config --global http.sslverify false

RUN git clone https://gitlab.nic.cz/labs/bird.git

RUN cd bird && autoreconf -i && ./configure && make && make install

COPY neighbor.py .

COPY target.py .