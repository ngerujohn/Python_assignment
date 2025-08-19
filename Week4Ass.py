# File Read & Write Challenge 🖋️

# Open the original file for reading
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify the content (example: convert to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("Modified content has been written to output.txt ✅")



# Error Handling Lab 🧪

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

except FileNotFoundError:
    print("❌ Error: The file does not exist.")








