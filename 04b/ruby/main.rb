require_relative "bingo_board"

FILENAME = "input.txt"
file = File.open(FILENAME)
lines = file.readlines.map(&:chomp)
draws, _, *boards = lines

draws = draws.split(",").map(&:to_i)

boards = boards.join("\n").split("\n\n").map{|x| x.split("\n")}
boards = boards.map { |lines| BingoBoard.new(lines) }

def get_loser_score(boards, draws)
  draws.each do |draw|
    boards.each{ |b| b.mark(draw) }
    if boards.length > 1
      boards.reject!(&:wins?)
    else
      # When there's just one board left.
      if boards[0].wins?
        return boards[0].unmarked.sum * draw
      end
    end
    nil
  end
end

puts get_loser_score(boards, draws)
