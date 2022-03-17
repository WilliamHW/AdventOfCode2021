from get_aoc import get_input

raw_input = get_input(14)

template, raw_rules = raw_input.split("\n\n")
#print(points)

rules = [rule.split(" -> ") for rule in raw_rules.split("\n")]

def check_rules (pair, rules): #Two character string to find resulting letter to add between
    for rule in rules:
        if rule[0] == pair: return rule [1]

number_of_steps = 40
polymer = template
for step in range(number_of_steps):
    new_polymer = polymer[0]
    for first_pair_place in range(len(polymer) - 1):
        pair = polymer[first_pair_place] + polymer[first_pair_place + 1]
        new_polymer += check_rules(pair, rules)
        new_polymer += polymer[first_pair_place + 1]
    polymer = new_polymer
    #for each pair

print("The polymer length is " + str(len(polymer)))

def ecart (polymer):
    b = polymer.count("B")
    c = polymer.count("C")
    f = polymer.count("F")
    h = polymer.count("H")
    k = polymer.count("K")
    n = polymer.count("N")
    o = polymer.count("O")
    p = polymer.count("P")
    s = polymer.count("S")
    v = polymer.count("V")
    group = {b, c, f, h, k, n, o, p, s, v}
    #print(group)
    #group.remove(0)
    #print(group)
    #print(max(group))
    #print(min(group))
    return (max(group) - min(group))

print("After " + str(number_of_steps) + " number of steps, the ecart is " + str(ecart(polymer)))
#2797 was the answer for part one with a polymer length of 19457


