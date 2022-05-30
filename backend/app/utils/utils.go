// utils.go package containing utility functions for the application

package utils


import (
	"os"
	"strconv"
	"fmt"
)


// Struct to hold variables required for DB connection
type DBVars struct {
	Host string
	Port int
	Username string
	Password string
	Database string
}


func get_port() int {

	port, err := strconv.Atoi(os.Getenv("PORT"))

    if err != nil {
        // handle error
        fmt.Println(err)
        os.Exit(2)
    }

	return port
}


// Function to get the database variables from the environment
// and assign them to the variables in the DBVars struct.
func GetDBVars() DBVars {

	Vars := DBVars{
		Host: os.Getenv("HOST"),
		Port: get_port(),
		Username: os.Getenv("USERNAME"),
		Password: os.Getenv("PASSWORD"),
		Database: os.Getenv("DATABASE"),
	}

	return Vars

}