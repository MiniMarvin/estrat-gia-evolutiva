from estrategia_evolutiva import EstrategiaEvolutiva

ee = EstrategiaEvolutiva(
    populationSize=200,
    mutationMethod=2,
    crossoverMethod=4,
    nextGenMethod=1,
    limit=500,
    learnRate=0.00001)

stats = ee.fit()
print(stats['fitness'])
