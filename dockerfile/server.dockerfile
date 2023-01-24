FROM python:3.10.7-slim

WORKDIR /server

COPY ./requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY ./app .

# command to run on container start
CMD [ "python", "./server.py" ]