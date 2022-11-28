package main

import (
	"fmt"
	"math"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run <inputfile>")
		os.Exit(1)
	}
	lines, err := readLinesFromFile(os.Args[1])
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", err)
		os.Exit(1)
	}
	intLines, err := convertLinesToIntSlices(lines)
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", err)
		os.Exit(1)
	}

	// Oxygen ...
	linesForO2 := intLines
	position := 0
	// Run as long as we have more than one line.
	for len(linesForO2) > 1 {
		mostCommon := mostCommonAtPosition(linesForO2, position)
		// For the next iteration, keep only lines that have this value.
		linesForO2 = linesWhereValueAtPosition(linesForO2, position, mostCommon)
		position++
	}
	winningLine := linesForO2[0]
	oxygen := lineToDecimal(winningLine)
	fmt.Println("Oxygen rating:", oxygen)

	// CO2 ...
	linesForCO2 := intLines
	position = 0
	// Run as long as we have more than one line.
	for len(linesForCO2) > 1 {
		mostCommon := mostCommonAtPosition(linesForCO2, position)
		leastCommon := 1 - mostCommon
		// For the next iteration, keep only lines that have this value.
		linesForCO2 = linesWhereValueAtPosition(linesForCO2, position, leastCommon)
		position++
	}
	winningLine = linesForCO2[0]
	co2 := lineToDecimal(winningLine)
	fmt.Println("CO2 rating:", co2)

	fmt.Println("Multiplied together:", co2*oxygen)
}

// Finds the most commonly-occuring number at a given position in a slice of slices of ints.
func mostCommonAtPosition(lines [][]int, position int) int {
	counts := make(map[int]int)
	for _, line := range lines {
		counts[line[position]]++
	}

	// Assuming only 0s and 1s will appear.
	if counts[0] > counts[1] {
		return 0
	} else {
		return 1
	}
}

// Return a slices of all lines that have a certain value in a certain position.
func linesWhereValueAtPosition(lines [][]int, position int, value int) [][]int {
	var goodLines [][]int
	for _, line := range lines {
		if line[position] == value {
			goodLines = append(goodLines, line)
		}
	}
	return goodLines
}

func lineToDecimal(line []int) int {
	total := 0
	lineLength := len(line)
	for i := 0; i < lineLength; i++ {
		place := math.Pow(2, float64(i))
		value := line[lineLength-(i+1)]
		total += (int(place) * value)
	}
	return total
}
