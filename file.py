def process_file():
    """Read a file, modify its content, and write to a new file with error handling."""
    
    # 🧪 Error Handling Lab: Get filename with validation
    while True:
        input_filename = input("Enter the input filename: ")
        output_filename = input("Enter the output filename: ")
        
        try:
            # 🖋️ File Read & Write Challenge
            with open(input_filename, 'r') as infile:
                content = infile.read()
            
            # Modify the content (example: convert to uppercase)
            modified_content = content.upper()
            
            # Write to new file
            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)
            
            print(f"Success! Modified content written to {output_filename}")
            break
            
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' doesn't exist. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied when accessing '{input_filename}'. Please check file permissions.")
        except IOError as e:
            print(f"Error: An I/O error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    process_file()