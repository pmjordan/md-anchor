import re

# ways to do anchor

#\[See “nil”, below\](#nil)
#  #### 9.1.1.6 nil 
#but the slug includes 9116

# so use
# ### This is the Heading <a name="this-is-the-heading"></a>


def add_anchors_to_markdown(input_file_path, output_file_path):
    # Define the pattern you want to match
    pattern = re.compile(r'^([#])+\s([0-9]+)')
    anchor_pattern = re.compile(r'><\/a>\s*$')

    # Open the input file for reading and the output file for writing
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        # Process each line in the input file
        for line in infile:
            # If the line matches the pattern, add the text
            if pattern.search(line):

                #check the line doesn't already have an anchor
                if not anchor_pattern.search(line):

                # This line needs processing
                    # Tokenize the line
                    tokens = line.split()
                    
                    # Ignore the first token and concatenate the rest with an underscore
                    if len(tokens) > 1:
                        slug = '-'.join(tokens[2:]).lower()
                        text_to_add ='<a name='+slug+'></a>'

                    line = line.strip() + ' ' + text_to_add +'\n'

            # Write the (possibly modified) line to the output file
            outfile.write(line)

    print(f'Processed lines written to {output_file_path}')

# Example usage:
add_anchors_to_markdown('input.md', 'output.md')
