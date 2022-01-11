require_relative "digits"

FILENAME = "input.txt"

displays = File.open(FILENAME).readlines.map{|line| Digits::Display.from_string(line)}

counter = 0
displays.each do |display|
  display.output_glyphs.each do |glyph|
    counter += 1 if display.candidate_digits(glyph).length == 1
  end
end

p counter
