# file_modes_demo.py

# 🔹 1. 'r' – Read mode
# First, create a file to read from
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# Now read it
with open("example.txt", "r") as f:
    content = f.read()
    print("Read mode:", content)


# 🔹 2. 'w' – Write mode (overwrites existing file)
with open("example.txt", "w") as f:
    f.write("Overwritten content.")

# Read to verify
with open("example.txt", "r") as f:
    print("Write mode:", f.read())


# 🔹 3. 'a' – Append mode
with open("example.txt", "a") as f:
    f.write("\nAppended line.")

# Read to verify
with open("example.txt", "r") as f:
    print("Append mode:\n", f.read())


# 🔹 4. 'b' – Binary mode
# Write binary data
with open("binary_file.bin", "wb") as f:
    f.write(b'\x00\x01\x02\x03')

# Read binary data
with open("binary_file.bin", "rb") as f:
    binary_data = f.read()
    print("Binary mode:", binary_data)


# 🔹 5. 'x' – Exclusive creation mode
try:
    with open("new_file.txt", "x") as f:
        f.write("This file is created exclusively.")
    print("Exclusive creation: File created.")
except FileExistsError:
    print("Exclusive creation: File already exists.")
