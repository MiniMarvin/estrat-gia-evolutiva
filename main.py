from estrategia_evolutiva import EstrategiaEvolutiva

# ee = EstrategiaEvolutiva(
#     populationSize=200,
#     mutationMethod=1,
#     crossoverMethod=1,
#     nextGenMethod=2,
#     limit=500,
#     learnRate=0.00001)

ee = EstrategiaEvolutiva(
    populationSize=250,
    mutationMethod=2,
    crossoverMethod=2,
    nextGenMethod=2,
    limit=500,
    learnRate=0.0005, pressure=10)

stats = ee.fit()
print(stats['fitness'][0])
print(stats['bestIndividual'])

# from validate import run

# run()