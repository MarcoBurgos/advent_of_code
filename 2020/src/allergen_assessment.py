import re
import math
import itertools
import numpy as np
from collections import defaultdict
from utils import read_and_load_input

class Food:
    def __init__(self, ingredients, allergens):
        self.ing = set(ingredients)
        self.allerg = set(allergens)

    def __repr__(self):
        ingr = ' '.join(self.ing)
        allerg = ', '.join(self.allerg)
        return f"{ingr} ({allerg})"

def allergen_assessment_1():
    input = read_and_load_input("DAY21")
    foods = []
    ingredients = set()
    allergens = set()

    allergen_probable_map = defaultdict(list)
    for line in input:
        ingr_re = re.match(r"(.*?)\(contains (.*?)\)", line)
        ingrs = [x for x in ingr_re.group(1).split(' ') if x]
        allergs = [x for x in ingr_re.group(2).split(', ') if x]
        ingredients.update(ingrs)
        allergens.update(allergs)
        food = Food(ingrs, allergs)
        foods.append(food)

    could_allergens = set()
    for a in allergens:
        ingr_sets = []
        for f in foods:
            if a in f.allerg:
                ingr_sets.append(f.ing)
        if len(ingr_sets) > 1:
            could_allergens.update(ingr_sets[0].intersection(*ingr_sets[1:]))
        else:
            could_allergens.update(ingr_sets[0])


    not_allergens = ingredients - could_allergens

    ingr_occur_map = defaultdict(int)
    for f in foods:
        for ing in not_allergens:
            if ing in f.ing:
                ingr_occur_map[ing] += 1

    solution = sum(list(ingr_occur_map.values()))
    return solution,foods,not_allergens,allergens

def allergen_assessment_2(foods, not_allergens,allergens):
    for f in foods:
        f.ing -= not_allergens

    eng_candidate_map = {a: None for a in allergens}

    for a in allergens:
        ingr_sets = []
        for f in foods:
            if a in f.allerg:
                ingr_sets.append(f.ing)
        if len(ingr_sets) > 1:
            intersection = ingr_sets[0].intersection(*ingr_sets[1:])
        else:
            intersection = ingr_sets[0]

        eng_candidate_map[a] = intersection

    eng_gib_map = {a: None for a in allergens}
    not_processed = set(allergens)
    while eng_candidate_map:
        for a, gibs in eng_candidate_map.items():
            if len(gibs) == 1:
                break
        eng_gib_map[a] = list(gibs)[0]
        del eng_candidate_map[a]
        for a in eng_candidate_map:
            eng_candidate_map[a] -= gibs

    gib_eng_map = {
        gib: eng for eng, gib in eng_gib_map.items()
    }
    dang_list = list(eng_gib_map.values())
    dang_list.sort(key=lambda x: gib_eng_map[x])

    return ','.join(dang_list)

if __name__ == '__main__':
    solution, foods, not_allergens,allergens = allergen_assessment_1()
    print(f"Solution 1: {solution}")
    print(f"Solution 2: {allergen_assessment_2(foods, not_allergens,allergens)}")
