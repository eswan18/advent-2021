require "set"

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
    def real_digit(glyph)
      real_glyph = glyph.map{|seg| true_seg(seg)}
      mapping = {
        0 => "abcefg",
        1 => "cf",
        2 => "acdeg",
        3 => "acdfg",
        4 => "bcdf",
        5 => "abdfg",
        6 => "abdefg",
        7 => "acf",
        8 => "abcdefg",
        9 => "abcdfg"
      }
      mapping.key(real_glyph.sort.join(""))
    end
    def proper_output
      determine_digits
      @output_glyphs.map{|g| real_digit(g)}.join("").to_i
    end
    def determine_digits
      # Start by identifying 1, 4, 7, and 8
      one = @unknown_glyphs.select{|g| candidate_digits(g) == [1]}.first
      four = @unknown_glyphs.select{|g| candidate_digits(g) == [4]}.first
      seven = @unknown_glyphs.select{|g| candidate_digits(g) == [7]}.first
      eight = @unknown_glyphs.select{|g| candidate_digits(g) == [8]}.first
      # Segment A is whichever is in 1 but not 7.
      a_seg = Set.new(seven).difference(Set.new(one)).first
      add_correspondence(a_seg, "a")
      # Whichever segment is in 4 but not 1 AND is present in 0, 6, and 9 is B.
      in_4_not_1 = Set.new(four).difference(Set.new(one))
      glyphs_069 = @unknown_glyphs.select{|g| g.length == 6}
      in_069 = glyphs_069.map{|g| Set.new(g)}.reduce{|x, y| x.intersection(y)}
      b_seg = in_4_not_1.intersection(in_069).first
      add_correspondence(b_seg, "b")
      # The other segment that is in 4 but not 1 is D.
      d_seg = in_4_not_1.difference(Set[b_seg]).first
      add_correspondence(d_seg, "d")
      # The segment in 1 and also in all of 0, 6, 9 is F.
      f_seg = in_069.intersection(Set.new(one)).first
      add_correspondence(f_seg, "f")
      # The other segment in one is C.
      c_seg = Set.new(one).difference(Set[f_seg]).first
      add_correspondence(c_seg, "c")
      # The digit of 069 that has all of abcdf is 9
      nine = glyphs_069.select do |g|
        Set.new(g).intersection(Set[a_seg, b_seg, c_seg, d_seg, f_seg]).length == 5
      end
      nine = nine.first
      # The segment in nine that we haven't seen yet is G.
      g_seg = Set.new(nine).difference(Set[a_seg, b_seg, c_seg, d_seg, f_seg]).first
      add_correspondence(g_seg, "g")
      # The segment we haven't seen yet is E.
      all_seen = Set[a_seg, b_seg, c_seg, d_seg, f_seg, g_seg]
      e_seg = Set.new(eight).difference(all_seen).first
      add_correspondence(e_seg, "e")
    end
  end

end
