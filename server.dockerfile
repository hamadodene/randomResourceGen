FROM python:3.10.7

WORKDIR /app

COPY server_requirements.txt .

# install dependencies
RUN pip install -r server_requirements.txt

# copy the content of the local src directory to the working directory
COPY ./app .

# command to run on container start
CMD [ "python", "./server.py" ]