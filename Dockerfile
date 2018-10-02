FROM python:2.7
RUN pip install -U pytest
RUN pip install -U requests
RUN mkdir /data
WORKDIR /data
ADD . /data
