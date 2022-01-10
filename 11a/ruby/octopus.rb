module Octopus
  class Grid
    attr_reader :nrows, :ncols

    def initialize(vals)
      @values = vals
      @nrows = vals.length
      @ncols = vals[0].length
    end
    def to_s
      @values.map{|row| row.join("")}.join("\n")
    end
    def [](idx)
      x, y = idx
      @values[y][x]
    end
    def adjacent_to(idx)
      x0, y0 = idx
      adj = (-1..1).map{|i| (-1..1).map{|j| [x0+i, y0+j]}}.flatten(1)
      adj = adj.select{|x, y| x.between?(0, @ncols) and y.between?(0, @nrows)}
      adj.reject{|x, y| x == x0 and y == y0}
    end

    private
    def []=(idx, val)
      x, y = idx
      @values[y][x] = val
    end
  end
end
