package utils

import (
	"encoding/csv"
	"fmt"
	"io"
	"os"
	"strconv"
)

func readFileCSV(fileName string) []int {
	data := []int{}
	f, err := os.Open(fileName)
	if err != nil {
		fmt.Println(err)
	}
	// remember to close the file at the end of the program
	defer f.Close()
	// read csv values using csv.Reader
	csvReader := csv.NewReader(f)
	csvReader.Comma = ';'
	for {
		rec, err := csvReader.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			fmt.Println(err)
		}
		// do something with read line
		for idx, val := range rec {
			intVar, err := strconv.Atoi(val)
			if err != nil {
				fmt.Println("Error in line", idx, "Error type:", err)
			}
			data = append(data, intVar)
		}
	}
	return data
}
