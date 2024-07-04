input_file = 'rr.txt'
output_file = 'cleaned_requirements.txt'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        clean_line = line.split('@')[0].strip()  # Split at '@' and take the part before it
        if clean_line:  # Write non-empty lines
            outfile.write(clean_line + '\n')
