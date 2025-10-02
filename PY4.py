# File Handling and Exception Handling Assignment

def file_read_write():
    try:
        # Ask user for input file
        filename = input("Enter the filename to read: ")

        # Try to open the file
        with open(filename, "r") as file:
            content = file.readlines()

        # Modify content (example: uppercase with line numbers)
        modified_content = [f"{i+1}: {line.strip().upper()}\n" for i, line in enumerate(content)]

        # Write to a new file
        with open("output.txt", "w") as new_file:
            new_file.writelines(modified_content)

        print(" File has been processed successfully! Check output.txt.")

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


# Run the function
file_read_write()
