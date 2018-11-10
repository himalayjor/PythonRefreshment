from sys import argv

scriptname, filename = argv

file = open(filename)

print(file.read())