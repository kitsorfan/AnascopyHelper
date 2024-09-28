def extract_titles(input_file, output_file):
    """
    Extracts titles from a text file following a 4-line pattern and saves them to a new file.

    Args:
        input_file (str): Path to the input text file containing the 4-line pattern.
        output_file (str): Path to the output text file where cleaned titles will be saved.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        
        # Iterate through lines with a step of 4 to match the 4-line pattern
        for i in range(0, len(lines), 4):
            # Extract the title (first line in each 4-line pattern)
            title = lines[i].strip()  # Remove leading/trailing whitespace
            if title:  # Check if title is not empty
                outfile.write(title + '\n')  # Write the title to the output file


if __name__ == "__main__":
    # Example usage
    input_file = "scopus"
    output_file = "scopusC"
    for i in range(0,5):
        extract_titles(input_file+str(i+1)+".txt", output_file+str(i+1)+".txt")
        print(f"Titles have been extracted and saved to {output_file}.")
