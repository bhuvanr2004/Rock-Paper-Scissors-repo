# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # Default guess
    guess = "R"

    # Use frequency analysis if enough history is available
    if len(opponent_history) >= 3:
        # Count frequencies
        freq = {"R": 0, "P": 0, "S": 0}
        for move in opponent_history:
            freq[move] += 1

        # Predict most frequent move
        predicted_move = max(freq, key=freq.get)

        # Counter it
        counter = {"R": "P", "P": "S", "S": "R"}
        guess = counter[predicted_move]

    return guess