FROM python:3.8-slim-buster

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