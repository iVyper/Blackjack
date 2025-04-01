
# Blackjack
Blackjack is a command-line card game implemented in Python where you play against a dealer. The game simulates a real deck of cards by shuffling and dealing cards, calculates hand totals with special handling for Aces, and follows standard Blackjack rules. As a player, you can choose to "hit" (take another card) or "stand" (end your turn). The dealer then plays by hitting until reaching a total of 17 or more. The game determines the outcome based on the final totals and offers the option to play multiple rounds.

## Features

- **Shuffled Deck:** Creates a deck with four of each card type, simulating four suits, and shuffles it for every round.

- **Accurate Hand Calculation:** Implements logic to handle Aces as either 11 or 1, ensuring your hand total is calculated correctly.

- **Interactive Gameplay:** Prompts you to hit or stand, and displays your hand, the dealer’s visible card, and the dealer's actions.

- **Dealer Logic:** The dealer automatically hits until reaching at least 17, following standard Blackjack rules.

- **Multiple Rounds:** Allows you to play again after each round with the option to start a new game.

- **Clean Interface:** Clears the terminal screen between actions to keep the interface uncluttered.

## Installation

### Prerequisites

- **Python 3.x:** Ensure that Python 3 is installed on your system. You can download it from [Python's offical website](python.org).

### How to Run

1. **Download the Code:** Clone the repository or download the `Blackjack.py` file to your computer.

2. **Open Terminal/Command Prompt:** Navigate to the directory containing the file.

3. **Run the program:** Execute the following command:

    ```bash
    python3 Blackjack.py
    ```

4. **Follow the Prompts:**
   - The game will display a welcome message, your initial hand, and the dealer's first card.

   - Choose whether to "hit" (take another card) or "stand" (end your turn).

   - After your turn, the dealer will play according to standard Blackjack rules.

   - The game will then display the final totals and announce whether you win, lose, or push.

   - At the end of the round, you will be prompted to play again.

   


## Demo
![Blackjack Demo](https://i.imgur.com/IWOna36.gif)
[Blackjack Demo](https://i.imgur.com/IWOna36.gif)

## License

This project is open-source and available under the [MIT License](https://choosealicense.com/licenses/mit/).


## Authors

- Ivis Perdomo [@ivyper](https://www.github.com/ivyper)

