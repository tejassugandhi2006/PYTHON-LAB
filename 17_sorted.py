import os.path
import sys

fname = input("Enter the filename to sort: ")   # input file

# Check if file exists
if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

# Open and read file
infile = open(fname, "r")
lines = infile.readlines()   # list of lines from file
infile.close()               # close the input file

lineList = []   # Empty list

# Remove newline characters
for line in lines:
    lineList.append(line.strip())

# Sort the list
lineList.sort()

# Write to output file
outfile = open("sorted.txt", "w+")

for line in lineList:
    outfile.write(line + "\n")

outfile.close()

print("Sorted content written to sorted.txt")