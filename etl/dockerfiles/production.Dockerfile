FROM python:3.8-slim

# Get the arguments passed at build-time
ARG NEWS_API_KEY
ARG AWS_ACCESS_KEY
ARG AWS_SECRET_KEY
ARG S3_BUCKET_NAME
ARG DB_USERNAME
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT
ARG DB_NAME

# Set the environment variables required for the Python code
ENV NEWS_API_KEY ${NEWS_API_KEY}
ENV AWS_ACCESS_KEY ${AWS_ACCESS_KEY}
ENV AWS_SECRET_KEY ${AWS_SECRET_KEY}
ENV S3_BUCKET_NAME ${S3_BUCKET_NAME}
ENV DB_USERNAME ${DB_USERNAME}
ENV DB_PASSWORD ${DB_PASSWORD}
ENV DB_HOST ${DB_HOST}
ENV DB_PORT ${DB_PORT}
ENV DB_NAME ${DB_NAME}

# Required for psycopg2
RUN apt-get update
RUN apt-get install -y gcc libpq-dev python-dev

# this creates the working directory inside our container
WORKDIR /code

# copy the API code into the working directory
COPY . /code/

# install the requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# run tests
RUN pytest -v -m production /code/tests