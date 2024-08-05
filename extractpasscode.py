"""
SHREEJI PATEL
PROJECT 1
CID PASSCODE EXTRACTOR
PROFESSOR SMITH
"""

# Function to find the first and last digit in a line
def find_digits(line):
    first_digit = None
    last_digit = None
    for char in line:  # Loop through each character in the line
        if '0' <= char <= '9':  # If the character is a digit
            if first_digit is None:  # If it's the first digit we've found
                first_digit = char
            last_digit = char  # Update the last digit found
    return first_digit, last_digit

# Function to compute the value from the first and last digit
def compute_value(first_digit, last_digit):
    if first_digit is None:  # If no digit was found in the line
        return -1
    if first_digit == last_digit:  # If only one digit was found in the line
        return int(first_digit) * 11
    return int(last_digit) * 10 + int(first_digit)  # If more than one digit was found, switch and combine them

# Function to remove leading and trailing spaces from a line
def trim_spaces(line):
    start_index = 0
    end_index = len(line) - 1
    while start_index <= end_index and line[start_index] == ' ':  # Find the first non-space character
        start_index += 1
    while end_index >= start_index and line[end_index] == ' ':  # Find the last non-space character
        end_index -= 1
    return line[start_index:end_index+1]  # Return the trimmed line

# Main function to extract the passcode
def extract_passcode():
    print("---CID Passcode Extractor---")
    passcode = ""
    previous_value = None

    while True:
        line = input("Enter line: ")  # Read a line from the user
        if line == "end":  # If the user wants to end the input
            break

        line = trim_spaces(line)  # Remove leading and trailing spaces from the line
        first_digit, last_digit = find_digits(line)  # Find the first and last digit in the line
        value = compute_value(first_digit, last_digit)  # Compute the value from the first and last digit

        if value == -1:  # If no digit was found in the line
            if previous_value is not None:  # If there was a previous value
                passcode = passcode[:-2]  # Remove the last two characters from the passcode
            print("\t-1 extracted")  # Tabbed output for -1 extracted
        else:  # If a digit was found in the line
            passcode += f"{value:02}"  # Add the value to the passcode
            previous_value = value  # Update the previous value
            print(f"\t{value:02} extracted")  # Tabbed output for extracted value

    if passcode == "":  # If no passcode was extracted
        print("No passcode was extracted.")
    else:  # If a passcode was extracted
        print(f"The passcode is: {passcode}")  # Print the passcode

# Call the main function
if __name__ == "__main__":
    extract_passcode()
