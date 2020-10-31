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
        line = line.rstrip()
        line = line.strip()
        if isSkippable(line):
            counter += 1
            continue
        elif isSection(line):
            section = getSection(line)
            if len(section) == 0:
                raise Exception("Error at line " + str(counter) + ": Section can't be empty.")
            data[section] = {}
        elif isKey(line):
            keyName = getKeyName(line)
            keyValue = getKeyValue(line)
            data[section][keyName] = keyValue
        else:
            raise Exception("Error at line " + str(counter))
        counter += 1
    return data


def isSection(line: str) -> bool:
    """
    Determines if the given line is a section or not
    Args:
        line: String of a line
    Returns:
        bool: true if line is a section and false otherwise
    """
    return len(line) > 0 and (line[0] == '[' and line[len(line) - 1] == ']')

def isKey(line: str) -> bool:
    """
    Determines if the given line is a key or not
    Args:
        line: String of a line
    Returns:
        bool: true if line is a key and false otherwise
    """
    return line.count('=') > 0

def isSkippable(line: str) -> bool:
    """
    Determines if the given line is skippable or not
    Args:
        line: String of a line
    Returns:
        bool: true if line is skippable and false otherwise
    """
    return len(line) == 0 or line[0] == ';'

def getSection(line: str) -> str:
    """
    Extract the section title from the line
    Args:
        line: string of a section line
    Returns:
        str: string of the section title
    """
    if len(line) == 0:
        raise Exception("Error")
    return line[1:len(line) - 1]

def getKeyName(line: str) -> str:
    """
    Extract the key name from the line
    Args:
        line: string of a key line
    Returns:
        str: string of the key name
    """
    if line.find('=') == -1:
        raise Exception("Error")
    return line[:line.find('=')]

def getKeyValue(line: str) -> str:
    """
    Extract the key value from the line
    Args:
        line: string of a key line
    Returns:
        str: string of the key value
    """
    if line.find('=') == -1:
        raise Exception("Error")
    return line[line.find('=') + 1:]