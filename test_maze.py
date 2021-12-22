import numpy as np
import imageio
from genetics import Genetics
import maze_utils as utils

POPULATION_SIZE = 10

'''
Genes imbalance intended to ensure a bigger number of generations (demo purposes)
'''
GENES = '0111111111111110'

MAZE_EDGE = 5
MAZE_SIZE = MAZE_EDGE * MAZE_EDGE


def print_maze_progression_image(fittest_list: list):
    '''
    Output the fittest from generation into an animated gif
    '''
    image_list = []
    for fitness, fittest in fittest_list:
        nd_fittest = np.reshape(np.array(list(map(int, fittest.chromosome))), [MAZE_EDGE, MAZE_EDGE])
        processed_grid = utils.preprocess_grid(nd_fittest, MAZE_EDGE)
        #print(processed_grid)
        output = utils.carve_maze(processed_grid, MAZE_EDGE)
        
        o = []
        for elm in output:
            elm[elm == '#'] = 0
            elm[elm == ' '] = 1
            o.append(list(elm.astype(int)))
        nd_output = np.array(o)
        utils.add_grid_to_image_list(nd_output, image_list, fitness)
    imageio.mimsave('maze_output.gif', image_list, fps=2)


def cal_fitness(self):
    '''
    Calculate fitness score
    '''
    fitness = abs(sum(list(map(int, self.chromosome))) - MAZE_SIZE // 2)
    return fitness

def fitness_for_no_horz_corridors(self):
    '''
    Maze without horizontal corridors
    '''
    fitness = self.chromosome.count("0")
    return fitness

def cal_fitness3(self):
    '''
    Maze without vertical corridors
    '''
    fitness = self.chromosome.count("1")
    return fitness    


def main():
    g = Genetics(population_size=POPULATION_SIZE, genes=GENES, gnome_len=MAZE_SIZE, fitness_func=cal_fitness)
    output = g.run()
    for generation, (fitness, fittest) in enumerate(output):
        print("Generation: {} String: {} Fitness: {}".
            format(generation,
            "".join(fittest.chromosome),
            fitness))
    
    print_maze_progression_image(fittest_list=output)


if __name__ == '__main__':
    main()
