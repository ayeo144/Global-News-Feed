// Main Application package for REST API working on top
// of Postgres database.

package main


import (
	"log"
	"net/http"

	"github.com/gorilla/mux"

	"app/endpoints"
)


func main() {
	// Main function for application, creates the router and adds the endpoints
	// then serves on a selected port.

	router := mux.NewRouter()

	// Need to include "OPTIONS" here as a method to enable CORS
	router.HandleFunc("/records/", endpoints.GetRecordsEndpoint).Methods("GET", "OPTIONS")

	log.Fatal(http.ListenAndServe(":8081", router))

}
