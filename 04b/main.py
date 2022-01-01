with open('input.txt', 'rt') as f:
    draws = (int(x) for x in f.readline().split(','))
    boards = [b.strip() for b in f.read().split('\n\n')]

class Board:
    
    def __init__(self, nums: str):
        self.marks = [[False for _ in range(5)] for _ in range(5)]
        self.nums = [[int(n) for n in row.split()] for row in nums.split('\n')]

    def is_winner(self):
        # Rows
        if any(all(row) for row in self.marks):
            return True
        # Cols
        if any(all(row[i] for row in self.marks) for i in range(5)):
            return True
        return False

    def mark(self, num):
        # This is uuuuugly
        for i in range(5):
            for j in range(5):
                if self.nums[i][j] == num:
                    self.marks[i][j] = True

    def unmarked_sum(self):
        sum_ = 0
        for i in range(5):
            for j in range(5):
                if not self.marks[i][j]:
                    sum_ += self.nums[i][j]
        return sum_


boards = [Board(b) for b in boards]

def main():
    global boards
    for draw in draws:
        new_boards = []
        for board in boards:
            board.mark(draw)
            if not board.is_winner():
                new_boards.append(board)
            else:
                if len(boards) == 1:
                    winner = boards[0]
                    unmarked_sum = winner.unmarked_sum()
                    result = unmarked_sum * draw
                    return result
        boards = new_boards
            
result = main()
print(result)
