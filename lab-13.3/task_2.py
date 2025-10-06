def read_file(filename):
    """
    Read the contents of a file.

    Parameters:
    -----------
    filename : str
        The path to the file to be read.

    Returns:
    --------
    str
        The contents of the file.

    Raises:
    -------
    FileNotFoundError
        If the file does not exist.
    IOError
        If there is an error reading the file.
    """
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace 'example.txt' with a valid file path to test
        print(read_file("example.txt"))
    except Exception as e:
        print(e)