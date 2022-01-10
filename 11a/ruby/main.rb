require_relative "octopus"

FILENAME = "test_input.txt"

lines = File.open(FILENAME).readlines
values = lines.map(&:chomp).map{|line| line.split("").map(&:to_i)}
x = Octopus::Grid.new(values)
puts x

p [1, 3]
p x.adjacent_to([1, 3])

p [0, 0]
p x.adjacent_to([0, 0])
