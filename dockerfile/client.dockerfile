FROM python:3.10.7

WORKDIR /client

COPY ./requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY ./app .

# command to run on container start
CMD [ "python", "./client.py" ]