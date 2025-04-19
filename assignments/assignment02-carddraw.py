#Deals five cards from a Deck of Cards API, prints them out, and checks for poker-style patterns: pair, triple, straight, and flush. 

import requests
from collections import Counter 

#mapping face cards to numeric values
face_card_values = {
    'JACK': 11, 
    'QUEEN': 12, 
    'KING': 13, 
    'ACE': 14
}

def shuffle_deck():
    #shuffle a new deck and return it's deck_id
    shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(shuffle_url)
    data = response.json()
    deck_id= data['deck_id']
    print(f"Deck ID: {deck_id}")
    return deck_id


def draw_cards(deck_id, count=5):
    #draw five cards from the shuffled deck
    draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    response = requests.get(draw_url)
    response.raise_for_status()
    return response.json()['cards']

def evaluate_hand(cards):
    values = [c['value'] for c in cards]
    suits = [c['suit'] for c in cards]

    #convert face cards to numbers
    numbers = sorted(
        face_card_values[v] if v in face_card_values else int(v)
        for v in values
    )

    #checking for straights (incuding Ace low straight)
    is_consecutive = all(numbers[i] == numbers[i-1] + 1 for i in range(1, len(numbers)))
    ace_low = numbers == [2,3,4,5,14]
    straight = is_consecutive or ace_low 

    #check for flush/same suit
    flush = len(set(suits)) == 1

    #count duplications 
    value_counts = Counter(values)
    pairs = [v for v, count in value_counts.items() if count == 2]
    triples = [v for v, count in value_counts.items() if count == 3]

    return {
        'pairs': pairs, 
        'triples': triples, 
        'straight': straight, 
        'flush': flush
    }

def main():
    deck_id = shuffle_deck()
    cards = draw_cards(deck_id, count=5)

    print ("\nDrawn Cards:")
    for c in cards: 
        print(f" {c['value']} of {c['suit']}")

    result = evaluate_hand(cards)

    #print which patterns occured 
    if result['pairs']:
        print("You got a pair!")
    if result['triples']:
        print("You got a triple!")
    if result['straight']:
        print("You got a straight!")
    if result['flush']:
        print("You got a flush! All cards are the same suit.")

    #final prints - win or loss
    if result['pairs'] or result['triples'] or result ['straight'] or result ['flush']:
        print("\nCongratulations on your hand! :) ")
    else: 
        print("\n Better luck next time! :( ")

if __name__ == "__main__":
    main()