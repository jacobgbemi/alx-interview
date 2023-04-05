#!/usr/bin/python3
"""Prime Game
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    winner = None

    for i in range(x):
        n = nums[i]
        primes = []
        is_prime = [True] * (n+1)
        is_prime[0] = is_prime[1] = False

        # Use Sieve of Eratosthenes to find all primes
        for p in range(2, n+1):
            if is_prime[p]:
                primes.append(p)
                for multiple in range(2*p, n+1, p):
                    is_prime[multiple] = False

        # Play the game
        current_player = "Maria"
        while primes:
            # Choose a prime number to remove
            prime = primes.pop(0)
            multiples = [num for num in range(prime, n+1, prime)]

            # Remove the prime and its multiples from the set
            for multiple in multiples:
                if multiple in primes:
                    primes.remove(multiple)

            # Check if the game is over
            if not primes:
                winner = current_player
                break

            # Switch to the other player's turn
            if current_player == "Maria":
                current_player = "Ben"
            else:
                current_player = "Maria"

    return winner
