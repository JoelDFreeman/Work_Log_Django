FROM python:3.8-slim-buster

# Download latest listing of available packages:
RUN apt-get -y update
# Upgrade already installed packages:
RUN apt-get -y upgrade
# Install a new package:
RUN apt-get -y install syslog-ng

RUN apt-get -y install python3-pip

RUN pip3 install Django