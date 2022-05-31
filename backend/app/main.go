package main


import (
	"fmt"
	"database/sql"

	_ "github.com/lib/pq"

	"app/utils"
	"app/crud"
)


func main() {

	// Get the structure containing the variables for the database connection
	var db_info string = utils.GetDbInfo()

	db, err := sql.Open("postgres", db_info)

	if err != nil {
		panic(err)
	  }
	  defer db.Close()
	
	  err = db.Ping()
	  if err != nil {
		panic(err)
	  }

	records := crud.GetRecords(db)

	fmt.Println(records[0].Id)

	db.Close()

}
