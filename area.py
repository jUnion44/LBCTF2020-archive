import math, argparse
parser = argparse.ArgumentParser(description="Put in a decimal between 2.0 and 4.0 and see what the mys$parser.add_argument('--inValue', required=True, type=float, help='A decimal between 2.0 and 4.0'")
args = parser.parse_args()
myInput = args.inValue
myOutput = math.exp(myInput ** 2) / (math.sin(myInput) + 2)
print(myOutput)
