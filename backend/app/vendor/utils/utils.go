package utils


// Structure to hold variables in
type Variables struct {
	Name string
	Message string
}


// Function that gets the Name from the Variables struct
func GetName(v Variables) string {
	return v.Name
}


// Function that gets the Message from the Variables struct
func GetMessage(v Variables) string {
	return v.Message
}
