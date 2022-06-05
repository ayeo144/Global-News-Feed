// Endpoint(s) for Records

package endpoints

import (
	"encoding/json"
	"net/http"

	_ "github.com/lib/pq"

	"app/utils"
	"app/crud"
)


// Response object for list of Records queried from database
type RecordResponse struct {
	Type string `json:"type"`
	Data []crud.Record `json:"data"`
}


func GetRecordsEndpoint(w http.ResponseWriter, r *http.Request) {
	// Open connection to database, query the 'production' table to
	// get records.
	db := utils.SetupDb()
	records := crud.GetRecords(db)
	db.Close()

	// Construct the JSON response object containing the records
	var response = RecordResponse{Type: "success", Data: records}

    //Allow CORS here By * or specific origin
    w.Header().Set("Access-Control-Allow-Origin", "*")
    w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

	// Encode the response object
	json.NewEncoder(w).Encode(response)

}