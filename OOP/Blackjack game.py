from enum import Enum
from random import shuffle
from typing import List
class Suit(Enum): CLUBS = 'clubs'; DIAMOND = "Diamonds"; HEART = "Hearts"; SPADE = "Spades"
class Card():
    def __init__(self, num_idx, suit): self.num_idx = num_idx; self.suit = suit # idx 1 Indexed
    def get_val(self):
        if self.num_idx >= 10: return 10
        return self.num_idx
    def is_ace(self): return self.num_idx == 1
    def __str__(self): return [" ", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][self.num_idx] + f" of {self.suit.value}"
class Cards():
    def __init__(self): self.cards = self.get_cards(); self.shuffle()
    def get_cards(self): return [Card(num_idx, suit) for num_idx in range(1, 14) for suit in [Suit.CLUBS, Suit.DIAMOND, Suit.HEART, Suit.SPADE]]
    def shuffle(self): shuffle(self.cards)
    def get_card(self): return self.cards.pop() if self.cards else None
class Hand():
    def __init__(self): self.cards: List[Card] = []
    def add_card(self, card): self.cards.append(card)
    def get_tot_val(self):  
        mn = mx = 0
        for card in self.cards:
            mn += card.get_val()
            mx += 11 if card.is_ace() else card.get_val()  
        return mn if mx > 21 else mx
    def busted(self): return self.get_tot_val() > 21
    def is_blackjack(self): return len(self.cards) == 2 and self.get_tot_val() == 21
    def __str__(self): return ", ".join(str(card) for card in self.cards)
class Player:
    def __init__(self, name): self.name = name; self.hand = Hand() 
    def __str__(self): return f"{self.name}'s hand: {self.hand} (Score: {self.hand.get_tot_val()})"
class Dealer(Player):
    def should_hit(self): return self.hand.get_tot_val() < 17 
class BlackjackGame:
    def __init__(self, name: str):
        self.cards = Cards(); self.player = Player(name); self.dealer = Dealer("Dealer")
    def deal_initial(self):
        for _ in range(2):
            self.player.hand.add_card(self.cards.get_card())
            self.dealer.hand.add_card(self.cards.get_card())
    def player_turn(self):
        while not self.player.hand.busted():
            action = input("Hit or Stand? ").strip().lower()
            if action == "hit": self.player.hand.add_card(self.cards.get_card())
            elif action == "stand": break
            else: print("Invalid input. Please type 'Hit' or 'Stand'.") 
            print(self.player)
    def dealer_turn(self):
        print("\n-- Dealer's Turn --")
        while self.dealer.should_hit(): 
            self.dealer.hand.add_card(self.cards.get_card())
            print(self.dealer)
    def determine_winner(self):
        if self.player.hand.busted(): return "Dealer wins! Player busted."
        if self.dealer.hand.busted(): return "Player wins! Dealer busted."
        if self.player.hand.get_tot_val() > self.dealer.hand.get_tot_val(): return "Player wins!"
        if self.player.hand.get_tot_val() < self.dealer.hand.get_tot_val(): return "Dealer wins!"
        return "It's a draw!"

    def play(self):
        self.deal_initial(); print("==========\nInitial Hands"); print(self.player); print(f"Dealer's visible card: {self.dealer.hand.cards[1]}")
        self.player_turn()
        if not self.player.hand.busted(): self.dealer_turn() 
        print("==========\nFinal Hands"); print(self.player); print(self.dealer)
        print("==========\nResult"); print(self.determine_winner())

# Main Execution
if __name__ == "__main__":
    name = input("Enter your name: ")
    game = BlackjackGame(name)
    game.play()
