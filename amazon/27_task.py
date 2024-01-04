def read_file(file):
    """
    Read the content of the file and return it in lowercase.
    If the file does not exists return an empty string.

    Example
    read_file("test.txt") == "hello world"
    read_file("asd") == ""
    """
    try:
        with open(file, "r") as f:
            content = f.read()
        return content.lower()
    except FileNotFoundError:
        return ""