package main

import (
	"fmt"
)

var memo map[int]uint64

func fib(n int) uint64 {
	if _, ok := memo[n]; ok {
		return memo[n]
	}
	if n < 3 {
		return 1
	}
	memo[n] = fib(n-1) + fib(n-2)
	return memo[n]
}

func main() {
	var count int
	memo = make(map[int]uint64)
	fmt.Scanln(&count)
	for i := 1; i <= count; i++ {
		fmt.Println(fib(i))
	}
}
