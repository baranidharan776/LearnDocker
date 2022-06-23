FROM ubuntu:18.04
RUN apt update && apt install python3 -y  && apt install python3-pip -y
RUN pip3 install flask
COPY app.py /opt
EXPOSE 8080
CMD ["python3", "/opt/app.py"]

