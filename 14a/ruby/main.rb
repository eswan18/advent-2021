FILENAME = "input.txt"

lines = File.open(FILENAME).readlines.map(&:chomp)

sequence = lines[0]
rules = Hash[
  lines[2..].map do |line|
    pair, insertion = line.split(" -> ")
  end
]

class String
  def update(rules)
    new_seq = split("").join(" ")
    (length-1).times do |i|
      new_seq[2*i+1] = rules[self[i]+self[i+1]]
    end
    new_seq
  end
end

10.times do
  sequence = sequence.update(rules)
end
seq_array = sequence.split("")
most_common_letter = seq_array.max_by{|s| seq_array.count(s)}
least_common_letter = seq_array.min_by{|s| seq_array.count(s)}
result = seq_array.count(most_common_letter) - seq_array.count(least_common_letter)
p result
