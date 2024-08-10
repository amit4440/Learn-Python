""" import sys
import fileinput

x = input("text to be replaced:")
y = input("new text:")

for l in fileinput.input(files = "file.txt"):
    l = l.replace(x, y)
    sys.stdout.write(l) """

search_text = "kumari"
replace_text = "jha"

with open(r'file.txt', 'r') as file:

    data = file.read()
    data = data.replace(search_text, replace_text)

with open(r'file.txt', 'w') as file:

    file.write(data)

print('txt replaced')