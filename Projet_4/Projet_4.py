def main():
    print("=== Mini Script Python ===")
    print("1. Dire bonjour")
    print("2. Additionner deux nombres")
    print("3. Quitter")

    choix = input("Choisis une option : ")

    if choix == "1":
        nom = input("Ton nom : ")
        print(f"Bonjour {nom} !")  # f-string corrigée

    elif choix == "2":
        a = float(input("Nombre 1 : "))
        b = float(input("Nombre 2 : "))
        print("Résultat :", a + b)

    elif choix == "3":
        print("Au revoir !")

    else:
        print("Option invalide.")

main()