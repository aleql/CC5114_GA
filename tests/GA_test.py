import unittest

from Generator.Generator import Generator
from GeneticAlgorithm import GeneticAlgorithm


class Test_generator(unittest.TestCase):

    def test_binary_genetic_algorithm(self):
        self.generator = Generator(['0', '1'], 5)
        self.GA = GeneticAlgorithm(self.generator, 8, "01010")
        self.GA.initialize_population()
        generations, chromosome = self.GA.genetic_algorithm()

        assert generations == 4, "GA did not converge on generation 4"
        assert chromosome == "01010", "GA did not converge to the right chromosome"

    def test_character_genetic_algorithm(self):
        self.generator = Generator(list("abcdefghijklmnñopqrstuvwxyz"), 10)
        self.GA = GeneticAlgorithm(self.generator, 16, "murcielago")
        self.GA.initialize_population()
        generations, chromosome = self.GA.genetic_algorithm()

        assert generations == 659, "GA did not converge on generation 4"
        assert chromosome == "murcielago", "GA did not converge to the right chromosome"





