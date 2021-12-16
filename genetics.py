from individual import Individual
from random import choice
from mutating_being import MutatingBeing


class Genetics(MutatingBeing):

    def __init__(self, population_size, genes, gnome_len, fitness_func):
        super().__init__(genes)
        self.population_size = population_size
        self.fitness_func = fitness_func
        self.gnome_len = gnome_len
        print(self.gnome_len)

    def create_gnome(self) -> list:
        return [self.mutate_genes() for _ in range(self.gnome_len)]

    def run(self) -> list:
        output = []
        # current generation
        generation = 1

        found = False
        population = []

        # create initial population
        for _ in range(self.population_size):
            gnome = self.create_gnome()
            population.append(Individual(gnome, self.genes, self.gnome_len, self.fitness_func))

        while not found:

            # sort the population in increasing order of fitness score
            population = sorted(population, key=lambda x: x.fitness)

            # if the individual having lowest fitness score ie.
            # 0 then we know that we have reached to the target
            # and break the loop
            if population[0].fitness <= 0:
                found = True
                break

            # Otherwise generate new offsprings for new generation
            new_generation = []

            # Perform Elitism, that mean 10% of fittest population
            # goes to the next generation
            s = int((10*self.population_size)/100)
            new_generation.extend(population[:s])

            # From 50% of fittest population, Individuals
            # will mate to produce offspring
            s = int((90*self.population_size)/100)
            for _ in range(s):
                parent1 = choice(population[:self.population_size//2])
                parent2 = choice(population[:self.population_size//2])
                child = parent1.mate(parent2)
                new_generation.append(child)

            population = new_generation

            output.append((generation, population[0]))
            generation += 1

        output.append((generation, population[0]))
        return output
