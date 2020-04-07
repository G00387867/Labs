import sys

try:
    with open(sys.argv[1]) as f:
        print(f.read())

except FileNotFoundError:
    print("file " + sys.argv[1] + " does not exist")
except:
    print("This is the zero division error handler")
