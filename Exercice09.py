phrase = input("Veuillez entrer une phrase!\n")
plus_long = ""
for mot in phrase.split():
    if len(mot) > len(plus_long):
        plus_long = mot

print(f"Le plus long mot de la phrase est: {plus_long}")