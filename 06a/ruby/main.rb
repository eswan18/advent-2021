FILENAME = "input.txt"
f = File.open(FILENAME)
fish = f.read.split(',').map(&:to_i)

DAYS = 80

$new_fish = 0

def tick(timer)
  if timer == 0
    $new_fish += 1
    6
  else
    timer - 1
  end
end

DAYS.times do
  $new_fish = 0
  fish = fish.map{ |x| tick(x) }
  fish += Array.new($new_fish, 8)
end

p fish.size
