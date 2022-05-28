// utils.go package containing utility functions for the application

package utils


import (
	"os"
)


// Struct to hold variables required for DB connection
type DBVars struct {
	Host string
	Port string
	Username string
	Password string
	Database string
}


// Function to get the database variables from the environment
// and assign them to the variables in the DBVars struct.
func GetDBVars() DBVars {

	Vars := DBVars{
		Host: os.Getenv("HOST"),
		Port: os.Getenv("PORT"),
		Username: os.Getenv("USERNAME"),
		Password: os.Getenv("PASSWORD"),
		Database: os.Getenv("DATABASE"),
	}

	return Vars

}