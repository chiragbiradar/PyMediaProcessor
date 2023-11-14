FROM ubuntu

RUN apt-get update && apt-get install -y apt-transport-https && apt-get install -y python3 && apt-get install -y python3-pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

RUN apt-get install -y ffmpeg

EXPOSE 5000

RUN python3 createdb.py
CMD ["python3", "app.py"]