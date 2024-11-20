import os

def run_lab(lab_number):
    os.system(f'python lab{lab_number}/runner.py')

def main():
    while True:
        print("\nSelect a lab to run:")
        for i in range(1, 9):
            print(f"{i}. Lab work {i}")
        print("0. Exit")

        choice = input("Your choice: ")

        if choice == '0':
            print("Exit.")
            break
        elif choice in map(str, range(1, 9)):
            run_lab(choice)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
