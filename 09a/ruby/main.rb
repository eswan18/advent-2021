FILENAME = "input.txt"

class Map
  def initialize(nums)
    @nums = nums
  end
  def Map.from_string(s)
    self.new(s.split("\n").map{|line| line.chars.map(&:to_i)})
  end
  def to_s
    @nums.map{|row| row.join("")}.join("\n")
  end
  def neighbor_heights(x, y)
    [self[x+1, y], self[x-1, y], self[x, y+1], self[x, y-1]].compact
  end
  def sum_risk
    risk = 0
    @nums.each_with_index do |row, i|
      row.each_with_index do |elem, j|
        heights = neighbor_heights(i, j)
        if heights.map{|h| h > elem}.all?
          risk += (elem + 1)
        end
      end
    end
    risk
  end
  def [](x, y)
    begin
      @nums[x][y]
    rescue NoMethodError
      nil
    end
  end
end
map = Map.from_string(File.open(FILENAME).read)

p map.sum_risk
