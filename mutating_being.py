from random import choice


class MutatingBeing:

    def __init__(self, genes: str):
        self.genes = genes

    def mutate_genes(self) -> str:
        gene = choice(self.genes)
        return gene
