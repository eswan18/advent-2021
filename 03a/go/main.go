package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run <inputfile>")
	}
	lines, err := load_from_file(os.Args[1])
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", err)
		os.Exit(1)
	}
	n_bits := len(lines[0])
	gamma := make([]rune, n_bits)
	for i := 0; i < n_bits; i++ {
		var bits []rune
		for _, line := range lines {
			bits = append(bits, rune(line[i]))
		}
		err, most_common_bit := most_common(bits)
		if err != nil {
			fmt.Fprintf(os.Stderr, "%s\n", err)
			os.Exit(1)
		}
		gamma[i] = most_common_bit
	}
	err, epsilon := invert(gamma)
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", err)
		os.Exit(1)
	}
	gamma_val, err := strconv.ParseInt(string(gamma), 2, 64)
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", err)
		os.Exit(1)
	}
	epsilon_val, err := strconv.ParseInt(string(epsilon), 2, 64)
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", err)
		os.Exit(1)
	}
	result := gamma_val * epsilon_val
	fmt.Println(result)
}

func most_common[T comparable](slc []T) (error, T) {
	counts := make(map[T]int)
	var winning_element T
	if len(slc) < 1 {
		return errors.New("Can't get most common element of empty slice"), winning_element
	}
	for _, elem := range slc {
		counts[elem] += 1
	}
	max_count := -1
	for elem, count := range counts {
		if count > max_count {
			max_count = count
			winning_element = elem
		}
	}
	return nil, winning_element
}

func invert(input []rune) (error, []rune) {
	var inverse []rune
	for _, r := range input {
		if r == '1' {
			inverse = append(inverse, '0')
		} else if r == '0' {
			inverse = append(inverse, '1')
		} else {
			return errors.New("Unexpected rune"), make([]rune, 0)
		}
	}
	return nil, inverse
}

func load_from_file(s string) ([]string, error) {
	b, err := os.Open(s)
	if err != nil {
		return nil, err
	}
	scanner := bufio.NewScanner(b)
	scanner.Split(bufio.ScanLines)
	var result []string
	for scanner.Scan() {
		line := scanner.Text()
		result = append(result, line)
	}
	return result, scanner.Err()
}
