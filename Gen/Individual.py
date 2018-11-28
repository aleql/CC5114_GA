from functools import reduce


class Individual:

    def __init__(self, value):
        self.gen = value
        self.score = 0

    def evaluate_fitness(self, expected_sequence):
        diff_list = map((lambda x: 1 if x[0] == x[1] else 0), list(zip(self.gen, expected_sequence)))
        self.score = reduce((lambda x, y: x + y), diff_list)
        return self.score

# ind = Individual("00100")
# print(ind.evaluate_fitness("00100"))
