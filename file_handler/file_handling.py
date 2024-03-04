def process_file_with_long_lines(file_path, chunk_size=4096):
    try:
        with open(file_path, 'r') as file:
            buffer = ''
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                
                buffer += chunk
                lines = buffer.split('\n')
                for line in lines[:-1]:
                    print(line.strip())  
                buffer = lines[-1] 
            
            if buffer:
                print(buffer.strip())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")

file_path = 'file.txt'
process_file_with_long_lines(file_path)
