require_relative "bingo_board"

FILENAME = "test_input.txt"
file = File.open(FILENAME)
lines = file.readlines.map(&:chomp)
draws, _, *boards = lines

boards = boards.join("\n").split("\n\n").map{|x| x.split("\n")}
boards = boards.map { |lines| BingoBoard.new(lines) }
puts boards[0]
