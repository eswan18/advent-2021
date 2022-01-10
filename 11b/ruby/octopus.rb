module Octopus
  class Grid
    attr_reader :nrows, :ncols, :flashes

    def initialize(vals)
      @values = vals
      @nrows = vals.length
      @ncols = vals[0].length
    end
    def to_s
      @values.map{|row| row.join("")}.join("\n")
    end
    def [](*idx)
      x, y = idx
      @values[y][x]
    end
    def adjacent_to(idx)
      x0, y0 = idx
      adj = (-1..1).map{|i| (-1..1).map{|j| [x0+i, y0+j]}}.flatten(1)
      adj = adj.select do |x, y|
        x.between?(0, @ncols-1) and y.between?(0, @nrows-1)
      end
      adj.reject{|x, y| x == x0 and y == y0}
    end
    def increment(value=1)
      @values = @values.map{|row| row.map{|x| x + 1}}
      self
    end
    def flash
      flashers = []
      new_flashers = []
      # Keep going until there are no new flashers
      loop do
        (0..@ncols-1).each do |x|
          (0..@nrows-1).each do |y|
            idx = [x, y]
            if self[*idx] > 9
              # Only deal with octopi who haven't flashed yet this turn.
              if not (flashers.include?(idx) or new_flashers.include?(idx))
                new_flashers << idx
                adjacent_to(idx).each{|adj_idx| self[*adj_idx] += 1}
              end
            end
          end
        end
        # If we haven't found any new flashers, the board is done flashing.
        if new_flashers.empty?
          break
        end
        flashers += new_flashers
        new_flashers = []
      end
      flashers
    end
    def turn
      increment
      flashers = flash
      # Reset the flashers to 0.
      flashers.each{|x, y| self[x, y] = 0}
      if flashers.length == @nrows * @ncols
        true
      else
        false
      end
    end

    private
    def []=(*idx, val)
      x, y = idx
      @values[y][x] = val
    end
  end
end
