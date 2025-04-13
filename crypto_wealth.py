crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 0.3
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.8
    }
}

def get_recommendation(user_query):
    user_query = user_query.lower()

    if "trending up" in user_query:
        trending_up = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending_up:
            return f"Coins currently trending upwards are: {', '.join(trending_up)}."
        else:
            return "Currently, no coins in my data are marked as strongly trending upwards."

    elif "most sustainable" in user_query:
        best_sustainability = 0
        sustainable_coins = []
        for coin, data in crypto_db.items():
            if data["sustainability_score"] > best_sustainability:
                best_sustainability = data["sustainability_score"]
                sustainable_coins = [coin]
            elif data["sustainability_score"] == best_sustainability and best_sustainability > 0:
                sustainable_coins.append(coin)

        if sustainable_coins:
            return f"The most sustainable coin(s) based on my data: {', '.join(sustainable_coins)} with a sustainability score of {best_sustainability*10}/10."
        else:
            return "I don't have enough information to determine the most sustainable coin."

    elif "long-term growth" in user_query or "buy" in user_query or "invest" in user_query:
        profitable_sustainable = [
            coin for coin, data in crypto_db.items()
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7
        ]
        if profitable_sustainable:
            return f"For potential long-term growth and sustainability, consider: {', '.join(profitable_sustainable)}."
        profitable = [
            coin for coin, data in crypto_db.items()
            if data["price_trend"] == "rising" and data["market_cap"] == "high"
        ]
        if profitable:
            return f"For potentially profitable options with high market cap, consider: {', '.join(profitable)}."
        else:
            return "Based on my current data, I don't have a strong recommendation for long-term growth right now."

    else:
        return "Sorry, I don't quite understand that question. Try asking about trending coins or sustainability."

def chat():
    print("Welcome to CryptoWealth! Your AI-powered crypto advisor.")
    print("\n⚠️ Crypto is risky—always do your own thorough research before making any investment decisions! ⚠️\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            print("CryptoWealth: Happy investing! Remember to do your own research. 👋")
            break
        response = get_recommendation(user_input)
        print(f"CryptoWealth: {response}")

if __name__ == "__main__":
    chat()