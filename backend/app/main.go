package main


import (
	u "utils"

	"fmt"
)


func main() {

	// Initialise an instance of the Variables struct and assign some values
	variables := u.Variables{
		Name: "Alex",
		Message: "Hello",
	}

	// Get the Name and Message from the struct
	var name string = u.GetName(variables)
	var message string = u.GetMessage(variables)

	var string_message string = message + ", " + name

	fmt.Println(string_message)
}

