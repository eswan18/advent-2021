FILENAME = "input.txt"
file = File.open(FILENAME)
lines = file.readlines.map(&:chomp)

increases = 0
last_sum = -1

lines.each_cons(3) do |a|
  sum = a.map(&:to_i).sum
  if last_sum != -1 and sum > last_sum
      increases += 1
  end
  last_sum = sum
end

puts increases
