from game import Game

def main():

    print("=================================")
    print("     TEXAS HOLD'EM CLI GAME      ")
    print("=================================")

    while True:

        game = Game()
        game.play_round()

        again = input("\nPlay another round? (y/n): ")

        if again.lower() != "y":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()