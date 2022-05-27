package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type step struct {
	direction string
	magnitude int
}

type position struct {
	depth      int
	horizontal int
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run <inputfile>")
	}
	steps, err := load_from_file(os.Args[1])
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", err)
		os.Exit(1)
	}
	pos := position{0, 0}
	for _, step := range steps {
		pos, err = move(step, pos)
		if err != nil {
			fmt.Fprintf(os.Stderr, "%s\n", err)
			os.Exit(1)
		}
	}
	fmt.Println(pos.depth * pos.horizontal)
}

func move(s step, p position) (position, error) {
	switch s.direction {
	case "forward":
		p.horizontal += s.magnitude
	case "up":
		p.depth -= s.magnitude
	case "down":
		p.depth += s.magnitude
	default:
		return position{}, errors.New("Invalid direction")
	}
	return p, nil
}

func load_from_file(s string) ([]step, error) {
	b, err := os.Open(s)
	if err != nil {
		return nil, err
	}
	scanner := bufio.NewScanner(b)
	scanner.Split(bufio.ScanLines)
	var result []step
	for scanner.Scan() {
		line := scanner.Text()
		words := strings.Fields(line)
		if len(words) != 2 {
			return nil, errors.New("Parse error")
		}
		direction := words[0]
		magnitude, err := strconv.Atoi(words[1])
		if err != nil {
			return nil, err
		}
		result = append(result, step{direction, magnitude})
	}
	return result, scanner.Err()
}
