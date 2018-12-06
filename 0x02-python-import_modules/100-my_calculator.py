#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    args = len(sys.argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>".format())
        sys.exit(1)
    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if op[0] == '+':
        print("{:d} + {:d} = {:d}".format(a, b, calc.add(a, b)))
        sys.exit(0)
    elif op[0] == '-':
        print("{:d} - {:d} = {:d}".format(a, b, calc.sub(a, b)))
        sys.exit(0)
    elif op[0] == '*':
        print("{:d} * {:d} = {:d}".format(a, b, calc.mul(a, b)))
        sys.exit(0)
    elif op[0] == '/':
        print("{:d} / {:d} = {:d}".format(a, b, calc.div(a, b)))
        sys.exit(0)
    elif (op[0] != '+') or (op[0] != '-') or (op[0] != '*') or (op[0] != '/'):
        print("Unknown operator. Available operators: +, -, * and /".format())
        sys.exit(1)
