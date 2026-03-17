import argparse
from easyAI.games import ConnectFour
from easyAI import TwoPlayerGame, Negamax, SSS, AI_Player
import statistics

def parse_args():
    parser = argparse.ArgumentParser(
                    prog='',
                    description='Which game you want to play')
    
    parser.add_argument(
        "--game", type=str, default="connectFour"
    )
    parser.add_argument(
        "--randomised", type=bool, default=False
    )
    parser.add_argument(
        "--first_algo", type=str, default="negamax"
    )
    parser.add_argument(
        "--second_algo", type=str, default="negamax"
    )
    parser.add_argument(
        "--depth", type=int, default=5
    )
    parser.add_argument(
        "--n_runs", type=int, default=100
    )
    parser.add_argument(
        "--probabilistic", type=bool, default=False
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    game: str = args.game
    radomised: bool = args.randomised
    first_algo: str = args.first_algo
    second_algo: str = args.second_algo
    depth: int = args.depth
    n_runs: int = args.n_runs
    probabilistic: bool = args.probabilistic

    match first_algo:
        case "negamax":
            first_ai = Negamax(depth)
        case "alphabeta":
            pass

    match second_algo:
        case "negamax":
            second_ai = Negamax(depth)
        case "alphabeta":
            pass

    first_player = AI_Player(first_ai)
    second_player = AI_Player(second_ai)

    match game:
        case "connectFour":
            game: TwoPlayerGame = ConnectFour([first_player, second_player], randflag=probabilistic)

    first_counter: int = 0
    second_counter: int = 0
    starting_player= game.current_player_index

    for i in range(n_runs):
        print(f"Run number {i}")
        game.play()
        if game.lose():
            print("Player %d wins." % (game.opponent_index))
            if game.opponent_index == starting_player:
                first_counter += 1
            else:
                second_counter += 1
        else:
            print("Looks like we have a draw.")

        game.restart()

    print(f"Mean time of first player {statistics.mean(first_player.avg_times)}")
    print(f"Mean time of second player {statistics.mean(second_player.avg_times)}")

    print(f"First player has won {first_counter} times")
    print(f"Second player has won {second_counter} times")
    print(f"There have been {n_runs - first_counter - second_counter} draws")

    