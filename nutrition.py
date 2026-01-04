fruits = input("Items: ").lower()
items = [
    {"name": "apple", "Calories": 130 },
    {"name": "banana", "Calories": 110},
    {"name": "Avocardo", "Calories": 50},
    {"name": "Cantaloupe", "Calories": 50},
    {"name": "grapefruit", "Calories": 60},
]

for item in items:
    if item["name"].lower() in fruits:
        print("Calories: ", item["Calories"])