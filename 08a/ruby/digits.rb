module Digits
  class Digit
    def initialize(segments)
      # segments should be a string or array of segment chars.
      if segments.class == String
        segments = segments.split("")
      end
      @segments = segments.sort
    end
    def matches?(segments)
      segments.sort == @segments
    end
    def length
      segments.length
    end
  end

  def self.segments
    {
      0 => Digit.new("abcefg"),
      1 => Digit.new("cf"),
      2 => Digit.new("acdeg"),
      3 => Digit.new("acdfg"),
      4 => Digit.new("bcdf"),
      5 => Digit.new("abdfg"),
      6 => Digit.new("abdefg"),
      7 => Digit.new("acf"),
      8 => Digit.new("abcdefg"),
      9 => Digit.new("abcdfg")
    }
  end

  class Display
    attr_reader :correspondence, :output_glyphs
    attr_accessor :seen_digits
    def initialize(unknown_glyphs, output_glyphs)
      @seen_digits = []
      @correspondence = {}
      @unknown_glyphs = unknown_glyphs
      @output_glyphs = output_glyphs
    end
    def add_correspondence(shown, actual)
      if @correspondence.has_key?(shown) or @correspondence.has_value?(actual)
        msg = "shown: #{shown} or actual: #{actual} is already in correspondence"
        raise RuntimeError.new msg
      end
      @correspondence[shown] = actual
    end
    def true_seg(seg)
      @correspondence[seg]
    end
    def shown_as(seg)
      @correspondence.key(seg)
    end
    def candidate_digits(segs)
      if segs.length == 2
        [1]
      elsif segs.length == 4
        [4]
      elsif segs.length == 3
        [7]
      elsif segs.length == 7
        [8]
      # build out more logic in the next two elsifs
      elsif segs.length == 5
        [2, 3, 5]
      elsif segs.length == 6
        [0, 6, 9]
      else
        raise RuntimeError.new "Unknown digit"
      end 
    end
    def self.from_string(s)
      signal, output = s.split("|").map{|x| x.split(" ").map{|y| y.split("")}}
      self.new(signal, output)
    end
  end

end
