FILENAME = "test_input.txt"
f = File.open(FILENAME)
fish_raw = f.read.split(',').map(&:to_i)

DAYS = 256

# Initialize hash storing fish counts.
fish = {}
9.times do |i|
  fish[i] = fish_raw.count(i)
end

def tick(fish)
  new_fish = {}
  new_fish[8] = fish[0]
  (1..8).each do |i|
    new_fish[i-1] = fish[i] or 0
  end
  new_fish[6] += fish[0]
  new_fish
end

DAYS.times { fish = tick(fish) }

p fish.each_value.sum
