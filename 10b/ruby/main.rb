FILENAME = "input.txt"
fh = File.open(FILENAME)
lines = fh.readlines.map(&:chomp)

PAIRS = {
  '(' => ')',
  '{' => '}',
  '[' => ']',
  '<' => '>',
}
PAIRS_INVERTED = PAIRS.invert

class MismatchError < RuntimeError
end
def autocomplete(line)
  stack = []
  line.each_char do |c|
    if PAIRS.has_key? c
      stack << c
    else
      if (s = stack.pop) != PAIRS_INVERTED[c]
        raise MismatchError
      end
    end
  end
  stack.reverse.map{|c| PAIRS[c]}
end
def score(line)
  begin
    chars = autocomplete(line)
  rescue MismatchError
    return 0
  end
  pts = 0
  chars.each do |c|
    pts *= 5
    case c
    when ")"
      pts += 1
    when "]"
      pts += 2
    when "}"
      pts += 3
    when ">"
      pts += 4
    end
  end
  pts
end

scores = lines.map{|l| score(l)}.select{|s| s > 0}.sort
middle = scores[(scores.size - 1) / 2]
p middle
