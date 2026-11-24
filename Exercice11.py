carte = input("Veuillez entrer votre numéro de carte : ")

carte = carte.replace(" ", "").replace("-", "")

if not carte.isdigit():
    print("Erreur : le numéro de carte ne doit contenir que des chiffres.")
elif len(carte) < 16:
    print(f"Erreur : le numéro est trop court ({len(carte)} chiffres au lieu de 16).")
elif len(carte) > 16:
    print(f"Erreur : le numéro est trop long ({len(carte)} chiffres au lieu de 16).")
else:
    masque = "*" * 12 + carte[-4:]
    print(f"Numéro masqué : {masque}")