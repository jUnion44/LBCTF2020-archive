class Town():
    def __init__(self,pop):
        self.exports = {}
        self.population = pop
        self.populationQueue = 0
    def moveIn(self,ppl):
        self.populationQueue += ppl
    def confirmMoveIn(self):
        self.population+=self.populationQueue
        self.populationQueue=0
        #print(self.population)
    def moveOut(self):
        for e in list(self.exports.keys()):
            delta = self.exports[e]*self.population
            e.moveIn(delta)
            #input("Moving " + str(self.exports[e]*self.population) + " out of " + str(self.population) + "to another town." )
        
            self.population = self.population - delta
        #input(str(self.population)+" remaining")

        
towns = {
    "a":Town(128),
    "b":Town(48),
    "c":Town(88),
    "d":Town(88),
    "e":Town(88),
    "f":Town(88),
    "g":Town(88),
    "h":Town(88),
    "i":Town(88),
    "j":Town(88),
    "k":Town(88),
    "l":Town(88),
    "m":Town(88),
    "n":Town(90)}

towns["a"].exports = {towns["e"]:0.35,towns["m"]:0.15}
towns["b"].exports = {towns["a"]:0.33,towns["f"]:0.1,towns["k"]:0.03,towns["m"]:0.04}
towns["c"].exports = {towns["g"]:0.5}
towns["d"].exports = {towns["k"]:0.1,towns["m"]:0.1,towns["n"]:0.2}
towns["e"].exports = {towns["b"]:0.02,towns["h"]:0.4,towns["l"]:0.03,towns["m"]:0.35}
towns["f"].exports = {towns["a"]:0.125,towns["j"]:0.1,towns["m"]:0.025}
towns["g"].exports = {towns["c"]:0.12,towns["k"]:0.18,towns["l"]:0.2}

towns["h"].exports = {towns["c"]:0.01,towns["e"]:0.2,towns["k"]:0.1,towns["m"]:0.3}
towns["i"].exports = {towns["b"]:0.2,towns["d"]:0.2,towns["m"]:0.1}
towns["j"].exports = {towns["b"]:0.008,towns["e"]:0.05,towns["f"]:0.015,towns["g"]:0.047,towns["l"]:0.1,towns["m"]:0.03,towns["n"]:0.09}
towns["k"].exports = {towns["e"]:0.125,towns["f"]:0.22,towns["i"]:0.005,towns["j"]:0.02,towns["n"]:0.11}
towns["l"].exports = {towns["a"]:0.01,towns["d"]:0.02,towns["e"]:0.01,towns["h"]:0.03,towns["i"]:0.44,towns["k"]:0.04}
towns["m"].exports = {towns["b"]:0.12,towns["c"]:0.2,towns["d"]:0.005,towns["h"]:0.01,towns["i"]:0.03,towns["j"]:0.185,towns["l"]:0.15}
towns["n"].exports = {towns["d"]:0.12,towns["k"]:0.13,towns["m"]:0.05}

def advanceYear():
    
    for t in towns.values():
        t.moveOut()
    for t in towns.values():
        t.confirmMoveIn()
    
    sumpop = 0
    for t in towns.values():
        sumpop += t.population
    #input(sumpop)
    

for count in range(1000000):
    advanceYear()
    if count%1000 == 0:
        for t in towns.values():
            print(chr(int(t.population)),end="")
        print()
    


