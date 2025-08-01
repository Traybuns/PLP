def modify_content(content):
    
    return content.upper()

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as infile:
            content = infile.read()
            print("File read successfully ✅")

        modified_content = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"Modified content written to {new_filename} 📝")

    except FileNotFoundError:
        print(" Error: File not found. Please check the name and try again.")
    except IOError:
        print(" Error: Could not read or write the file.")

if __name__ == "__main__":
    main()
