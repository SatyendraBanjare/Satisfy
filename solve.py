import sys
from dpll import *
from format import *

def main(filename):
    instance_strs = check_format(filename)
    solver(instance_strs)
   
if __name__ == "__main__":
    main(sys.argv[1])
