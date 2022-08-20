package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"os"
	"sort"
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
			heapSort(sort.IntSlice(slice))
			duration := time.Since(start)
			durationNano := int(duration.Nanoseconds())
			tiempos = append(tiempos, durationNano)
		}
		writeFileCsv("../output/heapsort/go/"+cantidades[i]+".csv",tiempos)
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

func heapSort(list sort.Interface) {
	for start := (list.Len() - 2) / 2; start >= 0; start-- {
	   siftDown(list, start, list.Len()-1)
	}
	for end := list.Len() - 1; end > 0; end-- {
	   list.Swap(0, end)
	   siftDown(list, 0, end-1)
	}
 }
  
 func siftDown(list sort.Interface, start, end int) {
	for root := start; root*2+1 <= end; {
	   child := root*2 + 1
	   if child+1 <= end && list.Less(child, child+1) {
		  child++
	   }
	   if !list.Less(root, child) {
		  return
	   }
	   list.Swap(root, child)
	   root = child
	}
 }
