# Backend

Backend service of application. Depends on ETL (ELT) service to
create data resources for application.

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