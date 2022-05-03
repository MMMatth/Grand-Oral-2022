char = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()_+-=[]{}|;':,./<>?")

def bruteforce(word, length):
    global list, mdp
    if length <= 7:
        for letter in char:
            if mdp == word + letter:
                print("Votre mot de passe est " + word + letter)
            else:
                bruteforce(word + letter, length + 1)



mdp = "jaehdui"
bruteforce('', 7)