FROM python:3.7
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
RUN apt-get install -y chromium-browser
RUN apt-get install -y awscli
RUN pip3 install -r requirements.txt
ADD practice.py /
CMD ["python", "practice.py"]
