# preinstalled libraries by python includes
# from is a keyword that imports a specific function from a library
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

# system library

def sys():
    import sys # a system module
    # print("Hello , My name is", sys.argv[1]) # always type your name befoe compiling this argument

# packages
# *cowsay ~ pip install cowsay
def say():
    import cowsay
    import sys
    if len(sys.argv) == 2:
        cowsay.cow("Hello, " + sys.argv[1])
        cowsay.milk("hi")
        cowsay.trex("run")
# Api
def api():
    import json
    import requests
    import sys

    if len(sys.argv) !=2:
        sys.exit()
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]) #this would show the json format for the argument by the user
                                                                                                        # the url also limits the song search to 10 as indicated , it can be changed anyways
    # print(json.dumps(response.json(), indent=3)) # this would make the json file more readable

    #no we want to print a specify output from the json file
    out = response.json()
    for result in out["results"]:
        print(f'Song Name: {result["trackName"]}') # this would print the song name that was taken from the json file
        print(f'Artist: {result["artistName"]}') # this would print the artist name that was taken from the json file
        print(f'Genre: {result["primaryGenreName"]} \n') # this would print the genre that was taken from the json file
def main():
    #random()
    #rand()
    #shuffle()
    #stats()
    # sys()
    #say()
    api()

main()

