phrase = input("Veuillez entrer une phrase")
Nb_maj = 0
Nb_min = 0
phrase.strip()
for i in range(len(phrase)):
    if phrase[i].islower():
        Nb_min += 1
    elif phrase[i].isupper():
        Nb_maj += 1

print("Le nombre de lettres minuscules dans la phrase est: ",Nb_min)
print("Le nombre de lettres majuscules dans la phrase est: ",Nb_maj)