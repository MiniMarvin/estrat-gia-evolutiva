import random
import math
import statistics


class EstrategiaEvolutiva:
    """
	Estratégia evolutiva, passos do algoritmos:
	1. iniciar uma população de individuos aleatória
	2. construir um genótipo de função em R^n com n elementos
	3. adicionar a esse genótipo o desvio padrão de uma função normal (sigma) que se refere aos passos de mutação de cada um dos elementos daquele genótipo
	4. O fitness é a própria função que deve ser utilizada, no caso a função de Ackley. 
	5. pressão evolutiva de 7l para cada u
  

	O método de representação: 
	- uma lista com tuplas: [(X_i, Sigma_i)]
	"""

    def __init__(self, populationSize: int, mutationMethod: int,
                 crossoverMethod: int, nextGenMethod: int, limit: int,
                 learnRate: float):
        # -15 < x10 < 15
        # sigma pertence a R
        # x10' = x10 + N(0, sigma)
        self.genSize = 30
        self.populationSize = populationSize
        self.pool = [[(random.uniform(-15, 15), random.uniform(0, 1))
                      for _ in range(self.genSize)]
                     for _ in range(self.populationSize)]
        self.iteration = 0
        self.learnRate = learnRate
        self.limit = limit
        if crossoverMethod == 1:
            self.crossOver = self.crossover1
        elif crossoverMethod == 2:
            self.crossOver = self.crossover2
        elif crossoverMethod == 3:
            self.crossOver = self.crossover3
        else:
            self.crossOver = self.crossover4

        if mutationMethod == 1:
            self.mutation = self.mutate1
        else:
            self.mutation = self.mutate2

        if nextGenMethod == 1:
            self.nextGen = self.nextGen1
        else:
            self.nextGen = self.nextGen2

    def shouldEnd(self, iterations) -> bool:
        """
		Define se foi alcançada a condição de parada
		"""
        return iterations == self.limit

    def ackleyFunc(self, xSet):  #xSet: list[float] -> float
        c1 = 20
        c2 = 0.2
        c3 = 2 * math.pi
        n = self.genSize

        firstSum = 0
        for i in range(0, n):
            firstSum = firstSum + (xSet[i]**2)
        firstBlock = -c1 * math.exp(-c2 * math.sqrt(firstSum / n))

        secondSum = 0
        for i in range(0, n):
            secondSum = secondSum + math.cos(c3 * xSet[i])
        secondBlock = -math.exp(secondSum / n)

        finalResult = firstBlock + secondBlock + c1 + 1
        return finalResult

    # def fitness(self, gen: list[tuple[float, float]]) -> float:
    def fitness(self, gen) -> float:
        """
		Calcula o fitness de um gene
		"""
        values = [x[0] for x in gen]
        return self.ackleyFunc(values)

    def mutate1(self, gen, learnRate) -> float:
        """
		Algoritmo de mutação que vai ser aplicado sobre um gen.
		"""
        newGen = []
        sigma = gen[0][1]
        # print(gen)
        # print(sigma, learnRate, random.normalvariate(0,1))
        newSigma = sigma * math.exp(learnRate * random.normalvariate(0, 1))
        for x, _ in gen:
            newX = x + newSigma * random.normalvariate(0, 1)
            if newX < -15:
                newX = -15
            elif newX > 15:
                newX = 15
            newGen.append((newX, newSigma))

        return newGen

    def mutate2(self, gen, learnRate) -> float:
        """
		Algoritmo de mutação que vai ser aplicado sobre um gen.
		"""
        newGen = []
        for x, sigma in gen:
            newSigma = sigma * math.exp(learnRate * random.normalvariate(0, 1))
            newX = x + newSigma * random.normalvariate(0, 1)
            if newX < -15:
                newX = -15
            elif newX > 15:
                newX = 15
            newGen.append((newX, newSigma))

        return newGen

    def crossover1(self, pool):
        """
        Ponto local intermediário.
        """
        parents = random.sample(pool, 2)
        mix = lambda p1, p2: ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        child = [
            mix(parents[0][i], parents[1][i]) for i in range(self.genSize)
        ]
        return child

    def crossover2(self, pool):
        """
        Local discreto.
        """
        parents = random.sample(pool, 2)
        mix = lambda p1, p2: (random.choice([p1[0], p2[0]]), random.choice([p1[1], p2[1]]))
        child = [
            mix(parents[0][i], parents[1][i]) for i in range(self.genSize)
        ]
        return child

    def crossover3(self, pool):
        """
        Ponto Global Intermediário.
        """
        mix = lambda p1, p2: (([p1[0] + p2[0]]) / 2, ([p1[1] + p2[1]]) / 2)
        child = []
        for i in range(self.genSize):
            parents = random.sample(pool, 2)
            pair = mix(parents[0][i], parents[1][i])
            child.append(pair)

        return child

    def crossover4(self, pool):
        """
        Global discreto.
        """
        mix = lambda p1, p2: (random.choice([p1[0], p2[0]]), random.choice([p1[1], p2[1]]))
        child = []
        for i in range(self.genSize):
            parents = random.sample(pool, 2)
            pair = mix(parents[0][i], parents[1][i])
            child.append(pair)

        return child

    def nextGen1(self):  #in population -> newPop
        """
        Cria os filhos de acordo com a estratégia (μ,λ)
        μ -> tamanho da população
        λ -> o conjunto dos filhos
        λ = 7μ
        torneio sobre λ

        crossover (pool) => mutation => filhinho
        """
        newChilds = []
        for i in range(0, 7 * self.populationSize):
            crossChild = self.crossOver(self.pool)
            newChild = self.mutation(gen=crossChild, learnRate=self.learnRate)
            newChilds.append(newChild)

        newChilds.sort(key=lambda ind: self.fitness(ind), reverse=False)
        output = newChilds[:self.populationSize]

        return output

    def nextGen2(self):
        """
        Cria os filhos de acordo com a estratégia (μ + λ)
        μ -> tamanho da população
        λ -> o conjunto dos filhos
        λ = 7μ
        μ+λ -> conjunto com pais e filhos
        torneio sobre μ+λ
        """

        newChildsAndParents = self.pool
        for i in range(0, 7 * self.populationSize):
            crossChild = self.crossOver(self.pool)
            newChild = self.mutation(gen=crossChild, learnRate=self.learnRate)
            newChildsAndParents.append(newChild)

        newChildsAndParents.sort(key=lambda ind: self.fitness(ind), reverse=False)
        output = newChildsAndParents[:self.populationSize]

        return output

    # https://repl.it/@minimarvin/oito-rainhas#binary_eight_queens_enhanced_num.py
    def fit(self):
        stats = {"fitness": [], "fitnessHistory": []}
        pos = self.limit // 10
        for i in range(self.limit):
            # print(self.pool)
            newGen = self.nextGen()
            fitnesses = [self.fitness(gen) for gen in self.pool]
            avg = statistics.mean(fitnesses)
            stdev = statistics.stdev(fitnesses)
            stats["fitnessHistory"].append((avg, stdev))
            self.pool = newGen
            if i % pos == 0:
                print('geracao', i)
            if min(fitnesses) == 0:
                break
        fitnesses = [self.fitness(gen) for gen in self.pool]
        stats["fitness"] = fitnesses
        return stats
