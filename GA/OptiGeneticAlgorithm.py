from GA.GeneticAlgorithm import GeneticAlgorithm
from Individual.Individual import Individual


class OptiGeneticAlgorithm(GeneticAlgorithm):

    def __init__(self, *args, **kwargs):
        super(OptiGeneticAlgorithm, self).__init__(*args, **kwargs)


    # Override of father reproduce, to reproduce by chunks of data
    def reproduce(self, individual1, individual2):

        # Create new gen, for each 8bit chunk
        variables_individual1 = [individual1.chromosome[i:i + 8] for i in range(0, len(individual1.chromosome), 8)]
        variables_individual2 = [individual2.chromosome[i:i + 8] for i in range(0, len(individual2.chromosome), 8)]

        new_chromosome = ""

        for var1, var2 in zip(variables_individual1, variables_individual2):
            mixing_point = self.rand.randint(0, len(var1))
            new_variable = var2[:mixing_point] + var1[mixing_point:]

            # Mutate based of mutation_rate
            if self.mutation_rate > self.rand.random():
                # new_gen = list(map(lambda g: self.mutate(g), new_gen))
                new_variable = self.mutate(new_variable)

            new_chromosome += new_variable

        return Individual(new_chromosome)

