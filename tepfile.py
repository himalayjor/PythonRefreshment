import tempfile

fd, filename = tempfile.mkstemp()

with open(filename, "w") as tmp:
    tmp.write("some content")

print(filename)