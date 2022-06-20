package main

import (
	"fmt"
)

// Задание 3
// В массиве из 10 чисел найти сумму элементов больших, чем   второй элемент этого массива.

// RemoveIndex - deletes an element from  Slice. Удаляет элемент из типа Slice
func RemoveIndex(s []int, index int) []int {
	return append(s[:index], s[index+1:]...)
}

func main() {
	initSlice := make([]int, 0)

	for l := 0; l < 10; l++ {
		fmt.Println("Please enter number", (l + 1))
		fmt.Print("-> ")
		var integer int
		fmt.Scan(&integer)
		initSlice = append(initSlice, integer)
	}

	fmt.Println(initSlice)
	var secondInt = initSlice[1] // первый индекс - 0, => второе число - 1

	slice := RemoveIndex(initSlice, 1)

	var sum int = 0

	for i := 0; i < len(slice); i++ {
		if slice[i] > secondInt {
			sum = sum + slice[i]
		}
	}

	fmt.Println("Result: ", sum)
}
