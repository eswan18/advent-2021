class BingoBoard
  def initialize(lines)
    @rows = lines.map { |line| line.split(" ").map(&:to_i) }
  end
  def to_s
    return @rows.map{ |line| line.join(" ") }.join("\n")
  end
end
