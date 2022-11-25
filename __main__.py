from src.pattern import Patterns
from src.board import Board

def run():
    # patterns = Patterns().get_patterns(20)
    board = Board(50, 50)
    # board.populate(patterns)
    board.simulate()

if __name__ == '__main__':
    run()
