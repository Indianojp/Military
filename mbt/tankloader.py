class Tankloader:
    def __init__(self,content: list):
        self.content = content
        self.state = 0
        self.loaded = None
        self.rounds = {}
        for i in range(0, len(content)):
            self.rounds[i] = content[i]
    def load(self, type:str):
        shortest = len(self.content)
        for i in self.rounds:
            cwdist = (i - self.state) % len(self.content)
            ccdist = (self.state - i) % len(self.content)
            distance = min(cwdist,ccdist)
            if self.rounds[i] == type and distance < shortest:
                shortest = i
        self.state = shortest
        if not self.loaded:
            self.loaded = self.state
            return self.rounds[self.loaded]+" loaded"
    def shoot(self):
        shot = self.rounds[self.loaded]
        self.rounds[self.loaded] = None
        return f"remaining shells: {self.rounds}"

m1 = Tankloader(["AP","HE","APHE","HEAT"])
print(m1.load("HE"))
print(m1.shoot())