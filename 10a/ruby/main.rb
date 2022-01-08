FILENAME = "input.txt"
fh = File.open(FILENAME)
lines = fh.readlines

PAIRS = {
  '(' => ')',
  '{' => '}',
  '[' => ']',
  '<' => '>',
}
PAIRS_INVERTED = PAIRS.invert

class MismatchError < RuntimeError
end
def parse(line)
  stack = []
  line.each_char do |c|
    if PAIRS.has_key? c
      stack << c
    else
      if stack.pop != PAIRS_INVERTED[c]
        case c
        when ")"
          return 3
        when "]"
          return 57
        when "}"
          return 1197
        when ">"
          return 25137
        end
      end
    end
  end
  false
end

p lines.map{|l| parse(l)}.select{|s| s}.sum
