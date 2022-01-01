FILENAME = "input.txt"
file = File.open(FILENAME)
lines = file.readlines.map(&:chomp)

increases = 0
last_val = 0

lines.length.times do |i|
  val = lines[i].to_i
  if i > 0 and val > last_val
    increases += 1
  end
  last_val = val
end

puts increases
