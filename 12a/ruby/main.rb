require "Set"

FILENAME = "input.txt"

lines = File.open(FILENAME).readlines.map(&:chomp)
Paths = {}

lines.each do |line|
  a, b = line.split("-")
  # Add links from a to b and b to a
  Paths[a] = [] unless Paths.has_key? a
  Paths[a] << b
  Paths[b] = [] unless Paths.has_key? b
  Paths[b] << a
end

class String
  def is_lower?
    self == self.downcase
  end
end

def get_paths(current_path, seen)
  current_cave = current_path[-1]
  if current_cave == "end"
    return [current_path]
  end
  # Rule out caves that are small and already-seen
  available_caves = Paths[current_cave].reject do |cave|
    cave.is_lower? and seen.include?(cave)
  end
  paths = available_caves.map do |cave|
    get_paths(current_path + [cave], seen + Set[cave])
  end
  paths.flatten 1
end

paths = get_paths(["start"], Set["start"])
p paths.size
