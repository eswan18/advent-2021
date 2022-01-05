require_relative "vent_line"

FILENAME = "input.txt"

f = File.open(FILENAME)
coords = f.readlines.map(&:chomp).map{|line| line.split(" -> ").map{|coord| coord.split(",").map(&:to_i)}}

vent_lines = coords.map{|vl| VentLine.new(*vl)}

max_x = coords.map{|c| [c[0][0], c[1][0]]}.max.max
max_y = coords.map{|c| [c[0][1], c[1][1]]}.max.max

cts = Array.new(max_x+1) { Array.new(max_y+1, 0) }

vent_lines.each do |vl|
  vl.covered.each do |x, y|
    cts[x][y] += 1
  end
end

# How many spots in the counts grid have at least 2 lines on them?
p cts.map{|row| row.select{|x| x >= 2}.length}.sum
