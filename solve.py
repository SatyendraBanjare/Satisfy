'''
TO do : generate a boolean expression from given cnf file.
		apply dpll algo and solve
'''

import sys
import json

def main(argv=None):

  if argv is None: argv = sys.argv
  if len(argv) != 2:
    print "Usage: %s <cnf_file>	" % argv[0]
    return 1
  return 0

if __name__ == "__main__":
  sys.exit(main())

