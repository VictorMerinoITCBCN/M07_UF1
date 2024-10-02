coins = {
    "euro" : "€",
    "dolar" : "$"
}

user_coin = input("Coin: ").lower()
print(f"{user_coin.capitalize()} - {coins[user_coin]}") if user_coin in coins else print(f"{user_coin.capitalize()} no esta a la llista")