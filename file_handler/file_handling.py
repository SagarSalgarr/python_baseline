def process_file_with_long_lines(file_path, chunk_size=4096):
    try:
        with open(file_path, 'r') as file:
            buffer = ''
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    # End of file
                    break
                
                buffer += chunk
                lines = buffer.split('\n')
                # Process lines
                for line in lines[:-1]:
                    print(line.strip())  # Process line (strip trailing newline)S
                buffer = lines[-1]  # Store the incomplete line for the next iteration
            
            # Process any remaining incomplete line
            if buffer:
                print(buffer.strip())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")

# Example usage:
file_path = 'file.txt'
process_file_with_long_lines(file_path)
