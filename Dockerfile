
#Deriving the latest base image
FROM python:3.9-bookworm


WORKDIR /usr/app

RUN pip install "setuptools<58.0.0"
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

WORKDIR /usr/app/src
RUN chmod 775 /usr/app/src/data/predictions.csv
EXPOSE 5000

CMD ["python3", "main.py", "--host=0.0.0.0"]
