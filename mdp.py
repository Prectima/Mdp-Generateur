import random
import string

# Définir l'ensemble des caractères possibles pour le mot de passe
characters = string.ascii_letters + string.digits + string.punctuation

# Demander à l'utilisateur de saisir la longueur du mot de passe
nmb = int(input("Combien de caractères pour votre mot de passe (conseillé 8) : "))

# Initialiser une variable pour stocker le mot de passe
mdp = ""

# Générer le mot de passe en choisissant des caractères aléatoires
for i in range(nmb):
    mdp += random.choice(characters)

# Afficher le mot de passe généré
print("Votre mot de passe généré est :", mdp)
