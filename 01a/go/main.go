package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func load_from_file(s string) ([]int, error) {
	b, err := os.Open(s)
	if err != nil {
		return nil, err
	}
	scanner := bufio.NewScanner(b)
	scanner.Split(bufio.ScanWords)
	var result []int
	for scanner.Scan() {
		x, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return result, err
		}
		result = append(result, x)
	}
	return result, scanner.Err()
}

func count_increases(numbers []int) int {
	last_n := -1
	incr := 0
	for i, n := range numbers {
		if i != 0 {
			if n > last_n {
				incr += 1
			}
		}
		last_n = n
	}
	return incr
}

func main() {
	if len(os.Args) < 2 {
		panic("Usage: go run <inputfile>")
	}
	numbers, err := load_from_file(os.Args[1])
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", err)
		os.Exit(1)
	}
	result := count_increases(numbers)
	fmt.Println(result)
}
