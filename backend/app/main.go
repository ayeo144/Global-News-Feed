package main

import (
	"fmt"
)


// Structure to hold variables in
type variables struct {
	name string
	message string
}


// Function that gets variables from somewhere and
// populates the `variables` struct, then returns it
func get_variables() variables {

	vars := variables{
		name: "Hannah",
		message: "Hello",
	}

	return vars
}


func main() {
	
	var string_message string
	var message_vars variables = get_variables()

	string_message = message_vars.message + ", " + message_vars.name

	fmt.Println(string_message)
}