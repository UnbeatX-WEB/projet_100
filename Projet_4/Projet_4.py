def main():
    print("=== Mini Python Script ===")
    print("1. Say hello")
    print("2. Add two numbers")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Your name: ")
        print(f"Hello {name}!")

    elif choice == "2":
        a = float(input("Number 1: "))
        b = float(input("Number 2: "))
        print("Result:", a + b)

    elif choice == "3":
        print("Goodbye!")

    else:
        print("Invalid option.")

main()
