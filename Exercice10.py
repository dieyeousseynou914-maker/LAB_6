carte = input("Veuillez entrer votre numéro de carte : ")
masque = "*" * (len(carte) - 4) + carte[-4:]
print(masque)