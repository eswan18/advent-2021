class BingoBoard

  def initialize(lines)
    @rows = lines.map{ |line| line.split(" ").map(&:to_i) }
    # a bunch of spaces where numbers exist in the first array of arrays
    @marks = lines.map{ |line| line.split(" ").map{ |x| " " } }
  end

  def mark(num)
    if coords = coordinates_of(num)
      i, j = coords
      @marks[i][j] = "X"
    end
  end

  def marks
    @marks.map{ |line| line.join(" ")}.join("\n")
  end

  def to_s
    @rows.map{ |line| line.join(" ") }.join("\n")
  end

  def wins?
    wins_row? or wins_col?
  end

  def unmarked
    result = []
    @rows.each_with_index do |row, i|
      row.each_with_index do |elem, j|
        if @marks[i][j] != 'X'
          result << elem
        end
      end
    end
    result
  end

  private
  def coordinates_of(num)
    @rows.each_with_index do |subarray, i|
      j = subarray.index(num)
      return i, j if j
    end
    nil
  end

  def wins_row?
    @marks.map{ |line| line.map{ |x| x == "X"}.all?}.any?
  end

  def wins_col?
    cols = @marks.transpose
    cols.map{ |line| line.map{ |x| x == "X"}.all?}.any?
  end

end
