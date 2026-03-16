from deck import Deck
from player import Player
import random

class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player = Player("You", 1000)
        self.computer = Player("Computer", 1000)

        self.community_cards = []
        self.pot = 0
        self.bet_amount = 50


    # DEAL TWO CARDS
    def deal_hole_cards(self):

        for _ in range(2):
            self.player.receive_card(self.deck.deal())
            self.computer.receive_card(self.deck.deal())


    # FLOP
    def deal_flop(self):

        for _ in range(3):
            self.community_cards.append(self.deck.deal())


    # TURN
    def deal_turn(self):

        self.community_cards.append(self.deck.deal())


    # RIVER
    def deal_river(self):

        self.community_cards.append(self.deck.deal())


    # DISPLAY PLAYER CARDS
    def show_player_hand(self):

        print("\nYour Cards:")
        self.player.show_hand()


    # DISPLAY COMMUNITY CARDS
    def show_community_cards(self):

        print("\nCommunity Cards:")
        for card in self.community_cards:
            print(card)


    # SIMPLE BETTING
    def betting_round(self):

        print(f"\nCurrent Pot: {self.pot}")
        print("Choose an action:")
        print("1 - Check")
        print("2 - Call")
        print("3 - Fold")

        choice = input("Your move: ")

        if choice == "1":
            print("You checked.")

        elif choice == "2":
            print("You called.")
            self.player.chips -= self.bet_amount
            self.pot += self.bet_amount

        elif choice == "3":
            print("You folded. Computer wins the pot.")
            return False

        else:
            print("Invalid choice. Checking automatically.")

        # COMPUTER DECISION (simple AI)
        ai = random.choice(["check", "call"])

        if ai == "call":
            print("Computer calls.")
            self.computer.chips -= self.bet_amount
            self.pot += self.bet_amount
        else:
            print("Computer checks.")

        return True


    # VERY SIMPLE WINNER LOGIC
    def determine_winner(self):

        print("\nDetermining winner...")

        player_score = random.randint(1,100)
        computer_score = random.randint(1,100)

        if player_score > computer_score:
            print("🎉 You win the pot!")
            self.player.chips += self.pot

        elif computer_score > player_score:
            print("💻 Computer wins the pot!")
            self.computer.chips += self.pot

        else:
            print("It's a tie!")

        self.pot = 0


    # MAIN ROUND
    def play_round(self):

        print("\nStarting New Round")

        self.deal_hole_cards()

        self.show_player_hand()

        if not self.betting_round():
            return

        input("\nPress Enter for FLOP")
        self.deal_flop()
        self.show_community_cards()

        if not self.betting_round():
            return

        input("\nPress Enter for TURN")
        self.deal_turn()
        self.show_community_cards()

        if not self.betting_round():
            return

        input("\nPress Enter for RIVER")
        self.deal_river()
        self.show_community_cards()

        self.determine_winner()