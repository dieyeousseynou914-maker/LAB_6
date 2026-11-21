mot = input("Veuillez entrer un mot!\n")
Nb_voyelle = 0
for i in range(len(mot)):
    if mot[i] in ('a', 'e', 'i', 'o', 'u', 'y'):
        Nb_voyelle += 1

print("Le nombre de voyelles de votre mot est: ",Nb_voyelle)