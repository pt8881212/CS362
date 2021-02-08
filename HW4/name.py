#function for testing the name
def fullName(first,last):
    if (len(first) == 0):
        raise ValueError("Error: First name cannot be an empty array.");
    if (len(last) == 0):
        raise ValueError("Error: Last name cannot be an empty array. ");
    for x in first:
        if(first.isdigit()):
            raise TypeError("First name cannot be integers.");
    for x in last:
        if(last.isdigit()):
            raise TypeError("Last name cannot be integers.");
    return first + " " + last;