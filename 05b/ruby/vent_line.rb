class VentLine
  attr_reader :coord1, :coord2

  def initialize(coord1, coord2)
    if coord1[0] < coord2[0] or (coord1[0] == coord2[0] and coord1[1] < coord2[1])
      @coord1 = coord1
      @coord2 = coord2
    else
      @coord1 = coord2
      @coord2 = coord1
    end
  end

  def is_horizontal?
    coord1[1] == coord2[1]
  end

  def is_vertical?
    coord1[0] == coord2[0]
  end

  def is_diagonal?
    not (is_horizontal? or is_vertical?)
  end

  def is_pos_diag?
    is_diagonal? and @coord1[1] < @coord2[1]
  end

  def is_neg_diag?
    is_diagonal? and @coord1[1] > @coord2[1]
  end

  def covered
    pts = []
    x, y = coord1
    if is_vertical?
      while y <= coord2[1]
        pts << [x, y]
        y += 1
      end
    elsif is_horizontal?
      while x <= coord2[0]
        pts << [x, y]
        x += 1
      end
    elsif is_pos_diag?
      while x <= coord2[0]
        pts << [x, y]
        x += 1
        y += 1
      end
    elsif is_neg_diag?
      while x <= coord2[0]
        pts << [x, y]
        x += 1
        y -= 1
      end
    end
    pts
  end

  def to_s
    "#{coord1}, #{coord2}"
  end
end
