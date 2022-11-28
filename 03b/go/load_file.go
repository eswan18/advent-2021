package main

import (
	"bufio"
	"os"
	"strconv"
)

func readLinesFromFile(filepath string) (lines []string, err error) {
	b, err := os.Open(filepath)
	if err != nil {
		return nil, err
	}
	scanner := bufio.NewScanner(b)
	scanner.Split(bufio.ScanLines)
	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
	}
	return lines, scanner.Err()
}

func convertLinesToIntSlices(lines []string) ([][]int, error) {
	var intLines [][]int
	for _, line := range lines {
		var lineAsInts []int
		for _, char := range line {
			charAsInt, err := strconv.Atoi(string(char))
			if err != nil {
				return nil, err
			}
			lineAsInts = append(lineAsInts, charAsInt)
		}
		intLines = append(intLines, lineAsInts)
	}
	return intLines, nil
}
