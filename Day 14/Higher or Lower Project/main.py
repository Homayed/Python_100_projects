import game_data
import art
import random

data = game_data.data


def get_random_item(items, exclude_item=None):
    """Get a random item from the list, excluding a specific item if provided."""
    filtered_items = [item for item in items if item != exclude_item]
    return random.choice(filtered_items)


def play_game(items):
    score = 0
    print(art.logo)
    # Choose a random starting item
    current_item = get_random_item(items)

    while True:
        # Get another random item to compare, ensuring it's not the current item
        next_item = get_random_item(items, exclude_item=current_item)


        print(f"1. {current_item['name']}")
        print(art.vs)
        print(f"2. {next_item['name']}")

        # Get user choice
        choice = input("Choose the individual with more followers (1 or 2): ")

        # Validate user input
        if choice not in ['1', '2']:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        # Determine the correct item based on follower count
        correct_item = current_item if current_item['follower_count'] > next_item['follower_count'] else next_item

        # Check if the choice is correct
        if (choice == '1' and current_item['follower_count'] > next_item['follower_count']) or \
                (choice == '2' and next_item['follower_count'] > current_item['follower_count']):
            print("Correct!")
            score += 1

            # Get a new item to replace the next_item
            new_next_item = get_random_item(items, exclude_item=current_item)
            next_item = new_next_item

            # If there are no more items left to compare, end the game
            if len(items) < 2:
                print("No more items to compare. Game over!")
                break
        else:
            print("Game Over!")
            break

    print(f"Your final score is: {score}")


# Start the game
play_game(data)