import timeit

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    coin_count = {}
    for coin in coins:
        coin_count[coin] = amount // coin
        amount %= coin
    return coin_count

def find_min_coins(amount):
    min_coins = [0] + [float('inf')] * (amount + 1)
    used_coins = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                used_coins[i] = coin

    count_coins = {}
    current_sum = amount
    while current_sum > 0:
        coin = used_coins[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum -= coin

    return count_coins

def test_find_coins(amount, find_function):
    return find_function(amount)

# Пример использования
amount = 256842
time_for_greedy = timeit.timeit(lambda: test_find_coins(amount, find_coins_greedy), number=10)
time_for_min_coins = timeit.timeit(lambda: test_find_coins(amount, find_min_coins), number=10)

print("Жадібний алгоритм:", find_coins_greedy(amount))
print("Час на виконання':", time_for_greedy)

print("")

print("Динамічне програмування:", find_min_coins(amount))
print("Час на виконання':", time_for_min_coins)