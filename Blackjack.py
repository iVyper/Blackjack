import random
import os

# Dictionary representing the deck of cards.
# Keys are card labels; values are their numerical values.
# For the Ace ('A'), both possible values are provided.
card_deck = {
    "A": [1, 11],
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "J": 10,
    "Q": 10,
    "K": 10,
}

game = True  # Global flag to control the main game loop.


def clear_terminal():
    """
    Clears the terminal screen.

    Uses 'cls' for Windows and 'clear' for Unix-based systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def shuffle_deck():
    """
    Creates and shuffles a deck of cards.

    The deck is built by adding four of each card type (to simulate four suits)
    and then shuffling the list randomly.

    Returns:
        list: A shuffled list representing the deck of cards.
    """
    deck = []
    for card in card_deck:
        # Each card appears 4 times (one for each suit)
        for _ in range(4):
            deck.append(card)
    random.shuffle(deck)
    return deck


def deal_card(deck):
    """
    Deals a card from the deck.

    Removes and returns the last card from the deck list.

    Args:
        deck (list): The deck of cards.

    Returns:
        str: The dealt card.
    """
    dealt_card = deck.pop()
    return dealt_card


def initial_deal(deck):
    """
    Deals the initial two cards to both the player and the dealer.

    Args:
        deck (list): The deck of cards.

    Returns:
        tuple: Two lists containing the player's cards and the dealer's cards.
    """
    player_hand = []
    dealer_hand = []
    for _ in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))
    return player_hand, dealer_hand


def a_in_hand(hand):
    """
    Counts the number of Aces in a given hand.

    Args:
        hand (list): List of card strings in the hand.

    Returns:
        int: The count of Aces in the hand.
    """
    count = 0
    for card in hand:
        if card == "A":
            count += 1
    return count


def card_total(hand):
    """
    Calculates the total value of a hand of cards.

    Aces are initially counted as 11. If the total exceeds 21 and there are Aces in the hand,
    each Ace's value is reduced by 10 until the total is 21 or below.

    Args:
        hand (list): List of card strings in the hand.

    Returns:
        int: The calculated total value of the hand.
    """
    total = 0
    ace_count = 0
    for card in hand:
        if card == "A":
            total += 11
            ace_count += 1
        else:
            total += card_deck[card]
    # Adjust for Aces if total value exceeds 21
    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1
    return total


def dealers_logic(dealer_total, dealer_cards, deck):
    """
    Executes the dealer's logic for hitting or standing.

    The dealer hits until the total is 17 or greater.
    Displays messages for each action taken.

    Args:
        dealer_total (int): The current total value of the dealer's hand.
        dealer_cards (list): The dealer's current hand of cards.
        deck (list): The deck of cards.

    Returns:
        int: The final total value of the dealer's hand.
    """
    while dealer_total < 17:
        print("The dealer will hit.")
        dealer_cards.append(deal_card(deck))
        dealer_total = card_total(dealer_cards)
        print(dealer_cards)
        print(f"The dealer's total is {dealer_total}")
    if dealer_total > 21:
        print("The dealer has busted.")
    else:
        print(f"The dealer will stand at {dealer_total}")
    return dealer_total


def main():
    """
    Main function to run the Blackjack game.

    Handles the game loop, including shuffling the deck, dealing initial cards,
    managing the player's turn, executing the dealer's logic, and determining the outcome.
    Prompts the user to play again at the end of each round.
    """
    global game

    print("Welcome to Blackjack!")

    while game:
        # Prepare a new shuffled deck and deal initial cards.
        deck = shuffle_deck()
        player, dealer = initial_deal(deck)

        # Show dealer's first card and player's full hand.
        print("Dealer's shown card:", dealer[0])
        print("Your hand:", player)

        players_total = 0
        dealers_total = 0
        players_turn = True

        # Player's turn loop: allow hit or stand.
        while players_turn:
            players_total = card_total(player)
            print(f"Your cards total: {players_total}")

            # Automatically end turn if player hits or reaches 21.
            if players_total >= 21:
                players_turn = False
            else:
                hit_or_stand = input("Would you like to hit or stand?\nEnter 'hit' or 'stand': ").lower()
                if hit_or_stand == "hit":
                    clear_terminal()
                    player.append(deal_card(deck))
                    print("Your hand:", player)
                elif hit_or_stand == "stand":
                    players_turn = False

        # If player busts, skip dealer's turn.
        if players_total > 21:
            print("You have busted.")
        else:
            dealers_total = card_total(dealer)
            print("Dealer's hand:", dealer)
            print(f"The dealer's total is: {dealers_total}")
            # Dealer takes actions based on game logic.
            dealers_total = dealers_logic(dealers_total, dealer, deck)

        # Display final totals for both player and dealer.
        print("Your total:", players_total, "Dealer's total:", dealers_total)

        # Determine outcome of the round.
        if players_total > 21 or (players_total < dealers_total <= 21):
            print("You lose.")
        elif (players_total > dealers_total) or (players_total <= 21 < dealers_total):
            print("You win.")
        elif dealers_total == players_total:
            print("Push.")

        # Ask if the player would like to play another round.
        continue_prompt = input("Would you like to play again? (y/n): ").lower()
        if continue_prompt == "n":
            game = False
        clear_terminal()

    print("Thank you for playing!\nGoodbye.")


# Start the Blackjack game.
main()
