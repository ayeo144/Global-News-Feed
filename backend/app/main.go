package main


import (
	"utils"

	"fmt"
)


func main() {

	// Get the structure containing the variables for the database connection
	var db utils.DBVars = utils.GetDBVars()

	fmt.Println(db.Host)
}
