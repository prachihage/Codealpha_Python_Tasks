import re

# Open the input file
file = open("input.txt", "r")

# Read all text from the file
text = file.read()

# Find all email addresses
emails = re.findall(r"\S+@\S+", text)

# Create output file
output = open("emails.txt", "w")

# Save each email in a new line
for email in emails:
    output.write(email + "\n")

# Close both files
file.close()
output.close()

print("Emails extracted successfully!")