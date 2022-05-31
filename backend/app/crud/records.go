package crud


import (
	"time"
	"database/sql"
)


type Record struct {
	Id int
	Source string
	Author sql.NullString
	Title string
	URL string
	PublishDate time.Time
	Country string
	TimeStamp time.Time
	Lon float32
	Lat float32
}


func GetRecords(db *sql.DB) []Record {

	rows, err := db.Query("SELECT * FROM production;")

	if err != nil {
		panic(err)
	}

	defer rows.Close()

	Records := []Record{}

	for rows.Next() {

		var r Record

		err := rows.Scan(
			&r.Id, 
			&r.Source,
			&r.Author,
			&r.Title,
			&r.URL,
			&r.PublishDate,
			&r.Country,
			&r.TimeStamp,
			&r.Lon,
			&r.Lat,
		)

		if err != nil {
			panic(err)
		}

		Records = append(Records, r)

	}

	return Records

}