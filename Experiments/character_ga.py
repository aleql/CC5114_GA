
from Calculator.Seq_Calculator import Seq_Calculator
from Charts import lineChart
from GA.GeneticAlgorithm import GeneticAlgorithm
from Generator.Generator import Generator

character_generator = Generator(list("abcdefghijklmnñopqrstuvwxyz"), 10)

expected_sequence = "murcielago"

population_size = 16

# Calculator
calculator = Seq_Calculator(expected_sequence)

GA = GeneticAlgorithm(character_generator, population_size, calculator)
GA.initialize_population()

generations, chromosome, ga_stats = GA.genetic_algorithm()
print("Generations: {}".format(generations))
print("Chromosome: {}".format(chromosome))
# print("ga_stats: {}".format(ga_stats))


lineChart(list(range(generations)), ga_stats["sum"], "Generations", "Total Fitness", "Number of generations vs Total fitness for character string {} \n and population size: {}".format(expected_sequence, population_size))
lineChart(list(range(generations)), ga_stats["mean"], "Generations", "Mean Fitness", "Number of generations vs Mean fitness for character string {} \n and population size: {}".format(expected_sequence, population_size))
lineChart(list(range(generations)), ga_stats["std"], "Generations", "Standard deviation Fitness", "Number of generations vs Std Deviation of fitness for character string {} \n and population size: {}".format(expected_sequence, population_size))
lineChart(list(range(generations)), ga_stats["var"], "Generations", "Var Fitness", "Number of generations vs Variance of fitness for character string {} \n and population size: {}".format(expected_sequence, population_size))

