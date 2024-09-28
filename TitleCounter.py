import os

class TitleCounter:
    """
    A class to count unique and duplicate titles from multiple text files.
    """
    def __init__(self, files):
        """
        Initializes the TitleCounter with a list of file paths.

        Args:
            files (list): A list of file paths to text files containing titles.
        """
        self.files = files
        self.title_counts = {}

    def _read_titles_from_files(self):
        """
        Reads titles from the specified text files and stores them in the title_counts dictionary.
        """
        for file in self.files:
            if os.path.exists(file):
                with open(file, 'r', encoding='utf-8') as f:
                    for line in f:
                        title = line.strip()
                        if title:  # Only add non-empty lines
                            # Count occurrences of each title
                            if title in self.title_counts:
                                self.title_counts[title] += 1
                            else:
                                self.title_counts[title] = 1

    def count_titles(self):
        """
        Calculates the total number of unique titles and duplicates.

        Returns:
            tuple: A tuple containing total unique titles and total duplicate titles.
        """
        # Read and count titles from files
        self._read_titles_from_files()

        # Calculate unique and duplicate titles
        unique_titles = len(self.title_counts)
        duplicate_titles = sum(count - 1 for count in self.title_counts.values() if count > 1)

        return unique_titles, duplicate_titles


