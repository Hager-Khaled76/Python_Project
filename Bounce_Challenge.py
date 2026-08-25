# Bounce Challenge: ScoreBoard System

# 1. Decorator for counting method calls
def call_counter(func):

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


# 2. ScoreBoard Iterator Class
class ScoreBoard:

    def __init__(self):
        self.players = []
        self.index = 0

    @call_counter
    def add_player(self, name, score):
        self.players.append({"name": name, "score": score})

    def __iter__(self):
        # Sort players descending by score when iteration starts
        self.players = sorted(
            self.players, key=lambda x: x["score"], reverse=True
        )
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.players):
            player = self.players[self.index]
            rank = self.index + 1
            self.index += 1
            return f"{rank}. {player['name']} = {player['score']}"
        else:
            raise StopIteration


if __name__ == '__main__':
    board = ScoreBoard()

    # Add players
    board.add_player("Ali", 70)
    board.add_player("Sara", 95)
    board.add_player("Omar", 85)

    # Print Header and Loop through ScoreBoard
    print("--- Score Board ---")
    for entry in board:
        print(entry)

    # Print total calls using the decorator attribute
    print(f"add_player called {board.add_player.count} times")