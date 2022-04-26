import random

def simple_brute_force(password):
    character = list("123456789")
    tmp = ""
    while tmp != list(password):
        tmp = random.choices(list(character),k=len(password))
    return "Trouvé !"

print(simple_brute_force("175436849512"))