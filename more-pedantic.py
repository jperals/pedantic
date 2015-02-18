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

conjunctions = [
    ", but ",
    ", however ",
    ", nonetheless ",
    " as much as ",
    " inasmuch as ",
    ". However, ",
    ", even though ",
    " just like "
]

def simple_sentence():
    random_adjective_1 = random.choice(adjectives)
    random_noun_1 = random.choice(nouns)
    random_verb = random.choice(verbs)
    random_adjective_2 = random.choice(adjectives)
    random_noun_2 = random.choice(nouns)
    sentence = random_adjective_1 + " " + random_noun_1 + " " + random_verb + " " + random_adjective_2 + " " + random_noun_2
    return sentence

simple_sentence_1 = simple_sentence()
simple_sentence_2 = simple_sentence()
conjunction = random.choice(conjunctions)
compund_sentence = simple_sentence_1 + conjunction + simple_sentence_2
print(compund_sentence)
