competitors = {
    "South Africa": {'wins': 3, 'losses': 4},
    "Mexico": {'wins': 2, 'losses': 8},
    "Portugal": {'wins': 7, 'losses': 1},
    "Spain": {'wins': 0, 'losses': 8},
    "Argentina": {'wins': 6, 'losses': 2}
}

highest = None
highest_wins = 0

for country in competitors:
    if competitors[country]['wins'] > highest_wins:
        highest_wins = competitors[country]['wins']
        highest = country

print(highest)