import argparse

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("operation", choices=["add", "subtract"], help="Operation to perform")
parser.add_argument("x", type=float, help="First number")
parser.add_argument("y", type=float, help="Second number")

args = parser.parse_args()

if args.operation == "add":
    result = add(args.x, args.y)
elif args.operation == "subtract":
    result = subtract(args.x, args.y)
elif args.operation == "multiply":
    result = multiply(args.x, args.y)

print(f"Result: {result}")