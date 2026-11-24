mot_de_passe = input("Veuillez entrer un mot de passe : ")

caracteres_speciaux = "!@#$%^&*()-_=+[]{};:,.<>?/|~"

criteres = {
    "Au moins 8 caractères": len(mot_de_passe) >= 8,
    "Au moins une lettre majuscule": any(c.isupper() for c in mot_de_passe),
    "Au moins une lettre minuscule": any(c.islower() for c in mot_de_passe),
    "Au moins un chiffre": any(c.isdigit() for c in mot_de_passe),
    "Au moins un caractère spécial": any(c in caracteres_speciaux for c in mot_de_passe),
}

print("\nRésultats :")
for description, respecte in criteres.items():
    if respecte:
        print(f"Vrai:{description}")
    else:
        print(f"Faux:{description}")

if all(criteres.values()):
    print("\nMot de passe valide.")
else:
    print("\nMot de passe invalide : certains critères ne sont pas respectés.")