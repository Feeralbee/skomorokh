FROM ubuntu:22.10

RUN apt-get update
RUN apt-get install -y python3 python3-pip

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip -r requirements.txt
WORKDIR /skomorokh
CMD ["python3", "main.py"]
