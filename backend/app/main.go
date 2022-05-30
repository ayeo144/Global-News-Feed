package main


import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"

	"app/utils"
)


func main() {

	// Get the structure containing the variables for the database connection
	var db_vars utils.DBVars = utils.GetDBVars()

	psqlInfo := fmt.Sprintf(
		"host=%s port=%d user=%s password=%s dbname=%s sslmode=disable",
		db_vars.Host, 
		db_vars.Port, 
		db_vars.Username, 
		db_vars.Password, 
		db_vars.Database,
	)

	db, err := sql.Open("postgres", psqlInfo)

	if err != nil {
		panic(err)
	  }
	  defer db.Close()
	
	  err = db.Ping()
	  if err != nil {
		panic(err)
	  }

	db.Close()

	fmt.Println(db_vars.Host)
}
