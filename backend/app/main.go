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

	router.HandleFunc("/records/", endpoints.GetRecordsEndpoint).Methods("GET")

	log.Fatal(http.ListenAndServe(":8000", router))

}
