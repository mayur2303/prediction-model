
#Deriving the latest base image
FROM python:3.9-bookworm


WORKDIR /usr/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /usr/app/src
EXPOSE 6000

CMD ["python3", "main.py", "--host=0.0.0.0"]
