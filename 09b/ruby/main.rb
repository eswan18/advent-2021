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
  def neighbors(x, y)
    [[x+1, y], [x-1, y], [x, y+1], [x, y-1]].select{|x, y| x >= 0 and y >= 0}
  end
  def neighbor_heights(x, y)
    [self[x+1, y], self[x-1, y], self[x, y+1], self[x, y-1]].compact
  end
  def low_pts
    pts = []
    @nums.each_with_index do |row, i|
      row.each_with_index do |elem, j|
        heights = neighbor_heights(i, j)
        if heights.map{|h| h > elem}.all?
          pts << [i, j]
        end
      end
    end
    pts
  end
  def basin_from_pts(pts)
    new_pts = []
    pts.each do |x, y|
      nbs = neighbors(x, y).select{|x, y| self[x, y] and self[x, y] < 9}
      new_pts += nbs.reject{|nb| pts.include?(nb) or new_pts.include?(nb)}
    end
    if new_pts.size > 0
      basin_from_pts(pts + new_pts)
    else
      pts
    end
  end
  def basins
    low_pts.map{|pt| basin_from_pts([pt])}
  end
  def [](x, y)
    if x < 0 or y < 0
      nil
    end
    begin
      @nums[x][y]
    rescue NoMethodError
      nil
    end
  end
end
map = Map.from_string(File.open(FILENAME).read)

p map.basins.map(&:size).sort.last(3).reduce{|x, y| x * y}
