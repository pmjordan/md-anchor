import re


# ways to do anchor


#\[See “nil”, below\](#nil)
#  #### 9.1.1.6 nil 
#but the slug includes 9116

# so try 
# ### This is the Heading <a name="this-is-the-heading"></a>

# TODO add real anchors
# TODO don't add anchors to lines which already have them

def add_anchors_to_markdown(input_file_path, output_file_path):
    # Define the pattern you want to match
    pattern = re.compile(r'^([#])+\s([0-9]+)')
    text_to_add ='<a name="heading"></a>'
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
                    concatenated_tokens = '-'.join(tokens[2:]).lower()
                    text_to_add = '<a name="'+concatenated_tokens+'"></a>' 
                
                #remove the newline, add teh anchor and add a new line
                line = line.strip() + ' ' + text_to_add + '\n'
                
            # Write the (possibly modified) line to the output file
            outfile.write(line)

    print(f'Processed lines written to {output_file_path}')

# Example usage:
add_anchors_to_markdown('test.md', 'output.md')
