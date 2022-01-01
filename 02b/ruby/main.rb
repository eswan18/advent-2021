FILENAME = "input.txt"
file = File.open(FILENAME)
lines = file.readlines.map(&:chomp)

$horizontal = 0
$depth = 0
$aim = 0

def parse_line(line)
  direction, qty = line.split
  qty = qty.to_i
  case direction
  when "forward"
    $horizontal += qty
    $depth += ($aim * qty)
  when "up"
    $aim -= qty
  when "down"
    $aim += qty
  else
    puts "invalid input"
  end
end

lines.each { |line| parse_line(line) }

puts $horizontal * $depth
