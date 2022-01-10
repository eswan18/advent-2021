require_relative "octopus"

FILENAME = "input.txt"
N_STEPS = 100

lines = File.open(FILENAME).readlines
values = lines.map(&:chomp).map{|line| line.split("").map(&:to_i)}
grid = Octopus::Grid.new(values)

N_STEPS.times do
  grid.turn
end
puts grid.flashes
