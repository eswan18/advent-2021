require_relative "bingo_board"

FILENAME = "input.txt"
file = File.open(FILENAME)
lines = file.readlines.map(&:chomp)
draws, _, *boards = lines

draws = draws.split(",").map(&:to_i)

boards = boards.join("\n").split("\n\n").map{|x| x.split("\n")}
boards = boards.map { |lines| BingoBoard.new(lines) }

def get_winner_score(boards, draws)
  draws.each do |draw|
    boards.each{ |b| b.mark(draw) }
    winners = boards.select(&:wins?)
    # Assume there's just one winner
    if winners.length > 0
      return winners[0].unmarked.sum * draw
    end
    nil
  end
end

puts get_winner_score(boards, draws)
