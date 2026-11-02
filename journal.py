import datetime

FILENAME = "journal.txt"

def add_note():
    note = input("Write your note: ").strip()
    if not note:
        print("Empty note skipped.")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {note}\n")
    print("Note saved.")

def view_notes():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            notes = f.readlines()
    except FileNotFoundError:
        print("No notes yet. Add one first!")
        return

    if not notes:
        print("Journal is empty.")
        return

    print("\n--- Your Journal ---")
    for line in notes:
        print(line.strip())
    print("--------------------\n")

def main():
    while True:
        print("\n1. Add note")
        print("2. View notes")
        print("3. Quit")
        choice = input("Choose (1-3): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()