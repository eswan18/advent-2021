FILENAME = "input.txt"

lines = File.open(FILENAME).readlines.map(&:chomp)

sequence = lines[0].split("")
Rules = Hash[
  lines[2..].map do |line|
    pair, insertion = line.split(" -> ")
  end
]

# A hash of hashes: {[pair, N] => sequence}
Cache = Hash.new{ | hash, key| hash[key] = {} }

class Array
  def update(times=1)
    # print "updating #{self} #{times} times"
    if size == 1
      raise RuntimeError
    elsif size == 2
      insertion = Rules.fetch(self.join)
      seq = [self[0], insertion, self[1]]
      if times == 1
        seq
      elsif times > 1
        seq.update(times-1)
      else
        raise RuntimeError
      end
    else
      result = self[0..1].update(times)[0..-2] + self[1..].update(times)
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

sequence = sequence.update(10)
p sequence.max_minus_min
