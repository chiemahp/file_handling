
def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Line 1: Hello, World!\n")
            file.write("Line 2: Python is fun.\n")
            file.write("Line 3: 1234567890\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Line 4: Appending new line.\n")
            file.write("Line 5: Another line.\n")
            file.write("Line 6: 9876543210\n")
        print("Lines appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_file()
    read_file()
    append_file()
    read_file()

if __name__ == "__main__":
    main()