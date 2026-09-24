from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    """
    Given an integer array representing coins of different denominations,
    and an integer `amount` representing the total amount of money.
    Return the fewest number of coins that you need to make up that amount.

    f([2,5], 11-1) + 1 => f([1,2,5], 11)

    f(0) = 0
    f(1) = 1
    f(2) = 2 (n=1)
    f(3) = 1+2 (n=2)
    f(4) = 2+2 (n=2)
    f(5) = 5 (n=1)

    f(n) = f(n-coin_max) + 1

    so , for any x, f(x) = v, if there is a combo, v > 0, else v = 0
    """

    F = [-1] * (amount + 1)
    F[0] = 0

    for i in range(1, amount + 1):
        F[i] = min([(F[i - c] + 1) for c in coins if c <= i and F[i - c] >= 0])

    return F[amount]