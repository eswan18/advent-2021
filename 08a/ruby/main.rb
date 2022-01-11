require_relative "digits"

FILENAME = "test_input.txt"

displays = File.open(FILENAME).readlines.map{|line| Digits::Display.from_string(line)}

p displays[0]
