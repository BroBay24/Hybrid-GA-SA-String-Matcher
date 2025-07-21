import random
import string
import math

def calculate_fitness(candidate, target):
    return sum(1 for a, b in zip(candidate, target) if a == b)

def random_neighbor(s):
    # Ganti satu karakter secara acak
    idx = random.randint(0, len(s) - 1)
    new_char = random.choice(string.ascii_uppercase + " ")
    return s[:idx] + new_char + s[idx+1:]

def run_simulated_annealing(initial_string, target, initial_temp=100.0, cooling_rate=0.95, min_temp=0.1, max_iter=1000):
    current = initial_string
    current_fitness = calculate_fitness(current, target)
    best = current
    best_fitness = current_fitness
    temp = initial_temp

    for i in range(max_iter):
        if current == target:
            break

        candidate = random_neighbor(current)
        candidate_fitness = calculate_fitness(candidate, target)

        if candidate_fitness > current_fitness:
            current = candidate
            current_fitness = candidate_fitness
        else:
            prob = math.exp((candidate_fitness - current_fitness) / temp)
            if random.random() < prob:
                current = candidate
                current_fitness = candidate_fitness

        if current_fitness > best_fitness:
            best = current
            best_fitness = current_fitness

        temp *= cooling_rate
        if temp < min_temp:
            break

    return best, best_fitness
