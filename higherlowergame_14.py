import random

details = [{'Name': 'Neymar', 'Followers': 400, 'Occupation': 'footballer', 'Origin': 'Brazil'},
           {'Name': 'Kardashian', 'Followers': 320, 'Occupation': 'Tv reality show', 'Origin': "America"},
           {'Name': 'Messi', 'Followers': 500, 'Occupation': 'footballer', 'Origin': 'Argentina'},
           {'Name': 'Cristiano', 'Followers': 600, 'Occupation': 'footballer', 'Origin': 'Portugal'},
           {'Name': 'Rock', 'Followers': 520, 'Occupation': 'actor', 'Origin': 'America'},
           {'Name': 'Selena', 'Followers': 330, 'Occupation': 'Singer', 'Origin': 'America'},
           {'Name': 'Magnus Carlson', 'Followers': 110, 'Occupation': 'Chess player', 'Origin': 'Norway'}]

you_loose = False
user_score = 0

while not you_loose:
    x = random.randint(0, len(details))
    y = random.randint(0, len(details))

    while x == y:
        y = random.randint(0, len(details))

    print(f"{details[x]['Name']} is a {details[x]['Occupation']} from {details[x]['Origin']}")
    print(f"{details[y]['Name']} is a {details[y]['Occupation']} from {details[y]['Origin']}")
    value = input(f"Enter A if {details[x]['Name']} has more followers than {details[y]['Name']} or B otherwise: ")

    if value == 'A' and details[x]['Followers'] > details[y]['Followers']:
        user_score += 1
    elif value == 'B' and details[y]['Followers'] > details[x]['Followers']:
        user_score += 1
    else:
        you_loose = True
        print("you loose ! your score is ", user_score)
