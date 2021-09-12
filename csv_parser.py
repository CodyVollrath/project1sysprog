"""
This script file is deals with reading data from a file
and parsing csv data seperatly
"""
def get_file_data(filename):
    """
    Gets the file content from the file path that is passed into the function
    Returns: content of file if opened and None
    if an IOError occurs because file can not be opened and displays the error message
    """
    content = None
    try:
        with open(filename) as input_file:
            content = input_file.read()
        input_file.close()
        return content
    except IOError as error:
        print('Error:', error)

def parse_csv(csv_str):
    """
    Takes the CSV data from the passed in string and converts it into a dict
    Args: csv_str - the csv string to be parsed
    Returns: the dict of the csv data
    """
    data_map = {}
    line_split_csv = csv_str.split('*')
    for element in line_split_csv:
        fields = element.split(';')
        data_map[fields[0]] = fields[1:]
    data_map.pop('')
    return data_map
