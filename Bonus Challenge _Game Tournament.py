from abc import ABC, abstractmethod

# Abstract Base Class
class Player(ABC):

    def __init__(self, name):
        self.name = name
        self.score = 0

    @abstractmethod
    def play_round(self, difficulty):
        pass

    def is_eliminated(self):
        return self.score < 0


# Child Class 1: Attacker
class Attacker(Player):

    def play_round(self, difficulty):
        if difficulty <= 5:
            self.score += 10
        else:
            self.score -= 5


# Child Class 2: Defender
class Defender(Player):

    def play_round(self, difficulty):
        if difficulty <= 7:
            self.score += 5
        else:
            self.score -= 3


if __name__ == '__main__':
    players = [
        Attacker("Ali"),
        Attacker("Sara"),
        Defender("Omar"),
        Defender("Mona"),
    ]

    rounds = [3, 6, 8, 4]

    for diff in rounds:
        for p in players:
            if not p.is_eliminated():
                p.play_round(diff)

    # Filter out eliminated players
    alive_players = list(filter(lambda p: not p.is_eliminated(), players))
    eliminated_count = len(players) - len(alive_players)

    # Sort alive players by score (highest first)
    ranked_players = sorted(
        alive_players, key=lambda p: p.score, reverse=True)

    print("--- Final Ranking ---")
    rank = 1
    for p in ranked_players:
        role = p.__class__.__name__  # Gets 'Attacker' or 'Defender'
        print(f"{rank}. {p.name} ({role}) = {p.score}")
        rank += 1

    print(f"Alive: {len(alive_players)} | Eliminated: {eliminated_count}")