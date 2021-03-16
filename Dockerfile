FROM python:3.7
ADD practice.py /
RUN pip3 install -r requirements.txt
CMD ['python", 'practice.py"]
