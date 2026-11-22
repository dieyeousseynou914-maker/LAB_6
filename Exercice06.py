Username = input("Veuillez entrer votre nom d'utilisateur!\n")
if Username.isalnum() and len(Username) >= 5:
    print("Nom d'utilisateur valide!")
else:
    print("Nom d'utilisateur invalide")
