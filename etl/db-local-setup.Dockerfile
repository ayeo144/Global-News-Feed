# This Dockerfile is for local testing of the set-up
# of the production database (e.g. db creation, table
# creation, and inserting data from configuration.

FROM python:3.8-slim

# Get the arguments passed at build-time
ARG DB_USERNAME
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT
ARG DB_NAME

# Set the environment variables required for the Python code
ENV DB_USERNAME ${DB_USERNAME}
ENV DB_PASSWORD ${DB_PASSWORD}
ENV DB_HOST ${DB_HOST}
ENV DB_PORT ${DB_PORT}
ENV DB_NAME ${DB_NAME}

# Required for psycopg2
RUN apt-get update
RUN apt-get install -y gcc libpq-dev python-dev

# this creates the working directory inside our container
WORKDIR code/

# copy the API code into the working directory
COPY . /code/

# install the requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# RUN python /code/scripts/deploy_db.py

# run the code to set-up the database and tables
CMD ["python", "/code/scripts/deploy_db.py"]