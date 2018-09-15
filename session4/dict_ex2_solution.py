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
        contribute = input("Do you want to contribute (Y/N)? ").upper()
        if contribute == "Y":
            value = input("Your explanation? ")
            terms[key] = value
            print("Added")
    print()
