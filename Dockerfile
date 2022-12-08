FROM python:3.7.3

ADD Hello_Docker_World.py .

RUN pip3 install flask

CMD ["python","./Hello_Docker_World.py"]