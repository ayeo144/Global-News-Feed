FROM python:3.8-slim-buster

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

# this creates the working directory inside our container
WORKDIR code/

# copy the API code into the working directory
COPY . /code/

# install the requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# run tests
RUN pytest -v /code/tests

# run the API
CMD ["python", "/code/run.py"]