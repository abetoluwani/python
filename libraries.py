# preinstalled libraries by python includes
# *random
#using the random libraries

def random():
    import random as r # choice only takes up to 2 argument
    coin = r.choice(["heads","tails"])
    print(coin)

def rand():
    import random
    num = random.randint(1,40)
    print(num)

def shuffle():
    import random
    cards = ["Jack","King","Queen","Knight","Bishop"]
    random.shuffle(cards)
    print(cards) # it would be displayed as a list but shuffled

    for card in cards:
        print(card)
# Statistics Library
def stats():
    import statistics


    mean = statistics.mean([96,83])
    print(mean)


random()
rand()
shuffle()
stats()
# from is a keyword that imports a specific function from a library