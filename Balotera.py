import random

balotas = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11", "B12", "B13", "B14", "B15",
           "I16", "I17", "I18", "I19", "I20", "I21", "I22", "I23", "I24", "I24", "I25", "I26", "I27", "I28", "I29",
           "I30", "N31", "N32", "N33", "N34", "N35", "N36", "N37", "N38", "N39", "N40", "N41", "N42", "N43", "N44",
           "G45", "G46", "G47", "G48", "G49", "G50", "G51", "G52", "G53", "G54", "G55", "G56", "G57", "G58", "G59",
           "O60", "O61", "O62", "O63", "O64", "O65", "O66", "O67", "O68", "O69", "O70", "O71", "O72", "O73", "O74"]
dicc ={}
fichas = []
for i in range(len(balotas)):
    dicc[i+1]=balotas[i]
    fichas.append(i+1)

fichaB = random.sample(range(1, 15), 5)
fichaI = random.sample(range(16, 30), 5)
fichaN = random.sample(range(31, 44), 4)
fichaG = random.sample(range(45, 60), 5)
fichaO = random.sample(range(61, 74), 5)

fichas = fichaB + fichaI + fichaN + fichaG + fichaO

listakeys = list(dicc.keys())
listavalores = list(dicc.values())

balotas_revueltas = []

for i in fichas:
    balotas_revueltas.append(dicc[i])

print(balotas_revueltas)