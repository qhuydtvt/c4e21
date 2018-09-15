terms = {
    "lol": "Laugh out loud",
    "wth": "What the hell",
    "idk": "I don't know",
}

while True:
    key = input("Your term? ")
    if key in terms:
        print(terms[key])
    else:
        print("Not found")
    print()