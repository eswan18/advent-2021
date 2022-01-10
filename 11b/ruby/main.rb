require_relative "octopus"

FILENAME = "input.txt"
N_STEPS = 100000

lines = File.open(FILENAME).readlines
values = lines.map(&:chomp).map{|line| line.split("").map(&:to_i)}
grid = Octopus::Grid.new(values)

N_STEPS.times do |t|
  all_flash = grid.turn
  if all_flash
    puts t+1
    break
  end
end
