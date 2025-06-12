def sort_file(input_file,output_file):
    try:
        with open(input_file,'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        return 'File not found error'
    
    lines = [line.strip() for line in lines]
    lines.sort()

    with open(output_file,'w') as file:
        for line in lines:
            file.write(line + '\n')

    print("The sorted file is in the {output_file}")

input_file = 'input.txt'
output_file = 'output_sorted.txt'
sort_file(input_file,output_file)