import random

class Teams:
    def __init__(self, name,nationality, place):
        self.name = name
        self.nationality=nationality
        self.place=place

def valid_match(t1,t2):
    if t1.nationality== t2.nationality:
        return False
    if t1.place==t2.place:
        return False
    if t1.nationality=="Russia" and t2.nationality=="Ukraine":
        return False
    if t1.nationality=="Ukraine" and t2.nationality=="Russia":
        return False
    return True

def roundof16(teams):
    matches=[]
    used = []
    while len(matches)<8:
        t1=random.choice(teams)
        if t1 in used:
            continue

        posssible=[]
        for i in teams:
            if i in used:
                continue
            if i==t1:
                continue
            if not valid_match(t1, i):
                continue
            posssible.append(i)

        if len(posssible) ==0:
            return roundof16(teams)
        
        t2=random.choice(posssible)
        matches.append((t1,t2))
        used.append(t2)
        used.append(t1)
    return matches

teams = [
    Teams("PSG", "France", 2),
    Teams("Liverpool", "England", 1),
    Teams("Inter", "Italy", 1),
    Teams("Manchester City", "England", 1),
    Teams("Leipzig", "Germany", 2),
    Teams("Eintracht Frankfurt", "Germany", 2),
    Teams("Napoli", "Italy", 1),
    Teams("Porto", "Portugal", 2),
    Teams("Barcelona", "Spain", 2),
    Teams("Benfica", "Portugal", 2),
    Teams("Dynamo Moscow", "Russia", 1),
    Teams("Milan", "Italy", 1),
    Teams("Bayern", "Germany", 1),
    Teams("Real Madrid", "Spain", 1),
    Teams("Shakhtar", "Ukraine", 2),
    Teams("Dortmund", "Germany", 2),
]

matches = roundof16(teams)
for a,b in matches:
    print(a.name," - ", b.name)