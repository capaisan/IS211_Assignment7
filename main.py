import random


class Die:
    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_score = 0

    def reset_turn_score(self):
        self.turn_score = 0

    def roll(self, current_player, next_player):
        roll = Die().roll()
        if roll == 1:
            print(f"Unfortunate! {current_player.name} rolled a 1. {next_player.name}'s turn.")
            self.reset_turn_score()
            return 0
        else:
            self.turn_score += roll
            print(f"{self.name} rolled a {roll} (This turns total: {self.turn_score}, Total Score: {self.score})")
            return self.turn_score

    def hold(self):
        self.score += self.turn_score
        print(f"{self.name} holds. (Turn Total: {self.turn_score}, Total Score: {self.score})")
        self.reset_turn_score()


def play_game():
    random.seed(0)  # set random seed for consistency
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    current_player = player1
    next_player = player2

    while player1.score < 100 and player2.score < 100:
        print(f"\n{current_player.name}'s turn.")
        decision = input("Enter 'r' to roll or 'h' to hold: ")
        while decision not in ['r', 'h']:
            print("Enter 'r' to roll and 'h' to hold: ")
            decision = input()

        if decision == 'r':
            current_player.roll(current_player, next_player)
        else:
            current_player.hold()
            if current_player == player1:
                current_player = player2
                next_player = player1
            else:
                current_player = player1
                next_player = player2

    print(f"\nGAME OVER\n{current_player.name} WINS with a score of {current_player.score}!"
          f"\n{next_player.name} came in a close second with a score of {next_player.score}!")

def main():
    play_game()

if __name__ == "__main__":
    main()