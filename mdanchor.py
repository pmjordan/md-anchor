import re

def add_anchors_to_markdown(input_file_path, output_file_path, text_to_add):
    # Define the pattern you want to match
    pattern = re.compile(r'^([#])+\s([0-9]+)')

    # Open the input file for reading and the output file for writing
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        # Process each line in the input file
        for line in infile:
            # If the line matches the pattern, add the text
            if pattern.search(line):

                # Tokenize the line
                tokens = line.split()
                
                # Ignore the first token and concatenate the rest with an underscore
                if len(tokens) > 1:
                    line=tokens[0]+' ('+' '.join(tokens[1:])+')'
                    concatenated_tokens = '_'.join(tokens[2:]).lower()
                    
                    #print(concatenated_tokens)

                line = line.strip() + ' ' + text_to_add 
                line = line.strip()+ '\n'
            # Write the (possibly modified) line to the output file
            outfile.write(line)

    print(f'Processed lines written to {output_file_path}')

# Example usage:
add_anchors_to_markdown('test.md', 'output.md', '')
