import random

import itertools

from Individual.Individual import Individual


class GeneticAlgorithm:

    def __init__(self, expected_sequence, generator, mutation_rate=0.1, population_size=10, iterations=5,
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
            individual = self.rand.choice(self.population) # self.population[self.rand.randint(0, len(self.population) - 1)]
            if best is None \
                    or individual.evaluate_fitness(self.expected_sequence) > best.evaluate_fitness(
                self.expected_sequence):
                best = individual
        return best

    def best_selection(self):
        for individual in self.population:
            individual.evaluate_fitness()
        

    # For a chromosome, mutate, changes randomly one gen of the chromosome.
    def mutate(self, chromosome):
        mutation_index = self.rand.randint(0, len(chromosome) - 1)

        # chromosome[mutation_index] = self.generator.generate_single_gen()

        text = chromosome
        new = list(text)
        new[mutation_index] = self.generator.generate_single_gen()
        new = ''.join(new)

        return new

    # Produce a new individual given two parent indivuals,
    # The new inidivual is mutated given a mutation_rate
    def reproduce(self, individual1, individual2):

        # Create new gen
        mixing_point = self.rand.randint(0, len(individual1.chromosome))
        new_chromosome = individual1.chromosome[mixing_point:] + individual2.chromosome[:mixing_point]

        # Mutate based of mutation_rate
        if self.mutation_rate > self.rand.random():
            # new_gen = list(map(lambda g: self.mutate(g), new_gen))
            new_chromosome = self.mutate(new_chromosome)

        return Individual(new_chromosome)

    # Generate a new population in a round robin permutation
    def generate_population(self, mating_pool):
        new_generation = []
        cycle_combinations = itertools.cycle(list(itertools.combinations(mating_pool, 2)))
        while len(new_generation) < self.population_size:
            mating_individuals = next(cycle_combinations)
            new_generation.append(self.reproduce(mating_individuals[0], mating_individuals[1]))
        return new_generation

    # Generate new population from the best individuals in a generation choosen via tournament selection.
    def new_generation(self):
        # Generate mating pool, size = 1/4 size population
        mating_pool_size = int(self.population_size/4)
        mating_pool = [self.tournament_selection() for _ in range(mating_pool_size)]

        # Generate a new population
        new_generation = self.generate_population(mating_pool)

        # replace population
        self.population = new_generation

