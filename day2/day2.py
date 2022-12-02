import sys


OPPONENT_MAP = {
    'A': 1,
    'B': 2,
    'C': 3
}

PLAYER_MAP = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

PLAYER_WINS = {
    'A Y': 8,
    'C X': 7,
    'B Z': 9
}

OPPONENT_WINS = {
    'A Z': 3,
    'B X': 1,
    'C Y': 2
}

DRAWS = {
    'A X': 4,
    'B Y': 5,
    'C Z': 6
}

class RPSGame:

    def __init__(self, rounds: list) -> None:
        self.__rounds = rounds
        self.__score = []
    
    @property
    def score(self):
        return sum(self.__score)
    
    def _do_round1(self, round: str):
        if round in PLAYER_WINS.keys():
            self.__score.append(PLAYER_WINS[round])
        elif round in OPPONENT_WINS.keys():
            self.__score.append(OPPONENT_WINS[round])
        elif round in DRAWS.keys():
            self.__score.append(DRAWS[round])
        else:
            raise Exception(f"invalid round: {round}")

    def play1(self):
        for round in self.__rounds:
            self._do_round1(round)
        print(f"score:{self.score}")

    def _do_round2(self, round):
        if round[2] == 'X':
            scores_map = OPPONENT_WINS
        elif round[2] == 'Y':
            scores_map = DRAWS
        elif round[2] == 'Z':
            scores_map = PLAYER_WINS
        else:
            raise Exception(f"invalid round: {round}")
        
        for k in scores_map.keys():
            if round[0] in k:
                self.__score.append(scores_map[k])
    
    def play2(self):
        for round in self.__rounds:
            self._do_round2(round)
        print(f"score:{self.score}")

def part1(input_data):
    RPSGame(input_data).play1()

def part2(input_data):
    RPSGame(input_data).play2()

def main():
    input_data = [ x.strip() for x in open(sys.argv[1], 'r') ]
    part1(input_data)
    part2(input_data)

if __name__ == '__main__':
    main()