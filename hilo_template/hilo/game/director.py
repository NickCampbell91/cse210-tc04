from game.dealer import Dealer

class Director:

    def __init__(self):
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()
        self.current_card = 0

    def start_game(self):
        while self.keep_playing:
            #self.get_inputs()
            #self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        self.dealer.deal_card()

    def do_updates(self):
        points = self.dealer.get_points()
        self.score += points

    def do_outputs(self):
        if len(self.dealer.cards) == 13:
            self.current_card = self.dealer.deal_card()
        print(f"The card is: {self.current_card}")
        if self.dealer.can_deal() and self.score != 0:
            choice = input("Higher or lower? [h/l] ")
            new_card = self.dealer.deal_card()
            if (choice == "h" and new_card > self.current_card) or (choice == "l" and new_card < self.current_card):
                self.score += 100
            elif (choice == "h" and new_card < self.current_card) or (choice == "l" and new_card > self.current_card):
                self.score -= 75
            else:
                print("That wasn't an option. You lose 200 points.")
                self.score -= 200
            print(f"Next card was: {new_card}")
            print(f"Your score is: {self.score}")
            self.current_card = new_card
            play_more = input("Draw again? [y/n] ")
            self.keep_playing = (play_more == "y")
        else:
            self.keep_playing = False