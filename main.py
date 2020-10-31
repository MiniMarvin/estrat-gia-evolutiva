from estrategia_evolutiva import EstrategiaEvolutiva

ee = EstrategiaEvolutiva(
    populationSize=100,
    mutationMethod=1,
    crossoverMethod=1,
    limit=100,
    learnRate=0.001)

stats = ee.fit()
print(stats['fitnessHistory'])
