class Entry:
    def __init__(self, word):
        self.word = word
        self.meanings = []

    def add_meaning(self, part_of_speech, definition, example):
        self.meanings.append({"part_of_speech": part_of_speech, "definition": definition, "example": example})

    def __str__(self):
        output = f"{self.word}:\n"
        for meaning in self.meanings:
            output += f"  {meaning['part_of_speech']}: {meaning['definition']}\n"
            output += f"    Example: {meaning['example']}\n"
        return output

class Dictionary:
    def __init__(self):
        self.entries = []

    def add_entry(self, word):
        entry = Entry(word)
        self.entries.append(entry)
        return entry

    def remove_entry(self, word):
        for entry in self.entries:
            if entry.word == word:
                self.entries.remove(entry)
                return True
        return False

    def find_entry(self, word):
        for entry in self.entries:
            if entry.word == word:
                return entry
        return None

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for entry in self.entries:
                file.write(str(entry) + "\n")

    def load_from_file(self, filename):
        self.entries = []
        part_of_speech,definition,example = "",'',''
        with open(filename, "r") as file:
            current_entry = None
            for line in file:
                line = line.rstrip()
                if line:
                    if line.endswith(":") and not line.startswith(" "):
                        word = line[:-1]
                        current_entry = self.add_entry(word)
                    elif line.startswith(" "):
                        if "Example" not in line:
                            part_of_speech , definition = line.split(":")
                            part_of_speech = part_of_speech.strip()
                            definition = definition.strip()
                        elif "Example" in line:
                            example = line.strip(":")
                            example = example.strip(" Example:")
                            current_entry.add_meaning(part_of_speech, definition, example)
                            part_of_speech,definition,example = "",'',''


def main():
    dictionary = Dictionary()

    while True:
        print("\nMenu:")
        print("1. Add a new entry")
        print("2. Remove an entry")
        print("3. Look up an entry")
        print("4. Save dictionary to file")
        print("5. Load dictionary from file")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            word = input("Enter the word: ")
            entry = dictionary.add_entry(word)
            while True:
                part_of_speech = input("Enter the part of speech (or 'q' to quit): ")
                if part_of_speech.lower() == "q":
                    break
                definition = input("Enter the definition: ")
                example = input("Enter an example (or leave blank): ")
                entry.add_meaning(part_of_speech, definition, example)

        elif choice == "2":
            word = input("Enter the word to remove: ")
            if dictionary.remove_entry(word):
                print(f"Entry '{word}' removed successfully.")
            else:
                print(f"Entry '{word}' not found in the dictionary.")

        elif choice == "3":
            word = input("Enter the word to look up: ")
            entry = dictionary.find_entry(word)
            if entry:
                print(entry)
            else:
                print(f"Entry '{word}' not found in the dictionary.")

        elif choice == "4":
            filename = input("Enter the filename to save the dictionary: ")
            dictionary.save_to_file(filename)
            print(f"Dictionary saved to '{filename}'.")

        elif choice == "5":
            filename = input("Enter the filename to load the dictionary from: ")
            dictionary.load_from_file(filename)
            print(f"Dictionary loaded from '{filename}'.")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()