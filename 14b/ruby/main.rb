FILENAME = "input.txt"

lines = File.open(FILENAME).readlines.map(&:chomp)

sequence = lines[0].split("")
rules = Hash[
  lines[2..].map do |line|
    pair, insertion = line.split(" -> ")
  end
]

class Array
  def update(rules)
    new_seq = clone
    (length-1).times do |i|
      insertion = rules.fetch(self[i] + self[i+1])
      new_seq.insert(2*i+1, insertion)
    end
    new_seq
  end
end

10.times do
  sequence = sequence.update(rules)
end

most_common_letter = sequence.max_by{|s| sequence.count(s)}
least_common_letter = sequence.min_by{|s| sequence.count(s)}
result = sequence.count(most_common_letter) - sequence.count(least_common_letter)
p result
