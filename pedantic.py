import random

nouns = [
    "progress",
    "solitude",
    "aura",
    "interpretation",
    "sacrifice",
    "meaning",
    "meaningfulness",
    "meaninglessness",
    "effort",
    "focus",
    "idiocy",
    "intelligence",
    "knowledge",
    "fear",
    "identification",
    "value",
    "curiosity",
    "manipulation",
    "ignorance",
    "literacy"
]

verbs = [
    "entails",
    "yields",
    "means",
    "contains",
    "provides",
    "retains",
    "provokes",
    "leads to",
    "implies",
    "requires",
    "prevents",
    "equates to"
]

adjectives = [
    "unlimited",
    "constant",
    "minimal",
    "artistic",
    "superior",
    "immediate",
    "superb",
    "ethereal",
    "ephemeral",
    "contemporary",
    "further"
]

random_adjective_1 = random.choice(adjectives)
random_noun_1 = random.choice(nouns)
random_verb = random.choice(verbs)
random_adjective_2 = random.choice(adjectives)
random_noun_2 = random.choice(nouns)
sentence = random_adjective_1 + " " + random_noun_1 + " " + random_verb + " " + random_adjective_2 + " " + random_noun_2 + "."
print(sentence)
