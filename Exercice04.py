mot = input("Veuillez entrer un mot!")
if mot[::-1] == mot:
    print("Votre mot est un palindrome.")
else:
    print("Votre mot n'est pas un palindrome.")