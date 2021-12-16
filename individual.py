import random

from mutating_being import MutatingBeing

class Individual(MutatingBeing):

    def __init__(self, chromosome: str, genes: str, gnome_len: int, fitness_func):
        super().__init__(genes)
        self.chromosome = chromosome
        self.gnome_len = gnome_len
        self.fitness_func = fitness_func
        self.fitness = fitness_func(self)

    def mate(self, par2) -> list:
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()

            # if prob is less than 0.45, insert gene
            # from parent 1
            if prob < 0.45:
                child_chromosome.append(gp1)
 
            # if prob is between 0.45 and 0.90, insert
            # gene from parent 2
            elif prob < 0.90:
                child_chromosome.append(gp2)

            else:
                child_chromosome.append(self.mutate_genes())

        return Individual(child_chromosome,self.genes,self.gnome_len,self.fitness_func)
