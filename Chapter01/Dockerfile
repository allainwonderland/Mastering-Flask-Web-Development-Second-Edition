FROM python:3.6.5

WORKDIR /app

ADD . /app
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
#RUN pip3 install Flask
EXPOSE 5000
CMD ["python", "main.py"]

