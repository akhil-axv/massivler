def main():
    text = input("Sózdi kiritiń: ")
    letters = list(text)

    print("\n1. Hariplerdi sortlaw")
    print("2. Keri tártipte kórsetiw")
    print("3. Birinshi haripti bas harip etiw")
    print("4. Barlıq hariplerdi bas harip etiw")
    print("5. Listti tazalaw")

    choice = input("Ámeldi tańlań (1-5): ").strip()

    if choice == "1":
        letters.sort()
        print("".join(letters))
    elif choice == "2":
        print("".join(reversed(letters)))
    elif choice == "3":
        print(text.capitalize())
    elif choice == "4":
        print(text.upper())
    elif choice == "5":
        letters.clear()
        print("List tazalandı:", letters)
    else:
        print("Qáte tańlaw. 1 den 5 ke shekem san kiritiń.")


if __name__ == "__main__":
    main()
