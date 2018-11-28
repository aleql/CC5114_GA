import random

import itertools

from Gen.Individual import Individual


# Hardcoded seed for repetible experiments


class GeneticAlgorithm:

    def __init__(self, expected_sequence, generator, mutation_rate=0.0, population_size=10, iterations=5,
                 rand=random.Random(9001)):
        self.population = []
        self.expected_sequence = expected_sequence
        self.generator = generator
        self.mutation_rate = mutation_rate
        self.population_size = population_size
        self.iterations = iterations
        self.rand = rand

    # Initialize a new population of given size
    def initialize_population(self, pop_size):
        for _ in range(pop_size):
            new_individual = Individual(self.generator.generate_sequence())
            self.population.append(new_individual)

    # Select an individual from a population given a number of iterations
    def tournament_selection(self):
        best = None
        for i in range(self.iterations):
            individual = self.population[self.rand.randint(0, len(self.population) - 1)]
            if best is None \
                    or individual.evaluate_fitness(self.expected_sequence) > best.evaluate_fitness(
                self.expected_sequence):
                best = individual
        return best

    # For a single gen, mutate returns a mutation depending of the
    # mutation_rate
    def mutate(self, single_gen):
        if self.mutation_rate > self.rand.random():
            return self.generator.generate_sigle_gen()
        return single_gen

    # Produce a new individual given two parent indivuals,
    # The new inidivual is mutated given a mutation_rate
    def reproduce(self, individual1, individual2):

        # Create new gen
        mixing_point = self.rand.randint(0, len(individual1.gen))
        new_gen = individual1.gen[mixing_point:] + individual2.gen[:mixing_point]

        # Mutate based of mutation_rate
        if self.mutation_rate > self.rand.random():
            new_gen = list(map(lambda g: self.mutate(g), new_gen))

        return Individual(new_gen)


    def new_generation(self):
        # Generate mating pool, size = 1/4 size population
        matig_pool_size = int(self.population_size/4)
        mating_pool = [self.tournament_selection() for _ in range(matig_pool_size)]

        # repoduce(round robin(=?)) until size is fullfilled
        new_generation = []
        round_robin = itertools.cycle(mating_pool)
        while len(new_generation) < self.population_size:
            new_generation.append(self.reproduce(round_robin.next(),))

        # replace population
#
# def generate_bit_seq(length=5):
#         return list(np.random.randint(2, size=(length,)))
