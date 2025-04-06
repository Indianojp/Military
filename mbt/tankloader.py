class Tankloader:
    def __init__(self,content: list):
        self.content = content
        self.target = 0
        self.ammo = False
        self.chamber = "Empty"
        self.racks = {}
        for i in range(0, len(content)):
            self.racks[i] = content[i]
    def load(self, type:str):
        if type not in self.racks.values():
            return f"No {type} remaining!"
        shortest = len(self.content)
        for i in self.racks:
            cwdist = (i - self.target) % len(self.content)
            ccdist = (self.target - i) % len(self.content)
            distance = min(cwdist,ccdist)
            if self.racks[i] == type and distance < shortest:
                shortest = i
        self.target = shortest
        if self.chamber == "Empty":
            self.chamber = (self.racks[self.target])
            self.ammo = self.target
            self.racks[self.target] = "Empty"
            return self.chamber+" loaded"
        else:
            return f"{self.chamber} is loaded, {self.racks[self.target]} is next!"
    def unload(self):
        self.racks[self.ammo] = self.chamber
        self.chamber = "Empty"
        return f"{self.racks[self.ammo]} unloaded!"
    def shoot(self):
        if self.chamber == "Empty":
            return "the chamber is empty"
        shot = (self.chamber)
        self.chamber = "Empty"
        racks = set(self.racks.values())
        racks.remove("Empty")
        if self.target == self.ammo:
            return f"{shot} shot! Remaining shells: {racks}"
        else:
            return f"{shot} shot! Remaining shells: {racks}\n{self.load(self.racks[self.target])}"

m1 = Tankloader(["AP","HE", "AP", "APHE","HEAT"])
print(m1.load("HE"))
print(m1.load("AP"))
print(m1.shoot())
print(m1.load("HE"))