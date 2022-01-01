FILENAME = "input.txt"
file = File.open(FILENAME)
lines = file.readlines.map(&:chomp).map { |line| line.split("") }
len = lines[0].length

gamma = []

for i in 0..(len - 1) do
  bits = lines.map { |line| line[i] }.map(&:to_i)
  if bits.count(1) > bits.count(0)
    gamma.append(1)
  else
    gamma.append(0)
  end
end
gamma = gamma.join("").to_i(base=2)
epsilon = gamma ^ (2 ** len - 1)

puts "gamma #{gamma}"
puts "epsilon #{epsilon}"
puts "result #{epsilon * gamma}"
