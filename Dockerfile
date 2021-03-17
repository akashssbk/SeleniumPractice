FROM ubuntu:18.04
COPY . /
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip && apt-get install wget
RUN wget https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN curl https://intoli.com/install-google-chrome.sh | bash
RUN sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
#RUN apt-get install -y awscli
RUN pip3 install -r requirements.txt
ADD practice.py /
CMD ["python", "practice.py"]
