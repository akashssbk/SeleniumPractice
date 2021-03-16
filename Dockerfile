FROM python:3.7
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
RUN wget https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN apt-get install -y awscli
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ADD practice.py /
CMD ["python", "practice.py"]
