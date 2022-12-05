from enum import Enum

with open('input_2.txt') as input:
    games = input.read().split("\n")

class PlayEnum(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

elf_dict = {
  "A": PlayEnum.ROCK,
  "B": PlayEnum.PAPER,
  "C": PlayEnum.SCISSORS
}

my_dict = {
  "X": PlayEnum.ROCK,
  "Y": PlayEnum.PAPER,
  "Z": PlayEnum.SCISSORS
}

def play_game(elf_play: PlayEnum, my_play: PlayEnum):
     # outcome of the round = 0 if you lost, 3 if the round was a draw, and 6 if you won
     if elf_play.value == my_play.value:
         outcome = 3
     elif (my_play.value + 1) % 3 == elf_play.value % 3:
         outcome = 0
     else:
         outcome = 6
     # score for a round is the score for the shape you selected
     # plus the score for the outcome
     return my_play.value + outcome

all_scores = []

for game in games:
    raw_play = game.split(" ")
    elf_play = elf_dict[raw_play[0]]
    my_play = my_dict[raw_play[1]]

    game_score = play_game(elf_play, my_play)

    all_scores.append(game_score)
exit

print(sum(all_scores))

# part 2

class GameResult(Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"

def get_my_play(elf_play: PlayEnum, outcome: GameResult):
     # draw
     if outcome == GameResult.DRAW:
        return elf_play
    # win
    # there must be a better way to do this???
     elif outcome == GameResult.LOSE:
        if elf_play == PlayEnum.PAPER:
            return PlayEnum.ROCK
        elif elf_play == PlayEnum.SCISSORS:
            return PlayEnum.PAPER
        elif elf_play == PlayEnum.ROCK:
            return PlayEnum.SCISSORS

    # lose
     elif outcome == GameResult.WIN:
        if elf_play == PlayEnum.PAPER:
            return PlayEnum.SCISSORS
        elif elf_play == PlayEnum.SCISSORS:
            return PlayEnum.ROCK
        elif elf_play == PlayEnum.ROCK:
            return PlayEnum.PAPER

all_scores_2 = []

for game in games:
    raw_play = game.split(" ")
    elf_play = elf_dict[raw_play[0]]

    my_play = get_my_play(elf_play, GameResult(raw_play[1]))

    game_score = play_game(elf_play, my_play)

    all_scores_2.append(game_score)
exit

print(sum(all_scores_2))