FROM golang:1.18.2-bullseye

RUN mkdir /code

COPY . /code/

WORKDIR /code/app/

# Download go modules
RUN go mod vendor

# Build the application
RUN go build -o ./compiled/

CMD ["./compiled/app"]