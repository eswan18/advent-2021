FILENAME = "input.txt"

lines = File.open(FILENAME).readlines.map(&:chomp)

sequence = lines[0].split("")
Rules = Hash[
  lines[2..].map do |line|
    pair, insertion = line.split(" -> ")
  end
]

# A hash of hashes
Cache = Hash.new{ | hash, key| hash[key] = {} }

class Array
  def update(times=1)
    if times == 1
      new_seq = clone
      (length-1).times do |i|
        insertion = Rules.fetch(self[i] + self[i+1])
        new_seq.insert(2*i+1, insertion)
      end
      new_seq
    elsif times == 10
      if Cache[10].include?(self)
        Cache[10][self]
      else
        seq = self
        10.times do
          seq = seq.update
        end
        Cache[10][self] = seq
      end
    elsif times == 20
      if Cache[20].include?(self)
        Cache[20][self]
      else
        result = update(10).update(10)
        Cache[20][self] = result
      end
    else
      raise RuntimeError "Bad number of times"
    end
  end
  def value_counts
    counts = Hash.new 0
    each{|letter| counts[letter] += 1}
    counts
  end
  def max_minus_min
    counts = value_counts
    min, max = counts.minmax_by{|k, v| v}
    max[1] - min[1]
  end
end

sequence = sequence.update(20)
p sequence.max_minus_min
