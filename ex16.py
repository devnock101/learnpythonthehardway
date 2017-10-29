from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

# print("Truncating the file. Goodbye!")
#target.truncate()

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
new_line = ("\n")

print("I'm going to write these to the file.")

target.write(line1 + new_line + line2 + new_line + line3 + new_line)

print("And finaly, we close it.")
target.close()