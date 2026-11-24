chaine = input("Veuillez entrer une chaine!")
Nb_lettre = 0
Nb_chiffre = 0
Nb_space = 0
for i in range(len(chaine)):
    if chaine[i].isalpha():
        Nb_lettre += 1
    elif chaine[i].isdigit():
        Nb_chiffre += 1
    elif chaine[i].isspace():
        Nb_space += 1

print(f"""Le nombre de lettre dans la chaine est: {Nb_lettre}
        Le nombre de chiffre dans a chaine est: {Nb_chiffre} 
        et le nombre d'espaces dans la chaine est: {Nb_space}""")
