FILENAME = "input.txt"
def get_lines
  file = File.open(FILENAME)
  lines = file.readlines.map(&:chomp).map { |line| line.split("").map(&:to_i) }
  lines
end

# Oxygen
numbers = get_lines
position = 0
while numbers.length > 1
  bits = numbers.map { |line| line[position] }
  ones = bits.count(1)
  zeros = bits.count(0)
  most_common = ones >= zeros ? 1 : 0
  numbers = numbers.filter { |number| number[position] == most_common }
  position += 1
end
o2 = numbers.join("").to_i(base=2)

# CO2
numbers = get_lines
position = 0
while numbers.length > 1
  bits = numbers.map { |line| line[position] }
  ones = bits.count(1)
  zeros = bits.count(0)
  least_common = ones >= zeros ? 0 : 1
  numbers = numbers.filter { |number| number[position] == least_common }
  position += 1
end
co2 = numbers.join("").to_i(base=2)

puts "oxygen #{o2}"
puts "co2 #{co2}"
puts "result = #{o2 * co2}"
