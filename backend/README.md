# Backend

Backend service of application. Depends on ETL (ELT) service to
create data resources for application.

### Tips for writing code in Go

* If you want any variables/functions in one package to be exposed and available for use in another package, you must begin their name with an uppercase letter otherwise they will be undefined when you import them into another package.

### Useful command-line snippets for Go

Creating a new module:

`mkdir <module-name>`
`cd <module-name>`
`go mod init <module-name>`

Running module code from within the root folder of the module:

`go run .`

Compiling:

here we are writing the compiled files to a folder in `<module-name>/compiled/`...

`go build -o ./compiled/`

Running the compiled code:

`./compiled/<module-name>`

### CORS Problem/Solution

When running the docker-compose, the frontend service was not able to query the backend
service REST API due to a CORS error - "Cross-Origin Request Blocked". I first tried several
approaches to reconfiguring nginx (which the frontend service was running on), such as using
a proxy for the backend service URL in the hope that the frontend could access it. 
<br>
Ultimately, it was configuring the backend code and adding specific headers to all the requests
that allowed for cross-origin requests to be made. This resource was extremely helpful for getting
the problem solved: https://stackoverflow.com/questions/39507065/enable-cors-in-golang.