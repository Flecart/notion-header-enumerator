FROM python:3.9-alpine
LABEL MAINTAINER="Angelo Flecart Huang <huangelo02@gmail.com>"

ENV GROUP_ID=1000
ENV USER_ID=1000

WORKDIR /usr/src/app

COPY . . 

RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
