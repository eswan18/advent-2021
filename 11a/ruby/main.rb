require_relative "octopus"

FILENAME = "minitest_input.txt"

lines = File.open(FILENAME).readlines
values = lines.map(&:chomp).map{|line| line.split("").map(&:to_i)}
grid = Octopus::Grid.new(values)

puts grid
puts "\n"
for i in (1..4)
  grid.turn
  puts grid
  puts "\n"
end
