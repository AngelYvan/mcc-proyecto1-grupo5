package main

import "fmt"

func mergesort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	left := []int(arr[0 : len(arr)/2])
	right := []int(arr[len(arr)/2:])

	left = mergesort(left)
	right = mergesort(right)

	arr = make([]int, len(left)+len(right))
	j, k := 0, 0
	for i := 0; i < len(arr); i++ {
		if j >= len(left) {
			arr[i] = right[k]
			k++
			continue
		} else if k >= len(right) {
			arr[i] = left[j]
			j++
			continue
		} else if left[j] > right[k] {
			arr[i] = right[k]
			k++
		} else {
			arr[i] = left[j]
			j++
		}
	}
	return arr
}

func main() {
	a := []int{21,2,61,63,50,35,46,42,3,80,14,80,7,65,27,32,23,7,4,72,96,37,10,87,60,61,46,38,85,77,99,38,54,93,35,28,19,52,100,62,67,71,85,78,57,27,45,20,61,22,11,70,100,79,74,27,64,82,7,56,15,73,68,13,30,39,34,94,17,70,32,37,49,34,51,56,3,91,77,62,56,65,98,92,61,75,11,91,35,54,63,16,24,22,11,28,43,15,4,53}
	fmt.Printf("%v\n", mergesort(a))
}



