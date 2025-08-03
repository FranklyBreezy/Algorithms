import argparse
import numpy as np
import sys

def parse_matrix_string(s: str) -> np.ndarray:
    try:
        rows = s.strip().split(';')
        matrix = [list(map(float, row.strip().split())) for row in rows]
        return np.array(matrix)
    except Exception as e:
        raise ValueError(f"Invalid matrix string format: {e}")

def read_matrix_file(path: str) -> np.ndarray:
    try:
        return np.loadtxt(path, delimiter=',')
    except Exception as e:
        raise ValueError(f"Failed to read matrix file '{path}': {e}")

def add_matrices(a, b):
    if a.shape != b.shape:
        raise ValueError("Matrices must have the same shape for addition.")
    return a + b

def multiply_matrices(a, b):
    if a.shape[1] != b.shape[0]:
        raise ValueError("Inner matrix dimensions must agree for multiplication.")
    return a @ b

def main():
    parser = argparse.ArgumentParser(description="Mini NumPy Matrix Calculator CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_common_args(p):
        group = p.add_mutually_exclusive_group(required=True)
        group.add_argument('--a', type=str, help='Matrix A as inline string, e.g. "1 2;3 4"')
        group.add_argument('--a-file', type=str, help='Path to file containing matrix A (CSV)')
        group2 = p.add_mutually_exclusive_group(required=True)
        group2.add_argument('--b', type=str, help='Matrix B as inline string')
        group2.add_argument('--b-file', type=str, help='Path to file containing matrix B (CSV)')

    # Add command
    parser_add = subparsers.add_parser('add', help='Add two matrices')
    add_common_args(parser_add)

    # Multiply command
    parser_mul = subparsers.add_parser('multiply', help='Multiply two matrices')
    add_common_args(parser_mul)

    # Transpose command
    parser_transpose = subparsers.add_parser('transpose', help='Transpose a matrix')
    group = parser_transpose.add_mutually_exclusive_group(required=True)
    group.add_argument('--a', type=str, help='Matrix as inline string, e.g. "1 2;3 4"')
    group.add_argument('--a-file', type=str, help='Path to file containing matrix (CSV)')

    args = parser.parse_args()

    # Parse matrices
    def get_matrix(arg_inline, arg_file):
        if arg_inline:
            return parse_matrix_string(arg_inline)
        else:
            return read_matrix_file(arg_file)

    try:
        if args.command in ['add', 'multiply']:
            a = get_matrix(args.a, args.a_file)
            b = get_matrix(args.b, args.b_file)
            if args.command == 'add':
                result = add_matrices(a, b)
            else:
                result = multiply_matrices(a, b)
        elif args.command == 'transpose':
            a = get_matrix(args.a, args.a_file)
            result = a.T
        else:
            print("Unsupported command", file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Print result nicely
    np.set_printoptions(precision=4, suppress=True)
    print("Result:")
    print(result)

if __name__ == "__main__":
    main()
