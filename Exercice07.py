adresse = input("Veuillez entrer un adresse courriel!")
if ('@' in adresse) and ('.' in adresse) and (adresse.index('@') == adresse.index('.') - 1):
    print("Votre adresse courriel est correcte!")
else:
    print("Votre adresse n'est pas correcte!")