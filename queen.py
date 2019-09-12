import random
import names


selections = [23, 15, 47, 27]
weeks = 0
gameOver = False
numentries = 100


class Entry:
    def __init__(self, name, number):
        self.n = name
        self.num = number


def Reset(selections, numentries, entries):
    for i in range(1, numentries):
        number = random.choice(selections)
        name = names.get_full_name()
        currEntry = Entry(name, number)
        entries.append(currEntry)
    entries.append(Entry('Margaret Dospiljulian', random.choice(selections)))


def Probability(numentries, numcards, bought):
    probability = 0
    count = 1
    for i in range(0, numcards - 1):
        entries = numentries * (count)
        currCard = numcards - i
        picked = bought / entries
        rightCard = bought / currCard
        probability = probability + (picked * rightCard)
        count += bought
    return probability


def Simulation(selections, numentries):
    gameOver = False
    numberOfWins = 0
    numGames = 0
    newselections = selections
    entries = []
    Reset(newselections, numentries, entries)
    while (len(newselections) > 0) and (gameOver == False):
        currChoice = random.choice(entries)
        currNum = currChoice.num
        currName = currChoice.n
        winningNumber = random.choice(newselections)
        if currNum not in newselections:
            print("selections numbers: ")
            for i in newselections:
                print(i)
            print("Current Number: " + str(currNum))
        if currNum == winningNumber:
            gameOver = True
            numGames = numGames + 1
            if currName == 'Margaret Dospiljulian':
                numberOfWins += 1
        else:
            newselections.remove(winningNumber)
            numentries = numentries + 100
            entries.clear()
            if len(newselections) > 0:
                Reset(newselections, numentries, entries)
    return numberOfWins


numberOfWins = 0

print("Theoretical probability of winning: " + str(round(Probability(10000, 4, 200) * 100, 3)) + "%")

# for i in range(1000):
#     selections = [23, 15, 47, 27]
#     numberOfWins += Simulation(selections, numentries)
#     print("Game: " + str(i) + " completed.")
# print("Margaret won " + str(numberOfWins) + " times out of 1000")
