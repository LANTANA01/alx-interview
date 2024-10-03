#!/usr/bin/python3
""" Determines who the winner of each game is."""


def isWinner(x, nums):
    def sieve(n):
        """ Helper function to generate list of primes up to n using Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulate the game for a given n """
        primes = sieve(n)
        moves = 0
        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            moves += 1
        return moves % 2 == 1  # Maria wins if moves are odd, Ben wins if moves are even

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        elif play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
