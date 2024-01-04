def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    valid_extensions = {'txt', 'exe', 'dll'}
    name_parts = file_name.split('.')

    # Check if the file's name contains exactly one dot
    if len(name_parts) != 2:
        return 'No'

    name, extension = name_parts

    # Check if the file's name starts with a latin alphabet letter and the extension is valid
    if not (name and name[0].isalpha() and extension in valid_extensions):
        return 'No'

    # Check if there are more than three digits in the file's name
    if sum(c.isdigit() for c in name) > 3:
        return 'No'

    return 'Yes'