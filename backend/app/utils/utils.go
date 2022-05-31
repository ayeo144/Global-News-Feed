// utils.go package containing utility functions for the application

package utils


import (
	"os"
	"strconv"
	"fmt"
)


// Struct to hold variables required for DB connection
type DbVars struct {
	Host string
	Port int
	Username string
	Password string
	Database string
}


// Function to get the Port the database can be accessed from the
// environment variables and convert to integer.
func get_port() int {

	port, err := strconv.Atoi(os.Getenv("DB_PORT"))

	if err != nil {
		// handle error
		fmt.Println(err)
		os.Exit(2)
	}

	return port
}


// Function to get the database variables from the environment
// and assign them to the variables in the DBVars struct.
func GetDbVars() DbVars {

	Vars := DbVars{
		Host: os.Getenv("DB_HOST"),
		Port: get_port(),
		Username: os.Getenv("DB_USERNAME"),
		Password: os.Getenv("DB_PASSWORD"),
		Database: os.Getenv("DB_NAME"),
	}

	return Vars

}


func GetDbInfo() string {

	var db_vars DbVars = GetDbVars()

	DbInfo := fmt.Sprintf(
		"host=%s port=%d user=%s password=%s dbname=%s sslmode=disable",
		db_vars.Host, 
		db_vars.Port, 
		db_vars.Username, 
		db_vars.Password, 
		db_vars.Database,
	)

	return DbInfo

}