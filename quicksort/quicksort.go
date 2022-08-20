package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"math/rand"
	"os"
	"strconv"
	"time"
)

func main() {
	cantidades := []string{"100","1000","2000","3000","4000","5000","6000","7000","8000","9000","10000","20000","30000","40000","50000"}
	for i := 0; i < 15; i++ {
		tiempos := []int{}
		for j := 0; j < 5; j++ {
			slice := readFileCsv("../data/"+cantidades[i]+".csv")
			start := time.Now()
			quicksort(slice)
			duration := time.Since(start)
			durationNano := int(duration.Nanoseconds())
			tiempos = append(tiempos, durationNano)
		}
		writeFileCsv("../output/quicksort/go/"+cantidades[i]+".csv",tiempos)
	}
}

func readFileCsv(fileName string) []int {
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

func writeFileCsv(fileName string, vals []int){
	rec, err := os.Create(fileName)
    defer rec.Close()

    if err != nil {
		fmt.Println("failed to open file", err)
    }

    w := csv.NewWriter(rec)
	w.Comma = ';'
	
    defer w.Flush()
	var valsStr []string
	for _, i := range vals {
		valsStr = append(valsStr, strconv.Itoa(i))
	}
	if err := w.Write(valsStr); err != nil {
		fmt.Println("error writing record to file", err)
	}
}

func generateSlice(size int) []int {

	slice := make([]int, size, size)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < size; i++ {
		slice[i] = rand.Intn(999) - rand.Intn(999)
	}
	return slice
}

func quicksort(a []int) []int {
	if len(a) < 2 {
		return a
	}

	left, right := 0, len(a)-1

	pivot := rand.Int() % len(a)

	a[pivot], a[right] = a[right], a[pivot]

	for i, _ := range a {
		if a[i] < a[right] {
			a[left], a[i] = a[i], a[left]
			left++
		}
	}

	a[left], a[right] = a[right], a[left]

	quicksort(a[:left])
	quicksort(a[left+1:])

	return a
}
