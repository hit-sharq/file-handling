def process_file():
    """
    This function processes a text file by reading its content, converting it to uppercase,
    and writing the modified content to a new file.
    """
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            print(f"Successfully read {len(content)} characters from {input_filename}")

        # Convert content to uppercase and write to new file
        modified_content = content.upper()
        # Determine output file name based on input file name
        if '.' in input_filename:
            base, ext = input_filename.rsplit('.', 1)
            output_filename = f"{base}_modified.{ext}"
        else:
            output_filename = f"{input_filename}_modified"

        # Write modified content to output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            print(f"Successfully wrote modified content to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{input_filename}'.")
    except IOError as e:
        print(f"Error reading the file: {e}")
    except UnicodeDecodeError:
        print(f"Error: The file '{input_filename}' contains characters that cannot be decoded.")
    except Exception as e:
        print(f"Unexpected error: {e}")

        
if __name__ == "__main__":
    print("File Processor - Read, Modify, and Write")
    print("----------------------------------------")
    process_file()
