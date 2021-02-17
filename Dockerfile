FROM alpine 

RUN apk update
RUN apk add python3
RUN apk add py3-pip
RUN pip3 install flask
RUN cd /opt
RUN mkdir cmx_receiver

COPY cmxreceiver.py /opt/cmx_receiver/

CMD  python3 /opt/cmx_receiver/cmxreceiver.py
