

# Create new generator
# 0,1 5 lenght sequence generator
from Generator.Generator import Generator

generator = Generator(list("abcdefghijklmnñopqrstuvwxyz"), 5)
print(generator.generate_sequence())
print(generator.generate_single_gen())
