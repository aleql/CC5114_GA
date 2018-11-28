

# Create new generator
# 0,1 5 lenght sequence generator
from GeneticAlgorithm import GeneticAlgorithm
from Individual.Individual import Individual
from Generator.Generator import Generator

generator = Generator(list("abcdefghijklmnñopqrstuvwxyz"), 10)
# generator = Generator(['0', '1'], 5)
# print(generator.generate_sequence())
# print(generator.generate_single_gen())

# Create an individual and check fitness
# test_individual = Individual(generator.generate_sequence())
# print(test_individual.evaluate_fitness("bjcri"))

# Generate population
GA = GeneticAlgorithm(generator, 16, "murcielago")
GA.initialize_population()

print(GA.genetic_algorithm())
# pop = ""
# for i in GA.population:
#     pop += str(i.chromosome) # + "/" + str(i.score) + " "
# print("Initial populi: ")
# print(pop)
# print()
#
# last = None
# for _ in range(100):
#     GA.new_generation()
#     pop = ""
#     for i in GA.population:
#         pop += str(i.chromosome) # + "/" + str(i.score) + " "
#     print("New populi: ")
#     print(pop)
#     # last = pop
#     print()
#
# print("end")
# print(last)

