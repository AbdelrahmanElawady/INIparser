def parse(filename: str) -> dict:
    """
    Parses INI file 

    Args:
        filename: the name of the INI file
    Returns:
        dict of str: dict of str: str: dict maps section names to a dict that maps key names to thier values
    """
    file = open(filename, "r")
    data = {}
    counter = 1
    for line in file:
        line = line.rstrip("\n")
        if is_skippable(line):
            counter += 1
            continue
        elif is_section(line):
            line = line.strip()
            section = get_section(line)
            if len(section) == 0:
                raise Exception("Error at line " + str(counter) + ": Section can't be empty.")
            data[section] = {}
        elif is_key(line):
            keyName = get_key_name(line)
            keyValue = get_key_value(line)
            data[section][keyName] = keyValue
        else:
            raise Exception("Error at line " + str(counter))
        counter += 1
    return data


def is_section(line: str) -> bool:
    """
    Determines if the given line is a section or not
    Args:
        line: String of a line
    Returns:
        bool: true if line is a section and false otherwise
    """
    return len(line) > 0 and (line[0] == '[' and line[len(line) - 1] == ']')

def is_key(line: str) -> bool:
    """
    Determines if the given line is a key or not
    Args:
        line: String of a line
    Returns:
        bool: true if line is a key and false otherwise
    """
    return line.count('=') > 0

def is_skippable(line: str) -> bool:
    """
    Determines if the given line is skippable or not
    Args:
        line: String of a line
    Returns:
        bool: true if line is skippable and false otherwise
    """
    return len(line) == 0 or line[0] == ';'

def get_section(line: str) -> str:
    """
    Extract the section title from the line
    Args:
        line: string of a section line
    Returns:
        str: string of the section title
    """
    if len(line) < 2:
        raise Exception("Error: Section line can't be shorter than 2")
    return line[1:len(line) - 1]

def get_key_name(line: str) -> str:
    """
    Extract the key name from the line
    Args:
        line: string of a key line
    Returns:
        str: string of the key name
    """
    if line.find('=') == -1:
        raise Exception("Error: Key line must have equal sign seperating name and value")
    return line[:line.find('=')]

def get_key_value(line: str) -> str:
    """
    Extract the key value from the line
    Args:
        line: string of a key line
    Returns:
        str: string of the key value
    """
    if line.find('=') == -1:
        raise Exception("Error: Key line must have equal sign seperating name and value")
    return line[line.find('=') + 1:]