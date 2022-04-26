liste = list("123456789")

def bruteforce(word, length):
    global list, mdp
    if length <= 4:
        for letter in liste:
            if mdp == word + letter:
                print("Votre mot de passe est " + word + letter)
            else:
                bruteforce(word + letter, length + 1)



mdp = "4684"
bruteforce('', 1)