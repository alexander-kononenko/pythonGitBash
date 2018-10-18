FROM python:2.7
RUN sudo pip install -U pytest
RUN sudo pip install -U requests
RUN sudo mkdir /data
WORKDIR /data
ADD . /data
