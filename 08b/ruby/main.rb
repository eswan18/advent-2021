require_relative "digits"

FILENAME = "input.txt"

displays = File.open(FILENAME).readlines.map{|line| Digits::Display.from_string(line)}

p displays.map(&:proper_output).sum
