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
  def is_upper?
    self == self.upcase
  end
end

def get_paths(current_path, seen, can_revisit=true)
  current_cave = current_path[-1]
  if current_cave == "end"
    return [current_path]
  end
  # Rule out caves that are small and already-seen
  available_caves = Paths[current_cave].reject{|cave| cave == "start"}.select do |cave|
    cave.is_upper? or can_revisit or (cave.is_lower? and not seen.include?(cave))
  end
  paths = available_caves.map do |cave|
    if cave.is_lower?
      if seen.include?(cave)
        new_path = current_path + [cave]
        get_paths(new_path, seen, false)
      else
        new_seen = seen + Set[cave]
        new_path = current_path + [cave]
        get_paths(new_path, new_seen, can_revisit)
      end
    else
      get_paths(current_path + [cave], seen, can_revisit)
    end
  end
  paths.flatten 1
end

paths = get_paths(["start"], Set["start"]).uniq
p paths.length
