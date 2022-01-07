FILENAME = "input.txt"
f = File.open(FILENAME)
pos = f.read.split(",").map(&:to_i)

# This is lazy but it'll work...
# Figure out how much fuel it'll take to get to each position
min = 0
max = pos.max + 1
options = (min..max).map do |option|
  pos.map{|p| p-option}.map(&:abs).sum
end

p options.min
