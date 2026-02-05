import random


subjects = [
    "shahrukh khan",
    "Taylor Swift",
    "Virat Kohli",
    "Narendra Modi",
    "Joe Biden",
    "Rishi Sunak",
    "Alia Bahtt",
    "Cristiano Ronaldo",
    "Mamata Banerjee"

]

actions= [
    "lanches",
    "cancels",
    "dance with",
    "eats",
    "declare war on",
    "orders",
    "celebrates",
    "run",
    "dance"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside Parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India gate",
    "at New Delhi",
    "in Tokyo"
]
objects = [
    "a plate of samosa", 
    "a golden mic", 
    "a football", 
    "a laptop", 
    "a cup of tea", 
    "a bucket of popcorn", 
    "a red umbrella", 
    "a flying drone", 
    "a magic wand"
]
while True:
    subjects = random.choice(subjects)
    actions = random.choice(actions)
    objects  = random.choice(objects)
    places_or_things = random.choice(places_or_things)


    headline  = f"BREAKING NEWS : {subjects} {actions} {objects} {places_or_things}"
    print("\n" + headline)

    user_input  = input("\n Do you want another headline ? (yes/no)").strip().lower()
    if user_input == "no":
        break

print("\n Thanks for using the fake News Headline Generator . Have a fun day")