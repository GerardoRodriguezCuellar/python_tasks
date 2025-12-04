n_text = input("Enter number of rows: ")

# Validate input
try:
    n = int(n_text)
except:
    print()
    print("Error: invalid input")
    exit()

if n < 1:
    print()
    print("Error: invalid input")
    exit()

# Normal pattern
print()
print("Triangle:")
print()
for i in range(1, n + 1):
    line = ""
    for j in range(i):
        line = line + "*"
    print(line)

# Inverted pattern (optional extension)
print()
print("Inverted triangle:")
print()
for i in range(n, 0, -1):
    line = ""
    for j in range(i):
        line = line + "*"
    print(line)