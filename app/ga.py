import random
import string

def generate_chromosome(length):
    chars = string.ascii_uppercase + ' '
    return ''.join(random.choice(chars) for _ in range(length))

def calculate_fitness(chromosome, target):
    return sum(1 for i in range(len(target)) if i < len(chromosome) and chromosome[i] == target[i])

def select_parent(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    if total_fitness == 0:
        return random.choice(population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, chromosome in enumerate(population):
        current += fitness_scores[i]
        if current > pick:
            return chromosome
    return random.choice(population)

def crossover(parent1, parent2, length):
    point = random.randint(1, length - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def mutate(chromosome, mutation_rate):
    chars = string.ascii_uppercase + ' '
    mutated = list(chromosome)
    for i in range(len(mutated)):
        if random.random() < mutation_rate:
            mutated[i] = random.choice(chars)
    return ''.join(mutated)

def run_genetic_algorithm(target, population_size, mutation_rate, generations, progress_callback):
    population = [generate_chromosome(len(target)) for _ in range(population_size)]
    for generation in range(1, generations + 1):
        fitness_scores = [calculate_fitness(c, target) for c in population]
        best_idx = fitness_scores.index(max(fitness_scores))
        best = population[best_idx]
        best_fitness = fitness_scores[best_idx]
        progress_callback(generation, best, best_fitness)
        if best == target:
            return best, generation
        new_population = [best]
        while len(new_population) < population_size:
            p1 = select_parent(population, fitness_scores)
            p2 = select_parent(population, fitness_scores)
            c1, c2 = crossover(p1, p2, len(target))
            new_population.append(mutate(c1, mutation_rate))
            if len(new_population) < population_size:
                new_population.append(mutate(c2, mutation_rate))
        population = new_population
    return best, generations
