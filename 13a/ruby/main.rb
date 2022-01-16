FILENAME = "input.txt"

# Parse
lines = File.open(FILENAME).readlines.map(&:chomp)
folds, dots = lines.partition{|line| line.start_with? ("fold along")}
dots = dots.select{|line| line.length > 0}.map{|line| line.split(",").map(&:to_i)}
folds = folds.map do |line|
  axis, coord = line.delete_prefix("fold along ").split("=")
  coord = coord.to_i
  [axis, coord]
end

# Fold
def fold(axis:, coord:, dots:)
  if axis == "x"
    index = 0
  else
    index = 1
  end
  # Dots that are on the fold will be obliterated by folding.
  dots = dots.reject{|dot| dot[index] == coord}
  dots.map do |dot|
    if dot[index] < coord
      dot
    else
      new_dot = dot.clone
      new_dot[index] = 2 * coord - new_dot[index]
      new_dot
    end
  end
end

def print_dots(dots)
  board_width = dots.map{|d| d[0]}.max
  board_height = dots.map{|d| d[1]}.max
  s = ""
  (0..board_height).each do |y|
    (0..board_width).each do |x|
      if dots.include? [x, y]
        s << "#"
      else
        s << "."
      end
    end
    s << "\n"
  end
  s << "\n"
  puts s
end

folds.each do |axis, coord|
  dots = fold(axis: axis, coord: coord, dots: dots)
  # Dedup
  dots.uniq!
  # See how many dots are left
  p dots.length
  break
end

