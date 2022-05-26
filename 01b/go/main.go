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

func sum(numbers []int) int {
	s := 0
	for _, elem := range numbers {
		s += elem
	}
	return s
}

func sum_windows(window_size int, numbers []int) []int {
	if len(numbers) < window_size {
		panic("you moron")
	}
	n_windows := len(numbers) - (window_size - 1)
	window_sums := make([]int, 0, n_windows)
	for i := 0; i < n_windows; i++ {
		window := numbers[i : i+window_size]
		window_sums = append(window_sums, sum(window))
	}
	return window_sums
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
	sums := sum_windows(3, numbers)
	result := count_increases(sums)
	fmt.Println(result)
}
