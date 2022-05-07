FROM python:3.8-slim-buster

# Get the arguments passed at build-time
ARG NEWS_API_KEY
ARG AWS_ACCESS_KEY
ARG AWS_SECRET_KEY
ARG S3_BUCKET_NAME
ARG AWS_DB_INSTANCE_ID
ARG AWS_DB_USERNAME
ARG AWS_DB_PASSWORD
ARG AWS_DB_HOST
ARG AWS_DB_PORT
ARG AWS_DB_NAME

# Set the environment variables required for the Python code
ENV NEWS_API_KEY ${NEWS_API_KEY}
ENV AWS_ACCESS_KEY ${AWS_ACCESS_KEY}
ENV AWS_SECRET_KEY ${AWS_SECRET_KEY}
ENV S3_BUCKET_NAME ${S3_BUCKET_NAME}
ENV AWS_DB_INSTANCE_ID ${AWS_DB_INSTANCE}
ENV AWS_DB_USERNAME ${AWS_DB_USERNAME}
ENV AWS_DB_PASSWORD ${AWS_DB_PASSWORD}
ENV AWS_DB_HOST ${AWS_DB_HOST}
ENV AWS_DB_PORT ${AWS_DB_PORT}
ENV AWS_DB_NAME ${AWS_DB_NAME}

# Required for psycopg2
RUN apt-get update
RUN apt-get install -y libpq-dev python-dev

# this creates the working directory inside our container
WORKDIR code/

# copy the API code into the working directory
COPY . /code/

# install the requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# run tests
RUN pytest -v /code/tests

# run the ETL process
CMD ["python", "/code/run.py"]