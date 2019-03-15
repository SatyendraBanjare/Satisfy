import sys

def check_format(filename):
	variables, clauses = -1,-1
	instance_strs = []
	f = open(filename, 'r')
    
    # Check the file type, raise exceptions if not .cnf file
    filename_check_str = (f.name).split(".")
    if filename_check_str[1] != "cnf": raise Exception("Not a CNF problem file")

    lines  = f.readlines()
    i = -1
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith('c'):
            continue
        elif line.startswith('p'): # problem statement
            x = line.split(" ")
            if (x[1] != "cnf") : raise Exception("not a cnf problem")
            variables, clauses = int(x[2]), int(x[3])
            for j in range(i+1, i+clauses+1):
                instance_strs.append(lines[j].strip('\n'))
        break

    return instance_strs
