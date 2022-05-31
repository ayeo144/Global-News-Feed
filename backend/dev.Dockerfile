FROM golang:1.18.2-bullseye

# RUN mkdir /code

# COPY . /code/

# Download go modules
# RUN go mod download

# Build the application
# RUN go build -o

ENTRYPOINT ["tail", "-f", "/dev/null"]