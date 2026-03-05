import argparse
from easyAI.games.ConnectFour import ConnectFour
from easyAI import TwoPlayerGame, Negamax, SSS, AI_Player

def parse_args():
    parser = argparse.ArgumentParser(
                    prog='',
                    description='Which game you want to play')
    
    parser.add_argument(
        "--game", type=str, default="connectFour"
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    game: str = args.game

    ai_algo_neg = Negamax(5)
    ai_algo_sss = SSS(5)

    match game:
        case "connectFour":
            game: TwoPlayerGame = ConnectFour([AI_Player(ai_algo_neg), AI_Player(ai_algo_sss)])

    game.play()
    if game.lose():
        print("Player %d wins." % (game.opponent_index))
    else:
        print("Looks like we have a draw.")

    